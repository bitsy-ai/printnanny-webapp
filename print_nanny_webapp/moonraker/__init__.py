from django.apps import AppConfig


class MoonrakerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "print_nanny_webapp.moonraker"

    def ready(self):
        try:
            import print_nanny_webapp.moonraker.signals  # noqa F401
        except ImportError:
            pass
