from django.apps import AppConfig


class ClientEventsConfig(AppConfig):
    name = 'print_nanny_webapp.client_events'
    def ready(self):
        try:
            import print_nanny_webapp.client_events.signals  # noqa F401
        except ImportError:
            pass
