from flask import Flask, Response
from flask import request
import ast
import time

import os

from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor


def add_routes(app, tracer):
    @app.route("/login", methods=["POST"])
    def login():
        with tracer.start_as_current_span("login") as current_span:
            return "success"

    @app.route("/hello")
    def hello_route():
        return "hello"

    @app.route("/world")
    def world_route():
        return "world"

    @app.route("/order", methods=["POST", "GET"])
    def order():
        with tracer.start_as_current_span("order") as current_span:
            current_span.set_attribute("user_id", "99")

            # getting data from db
            try:
                work_with_db(tracer)
            except RuntimeError as re:
                r = Response("{0}".format(re), mimetype="text/plain")
                r.status_code = 503
                return r

            # calling an external service
            try:
                work_with_third_party(tracer)
                current_span.add_event(name="product ordered")
            except RuntimeError as re:
                r = Response("{0}".format(re), mimetype="text/plain")
                r.status_code = 503
                return r
            return "Success!"


def work_with_db(tracer):
    with tracer.start_as_current_span("work_with_db"):
        db_sleep = float(request.args.get("db_sleep", 0))
        is_db_error = ast.literal_eval(request.args.get("is_db_error", "False"))
        try:
            call_db(tracer, db_sleep, is_db_error)
        except RuntimeError as re:
            raise re


def call_db(tracer, db_sleep, is_error):
    with tracer.start_span("query_db"):
        mocked_call("Database XYZ", db_sleep, is_error)


def work_with_third_party(tracer):
    with tracer.start_as_current_span("call_payment"):

        srv_sleep = float(request.args.get("srv_sleep", 0))
        is_srv_error = ast.literal_eval(request.args.get("is_srv_error", "False"))

        try:
            call_external(srv_sleep, is_srv_error)
        except RuntimeError as re:
            """ """
            raise re


def call_external(srv_sleep, is_error):
    with tracer.start_span("do_request"):
        mocked_call("Payment", srv_sleep, is_error)


def mocked_call(what, sleep, is_error):
    if sleep > 0:
        time.sleep(sleep)
    if is_error:
        raise RuntimeError(what + " failed to process request")


def get_tracer(service_name, jaeger_host):
    trace.set_tracer_provider(
        TracerProvider(resource=Resource.create({SERVICE_NAME: service_name}))
    )
    tracer = trace.get_tracer(service_name)

    # create a JaegerExporter
    jaeger_exporter = JaegerExporter(
        agent_host_name=jaeger_host,
        agent_port=6831,
    )

    # Create a BatchSpanProcessor and add the exporter to it
    span_processor = BatchSpanProcessor(jaeger_exporter)

    # add to the tracer, for debugging if needed
    #
    #
    # from opentelemetry.sdk.trace.export import (SimpleSpanProcessor, ConsoleSpanExporter)
    #
    # SimpleSpanProcessor(ConsoleSpanExporter())
    trace.get_tracer_provider().add_span_processor(span_processor)
    return tracer


def get_app(tracer, service_name):
    app = Flask(service_name)

    FlaskInstrumentor().instrument_app(app)
    RequestsInstrumentor().instrument()

    add_routes(app, tracer)
    return app


if __name__ == "__main__":
    service_name = "my-shop-service"
    tracer = get_tracer(service_name, os.environ["JAEGER_HOST"])

    app = get_app(tracer, service_name)
    app.run(host="0.0.0.0", port=8080)
