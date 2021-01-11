from django.apps import AppConfig
from django.conf import settings

import beeline

class AlertsConfig(AppConfig):
    name = "print_nanny_webapp.alerts"

    def ready(self):
        try:
            import print_nanny_webapp.alerts.signals  # noqa F401
        except ImportError:
            pass
        beeline.init(
            writekey=settings.HONEYCOMB_API_KEY,
            dataset=settings.HONEYCOMB_DATASET,
            service_name=settings.HONEYCOMB_SERVICE_NAME,
            #debug=settings.DEBUG,
        )