import logging
from django.apps import AppConfig

logger = logging.getLogger(__name__)


class EventsConfig(AppConfig):
    name = "print_nanny_webapp.events"
    default_auto_field = "django.db.models.BigAutoField"

    def ready(self) -> None:
        try:
            import print_nanny_webapp.events.signals  # noqa F401
        except ImportError:
            logger.warn(
                "Failed import print_nanny_webapp.events.signals - no signals will be registered for app=%s",
                self,
            )
