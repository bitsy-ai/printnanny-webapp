from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DashboardConfig(AppConfig):
    name = "hyper.dashboard"
    verbose_name = _("Dashboard")

    def ready(self):
        pass
