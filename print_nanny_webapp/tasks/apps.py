from django.apps import AppConfig


class TasksConfig(AppConfig):
    name = "print_nanny_webapp.tasks"
    default_auto_field = "django.db.models.BigAutoField"

    def ready(self) -> None:
        try:
            import print_nanny_webapp.tasks.signals  # noqa F401
        except ImportError:
            pass
