from django.apps import AppConfig


class VideosConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "print_nanny_webapp.videos"

    def ready(self):
        try:
            import print_nanny_webapp.videos.signals  # noqa F401
        except ImportError:
            pass
