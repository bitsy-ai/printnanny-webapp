from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FormConfig(AppConfig):
    name = "hyper.form"
    verbose_name = _("Form")

    def ready(self):
        pass
