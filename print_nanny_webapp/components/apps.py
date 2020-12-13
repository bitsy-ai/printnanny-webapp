from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ComponentsConfig(AppConfig):
    name = "hyper.components"
    verbose_name = _("Components")

    def ready(self):
        pass
