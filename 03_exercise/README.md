# Observability - Tracing with Opentelemetry

1. Przetesuj przykładową aplikację z zaimplementowanym tracingiem - [example/](example/). Zwróć uwagę:

   - instrumentacje biblioteki flask ([doc](https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/flask/flask.html))
   - skonfigurowanie jaegera ([docs](https://opentelemetry-python.readthedocs.io/en/latest/exporter/jaeger/jaeger.html))
   - request ([doc](https://opentelemetry-python.readthedocs.io/en/stable/getting-started.html#instrumentation-example-with-flask))

2. Dodaj do swojego projektu tracing.

3. [Dodatkowe] Załóż konto na [https://lightstep.com](https://lightstep.com).

## Materiały dodatkowe

- https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/overview.md
- [AWS i OT](https://aws.amazon.com/blogs/opensource/auto-instrumenting-a-python-application-with-an-aws-distro-for-opentelemetry-lambda-layer/)
- [GCP i OT](https://cloud.google.com/trace/docs/setup/python-ot)
- [Azure i OT](https://docs.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-overview)
