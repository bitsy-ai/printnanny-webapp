from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppsConfig(AppConfig):
    name = "hyper.apps"
    verbose_name = _("Apps")

    def ready(self):
        pass