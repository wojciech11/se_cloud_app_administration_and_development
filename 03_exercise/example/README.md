# Python && Tracing with OpenTelemetry

## Demo

*Please add your notes*

```bash
```

## Developemnt


```bash
python3 -m venv .venv
source .venv/bin/activate
```

```bash
# start all-jeager
docker-compose up  jaeger -d

export JAEGER_HOST=127.0.0.1
make run
```

Open [http://localhost:16686](http://localhost:16686) to see Jaeger UI.

```bash
make srv_random_trafic_complex_slow_db_and_svc
make srv_random_trafic_complex_failed_third_party
```

To bring more traffic:

```bash
make perf_test
```

## Reading materials

- [Prometheus i OT](https://open-telemetry.github.io/opentelemetry-python/getting-started.html#use-metrics-with-prometheus)
- [opentelemetry-python getting started](https://opentelemetry-python.readthedocs.io/en/stable/getting-started.html)
- https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/flask/flask.html
- https://opentelemetry-python.readthedocs.io/en/latest/exporter/jaeger/jaeger.html
- https://opentelemetry.lightstep.com/spans/
- https://blog.thundra.io/instrumentation-of-python-apps-with-opentracing
- https://www.datadoghq.com/blog/instrument-python-apps-with-datadog-and-opentelemetry/
- [Fix for Message Too Long errors on MacOS](https://github.com/jaegertracing/jaeger-client-node/issues/124#issuecomment-324222456) ([jaeger docs](https://www.jaegertracing.io/docs/1.19/client-libraries/#emsgsize-and-udp-buffer-limits))