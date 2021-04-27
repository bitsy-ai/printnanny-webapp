from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PartnersConfig(AppConfig):
    name = "print_nanny_webapp.partners"
    verbose_name = _("Partners")

    def ready(self):
        pass
