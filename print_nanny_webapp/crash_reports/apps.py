from django.apps import AppConfig


class CrashReportsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "print_nanny_webapp.crash_reports"

    def ready(self):
        try:
            import print_nanny_webapp.crash_reports.signals  # noqa F401
        except ImportError:
            pass
