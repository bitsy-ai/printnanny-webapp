from django.apps import AppConfig

class AlertsConfig(AppConfig):
    name = 'print_nanny_webapp.alerts'
    def ready(self):
        try:
            import print_nanny_webapp.alerts.signals  # noqa F401
        except ImportError:
            pass
