from django.apps import AppConfig


class SurveysConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "print_nanny_webapp.surveys"

    def ready(self):
        try:
            import print_nanny_webapp.surveys.signals  # noqa F401
        except ImportError:
            pass
