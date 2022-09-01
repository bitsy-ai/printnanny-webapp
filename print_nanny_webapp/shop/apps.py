import logging
from django.apps import AppConfig

logger = logging.getLogger(__name__)


class ShopConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "print_nanny_webapp.shop"

    def ready(self):
        try:
            import print_nanny_webapp.shop.signals  # noqa F401

            logging.info(
                "Registered print_nanny_webapp.shop.signals %s",
                print_nanny_webapp.shop.signals,
            )
        except ImportError:
            pass
