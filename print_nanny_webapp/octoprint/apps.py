from django.apps import AppConfig


class OctoprintConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "print_nanny_webapp.octoprint"

    def ready(self):
        try:
            import print_nanny_webapp.devices.signals  # noqa F401
        except ImportError:
            pass
