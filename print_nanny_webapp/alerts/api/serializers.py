import logging
import time
from typing import Optional

from django.apps import apps
from django.urls import reverse
import drf_spectacular
from rest_framework import serializers
from drf_spectacular.utils import extend_schema_serializer
from django.contrib.humanize.templatetags.humanize import naturaltime


logger = logging.getLogger(__name__)

Alert = apps.get_model("alerts", "AlertMessage")
AlertSettings = apps.get_model("alerts", "AlertSettings")
from ..models import GenericAlertEventType


class AlertSerializer(serializers.ModelSerializer):

    event_type = serializers.ChoiceField(
        choices=GenericAlertEventType.choices,
        default=GenericAlertEventType.PRINT_NANNY_WEBAPP,
    )
    time = serializers.SerializerMethodField()

    def get_time(self, obj):
        return naturaltime(obj.updated_dt)

    gcode_file = serializers.SerializerMethodField()

    def get_gcode_file(self, obj):
        if getattr(obj, "print_session", None):
            return obj.print_session.gcode_file
        else:
            return None

    print_progress = serializers.SerializerMethodField()

    def get_print_progress(self, obj):
        if getattr(obj, "print_session", None):
            return obj.print_session.print_progress

    time_elapsed = serializers.SerializerMethodField()

    def get_time_elapsed(self, obj):
        if getattr(obj, "print_session", None):
            if obj.print_session and obj.print_session.time_elapsed:
                return time.strftime(
                    "%H:%M:%S", time.gmtime(obj.print_session.time_elapsed)
                )

    time_remaining = serializers.SerializerMethodField()

    def get_time_remaining(self, obj):
        if getattr(obj, "print_session", None):
            if obj.print_session and obj.print_session.time_remaining:
                return time.strftime(
                    "%H:%M:%S", time.gmtime(obj.print_session.time_remaining)
                )

    manage_device_url = serializers.SerializerMethodField()

    def get_manage_device_url(self, obj) -> Optional[str]:
        if getattr(obj, "octoprint_device", None):
            device_url = reverse(
                "dashboard:octoprint-devices:detail",
                kwargs={"pk": obj.octoprint_device.id},
            )
            return device_url

    message = serializers.SerializerMethodField()

    def get_message(self, obj) -> str:
        return obj.message

    class Meta:
        model = Alert
        fields = [
            "id",
            "time",
            "gcode_file",
            "print_progress",
            "time_elapsed",
            "time_remaining",
            "manage_device_url",
            "user",
            "octoprint_device",
            "event_type",
            "seen",
            "sent",
            "created_dt",
            "updated_dt",
            "message",
        ]
        read_only_fields = (
            "user",
            "alert_method",
        )


class AlertBulkRequestSerializer(serializers.Serializer):
    """
    Serializer used in POST /api/alerts/seen and POST /api/alerts/dismiss requests
    """

    ids = serializers.ListField(child=serializers.IntegerField())


class AlertBulkResponseSerializer(serializers.Serializer):
    """
    Serializer used in POST /api/alerts/seen and POST /api/alerts/dismiss requests
    """

    received = serializers.IntegerField()
    updated = serializers.IntegerField()


@extend_schema_serializer(many=False)
class AlertSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertSettings
        read_only_fields = ("user",)
        fields = "__all__"
