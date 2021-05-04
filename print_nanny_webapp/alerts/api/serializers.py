import logging
import inspect

from django.utils import timezone
from django.apps import apps
from django.urls import reverse
from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime


logger = logging.getLogger(__name__)

Alert = apps.get_model("alerts", "AlertMessage")
AlertSettings = apps.get_model("alerts", "AlertSettings")


class AlertSerializer(serializers.ModelSerializer):

    time = serializers.SerializerMethodField()

    def get_time(self, obj):
        return naturaltime(obj.updated_dt)

    gcode_file = serializers.SerializerMethodField()
    def get_gcode_file(self, obj):
        if obj.print_session:
            return obj.print_session.gcode_file
        else:
            return None

    print_progress = serializers.SerializerMethodField()
    def get_print_progress(self, obj):
        if obj.print_session:
            return obj.print_session.print_progress
    
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
            kwargs={"pk": obj.octoprint_device.id},
        )
        return device_url

    class Meta:
        model = Alert
        fields = [
            "time", 
            "gcode_file", 
            "print_progress",
            "time_remaining",
            "manage_device_url",
            "user",
            "octoprint_device",
            "alert_method",
            "event_type",
            "seen",
            "sent",
            "created_dt",
            "updated_dt"
        ]
        read_only_fields = ("user",)


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
