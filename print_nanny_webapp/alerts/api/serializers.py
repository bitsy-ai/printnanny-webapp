import logging
import inspect

from django.apps import apps
from django.urls import reverse
from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime

from rest_polymorphic.serializers import PolymorphicSerializer

logger = logging.getLogger(__name__)

Alert = apps.get_model("alerts", "Alert")
AlertEventSettings = apps.get_model("alerts", "AlertEventSettings")
ManualVideoUploadAlert = apps.get_model("alerts", "ManualVideoUploadAlert")
RemoteControlCommand = apps.get_model("remote_control", "RemoteControlCommand")
PrintSessionAlert = apps.get_model("alerts", "PrintSessionAlert")


class AlertSerializer(serializers.ModelSerializer):

    time = serializers.SerializerMethodField()

    def get_time(self, obj):
        return naturaltime(obj.updated_dt)

    class Meta:
        model = Alert
        fields = [
            "created_dt",
            "updated_dt",
            "alert_method",
            "user",
            "time",
            "seen",
            "octoprint_device",
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


class AlertPolymorphicSerializer(PolymorphicSerializer):
    resource_type_field_name = "type"

    model_serializer_mapping = {
        Alert: AlertSerializer,
    }

    def to_resource_type(self, model_or_instance):
        return model_or_instance._meta.object_name.lower()
