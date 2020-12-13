from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PagesConfig(AppConfig):
    name = "hyper.pages"
    verbose_name = _("Pages")

    def ready(self):
        pass
