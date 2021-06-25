from django.apps import AppConfig


class AnalyticsConfig(AppConfig):
    name = "print_nanny_webapp.analytics"

    def ready(self):
        try:
            import print_nanny_webapp.analytics.signals  # noqa F401
        except ImportError:
            pass
