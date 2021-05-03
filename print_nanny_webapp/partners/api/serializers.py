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
    print_nanny_plugin_version = serializers.SerializerMethodField()
    def get_print_nanny_plugin_version(self, obj):
        return obj.plugin_version
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
    
    time_remaining = serializers.SerializerMethodField()
    def get_time_remaining(self, obj):

        if obj.print_session and obj.print_session.time_remaining:
            now = timezone.now()
            remaining = now + obj.print_session.time_remainiing
            return naturaltime(remaining)
    
    manage_device_url = serializers.SerializerMethodField()
    def get_manage_device_url(self, obj):
        device_url = reverse(
            "dashboard:octoprint-devices:detail",
            kwargs={"pk": self.octoprint_device.id},
        )
        return device_url

    class Meta:
        model = AlertMessage
        fields = (
            "event_type", 
            "seen", 
            "sent", 
            "octoprint_device",
            "manage_device_url",
            "time",
            "token",
            "time_remaining",
            "progress",
            "gcode_file"
        )
