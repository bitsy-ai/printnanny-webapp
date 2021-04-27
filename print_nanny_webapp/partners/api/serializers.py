from enum import Enum
from django.apps import apps
from django.contrib.auth import get_user_model
from rest_framework import serializers

OctoPrintDevice = apps.get_model("remote_control", "OctoPrintDevice")
Alert = apps.get_model("alerts", "Alert")
User = get_user_model()
##
# Serializers for use with third-party partners and external systems
# These serializers exclude personally-identifying info
##


class PartnersEnum(Enum):
    """
    Used to determine if print_nanny_webapp.alerts.Alert.AlertMethodChoices is internal or external
    External partners receive a more limited set of data, with PII and other sensitive info excluded from serializers
    """

    PARTNER_3DGEEKS = "PARTNER_3DGEEKS"


class PartnerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class PartnerOctoPrintDeviceSerializer(serializers.ModelSerializer):
    """
    Please do not include any personally-identifying info or sensitive info in partner serializers
    """

    class Meta:
        model = OctoPrintDevice
        fields = (
            "name",
            "model",
            "platform",
            "octoprint_version",
            "plugin_version",
            "print_nanny_client_version",
        )


class PartnerAlertSerializer(serializers.ModelSerializer):

    octoprint_device = PartnerOctoPrintDeviceSerializer()
    user = PartnerUserSerializer()

    class Meta:
        model = Alert
        fields = ("user", "alert_type", "seen", "sent", "octoprint_device")
