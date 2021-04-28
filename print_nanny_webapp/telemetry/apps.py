from django.apps import AppConfig


class TelemetryConfig(AppConfig):
    name = "print_nanny_webapp.telemetry"
    # def ready(self):
    #     try:
    #         import print_nanny_webapp.telemetry.signals  # noqa F401
    #     except ImportError:
    #         pass
