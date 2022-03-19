# Observability - Tracing z Opentelemetry

1. Utwórz repozytorium na swoim koncie github (np., observability-tracing) z zawartością [example/](example/). Repozytorium powinno wyglądać tak:

   ```
   |- test_perf/
   |- docker-compose.yaml
   |- Dockerfile
   |- main.py
   |- Makefile
   \- ... # pozostałe pliki
   ```
  
   Proszę nie zapomnij o dodaniu `.gitignore` (możesz zacząć od [.gitignore](../.gitignore)). 

2. Przetesuj przykładową aplikację z zaimplementowanym tracingiem - . Zwróć uwagę:

   - instrumentacje biblioteki flask ([doc](https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/flask/flask.html)),
   - skonfigurowanie jaegera ([docs](https://opentelemetry-python.readthedocs.io/en/latest/exporter/jaeger/jaeger.html)),
   - jeśli rozbudujesz aplikację o wywołanie zewnętrznych serwisów, możesz dodać instrumentacje do biblioteki requests ([doc](https://opentelemetry-python.readthedocs.io/en/stable/getting-started.html#instrumentation-example-with-flask)).

3. Dodaj do swojego projektu tracing.

4. [Dodatkowe] Załóż konto na [https://lightstep.com](https://lightstep.com). Zmodyfikuj aplikację w taki sposób, aby można było wysyłac trace-y do lightstep.

## Materiały dodatkowe

- [OT python cookbook](https://opentelemetry.io/docs/instrumentation/python/cookbook/)
- https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/overview.md
- [AWS i OT](https://aws.amazon.com/blogs/opensource/auto-instrumenting-a-python-application-with-an-aws-distro-for-opentelemetry-lambda-layer/)
- [GCP i OT](https://cloud.google.com/trace/docs/setup/python-ot)
- [Azure i OT](https://docs.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-overview)
- https://httpbin.org
