from enum import Enum
from typing import Union
from django.apps import apps
from django.contrib.auth import get_user_model
from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes

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


class Partner3DGeeksMetadataSerializer(serializers.ModelSerializer):
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


class Partner3DGeeksAlertSerializer(serializers.ModelSerializer):

    current_time = serializers.SerializerMethodField()
    @extend_schema_field({
        'oneOf': [
            {'type': 'int'},
            {'type': 'null'}
        ]
    })
    def get_current_time(self, obj):
        if obj.print_session:
            return obj.print_session.current_time

    time_left = serializers.SerializerMethodField()

    @extend_schema_field({
        'oneOf': [
            {'type': 'int'},
            {'type': 'null'}
        ]
    })
    def get_time_left(self, obj):
        if obj.print_session:
            return obj.print_session.time_remaining
    
    event = serializers.SerializerMethodField()
    def get_event(self, obj):
        return obj.event_type
    
    printer = serializers.SerializerMethodField()
    def get_printer(self, obj):
        return obj.octoprint_device.name

    print = serializers.SerializerMethodField()
    @extend_schema_field({
        'oneOf': [
            {'type': 'string'},
            {'type': 'null'}
        ]
    })
    def get_print(self, obj):
        if obj.print_session:
            return obj.print_session.gcode_file

    percent = serializers.SerializerMethodField()
    @extend_schema_field({
        'oneOf': [
            {'type': 'int'},
            {'type': 'null'}
        ]
    })
    def get_percent(self, obj):
        if obj.print_session:
            return obj.print_session.progress

    token = serializers.SerializerMethodField()

    def get_token(self, obj):
        token = GeeksToken.objects.get(octoprint_device_id=obj.octoprint_device.id)
        return str(token)

    device_url = serializers.SerializerMethodField()
    def get_device_url(self, obj):
        device_url = reverse(
            "dashboard:octoprint-devices:detail",
            kwargs={"pk": self.octoprint_device.id},
        )
        return device_url

    image = serializers.SerializerMethodField()
    @extend_schema_field({
        'oneOf': [
            {'type': 'string'},
            {'type': 'null'}
        ]
    })
    def get_image(self, obj):
        return None

    class Meta:
        model = AlertMessage
        fields = (
            "event",
            "token",
            "printer",
            "print",
            "current_time",
            "time_left",
            "percent",
            "image"
        )
