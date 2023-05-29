import logging
from django.apps import AppConfig

logger = logging.getLogger(__name__)


class WorkspacesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "print_nanny_webapp.workspaces"

    def ready(self):
        try:
            import print_nanny_webapp.workspaces.signals  # noqa F401
            import print_nanny_webapp.utils.api.filters

            logging.info(
                "Registered print_nanny_webapp.shop.signals %s",
                print_nanny_webapp.workspaces.signals,
            )
        except ImportError:
            pass
