from enum import Enum
from django.apps import apps
from django.contrib.auth import get_user_model
from rest_framework import serializers

OctoPrintDevice = apps.get_model("remote_control", "OctoPrintDevice")
AlertMessage = apps.get_model("alerts", "AlertMessage")
GeeksToken = apps.get_model("partners", "GeeksToken")
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
        fields = ("id", "")


class PartnerOctoPrintDeviceSerializer(serializers.ModelSerializer):
    """
    Please do not include any personally-identifying info or sensitive info in partner serializers
    """

    verified = serializers.SerializerMethodField()

    def get_verified(self, obj):
        return obj.geekstoken_set.first().verified

    class Meta:
        model = OctoPrintDevice
        fields = (
            "name",
            "model",
            "platform",
            "octoprint_version",
            "print_nanny_plugin_version",
            "print_nanny_client_version",
            "verified",
        )


class PartnerAlertSerializer(serializers.ModelSerializer):

    octoprint_device = PartnerOctoPrintDeviceSerializer()
    time = serializers.SerializerMethodField()

    def get_time(self, obj):
        return naturaltime(obj.created_dt)

    gcode_file = serializers.SerializerMethodField()
    def get_gcode_file(self, obj):
        if obj.print_session:
            return obj.print_session.gcode_file
        else:
            return None

    progress = serializers.SerializerMethodField()
    def get_progress(self, obj):
        if obj.print_session:
            return obj.print_session.progress
    
    token = serializers.SerializerMethodField()
    def get_token(self, obj):
        token = GeeksToken.objects.get(octoprint_device_id=obj.octoprint_device.id)
        return str(token)

    class Meta:
        model = AlertMessage
        fields = (
            "alert_type", 
            "alert_method", 
            "seen", 
            "sent", 
            "octoprint_device"
            "time",
            "token"
        )
