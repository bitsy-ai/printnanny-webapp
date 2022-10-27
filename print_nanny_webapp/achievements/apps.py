from django.apps import AppConfig


class AchievementsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "print_nanny_webapp.achievements"

    def ready(self):
        try:
            import print_nanny_webapp.achievements.signals  # noqa F401
        except ImportError:
            pass
