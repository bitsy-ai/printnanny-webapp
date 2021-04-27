from typing import Union

from django.apps import apps
from print_nanny_webapp.alerts.api.serializer import AlertSerializer
from print_nanny_webapp.partners.api.serializer import PartnerAlertSerializer, PartnersEnum

AlertModel = apps.get_model("alerts", "Alert")
class AlertTask:

    serializer = AlertSerializer
    partner_serializer = PartnerAlertSerializer

    def __init__(self, instance: AlertModel):
        self.instance = instance
    

    def get_serializer(self) -> Union[AlertSerializer, PartnerAlertSerializer]:
        if self.instance.alert_method.value in PartnersEnum:
            return self.partner_serializer(self.instance)
        return self.serializer(self.instance)