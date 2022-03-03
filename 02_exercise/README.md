## Ćwiczenia 2

### Monitoring

1. Uruchom i przeanalizuj przykład aplikacji monitorowanej przez Protheusa dostępny na [githubie](https://github.com/wojciech12/talk_monitoring_with_prometheus/tree/master/) dla Pythona.

   Zauważ, jeśli będą problemy z `wrk`, możesz wykorzystać [locust](https://locust.io/) ([konfiguracja](https://github.com/wojciech11/se_perf_testing_basics/blob/master/exercise_2/test_perf/locustfile.py), [jak uruchomić](https://github.com/wojciech11/se_perf_testing_basics/tree/master/exercise_2#exercise-2)).

2. Przeczytaj co to jest [Histogram](https://prometheus.io/docs/concepts/metric_types/#histogram) oraz o [konwencjach nazewnictwa metryk](https://prometheus.io/docs/practices/naming/).

3. Utwórz repozytorium na swoim koncie githuba i przekopiuj kod. Prześlij link wykładowcy.

### Logging

Uruchom i przeanalizuj przykładową aplikację pokazującą ustrukturyzowane logowanie dostępną na [githubie](https://github.com/wojciech12/talk_observability_logging/).

### Projekt

1. Dodaj do swojego projektu ustrukturyzowane logowanie, jeśli nie masz jeszcze pomysłu, napisz prostą aplikację symulującą sklep lub inny serwis `API` lub web.

2. **Dodatkowe** dodaj integrację z Prometheusem w swojej aplikacji.

## Materiały dodatkowe

- [Prometheus naming conventions](https://prometheus.io/docs/practices/naming/)
- [Prometheus exporters](https://prometheus.io/docs/instrumenting/exporters/)
- [Opentelemetry](https://opentelemetry.io/) i [biblioteki](https://github.com/open-telemetry)
- Przykładowe biblioteki dla Pythona: [structlog](https://www.structlog.org/en/stable/) lub [loguru](https://github.com/Delgan/loguru)
- Przykładowe biblioteki dla Golanga: [zap](https://github.com/uber-go/zap) lub [logrus](https://github.com/sirupsen/logrus)
- [Opentelemetry i AWS Lambdas](https://aws.amazon.com/blogs/opensource/auto-instrumenting-a-python-application-with-an-aws-distro-for-opentelemetry-lambda-layer/)
- Jak dużo poziomów logowania potrzebujemy? - https://dave.cheney.net/2015/11/05/lets-talk-about-logging
- [Grafana best practices](https://grafana.com/docs/grafana/latest/best-practices/common-observability-strategies/#the-four-golden-signals)
- [Brendan Gregg blog](https://www.brendangregg.com/overview.html)([USE](https://www.brendangregg.com/usemethod.html))
