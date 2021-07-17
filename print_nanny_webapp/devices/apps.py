from django.apps import AppConfig


class DevicesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "print_nanny_webapp.devices"

    def ready(self):
        try:
            import print_nanny_webapp.devices.signals  # noqa F401
        except ImportError:
            pass
