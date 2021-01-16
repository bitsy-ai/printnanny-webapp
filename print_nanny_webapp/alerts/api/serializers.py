import logging
import inspect

from django.urls import reverse
from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime

from rest_polymorphic.serializers import PolymorphicSerializer

from ..models import ManualVideoUploadAlert, RemoteControlCommandAlert, Alert, ProgressAlert, DefectAlert

logger = logging.getLogger(__name__)


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ["created_dt", "updated_dt", "user", "dismissed"]
        read_only_fields = ("user",)


class ProgressAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressAlert
        read_only_fields = ("user",)

class DefectAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefectAlert
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


class RemoteControlCommandAlertSerializer(serializers.ModelSerializer):

    dashboard_url = serializers.SerializerMethodField()

    def get_dashboard_url(self, obj):
        return reverse(
            "dashboard:octoprint-devices:detail", kwargs={"pk": obj.command.device.id}
        )

    naturaltime = serializers.SerializerMethodField()

    def get_naturaltime(self, obj):
        return naturaltime(obj.updated_dt)

    icon = serializers.CharField()
    description = serializers.CharField()
    color = serializers.CharField()
    title = serializers.CharField()

    class Meta:
        model = RemoteControlCommandAlert
        fields = [
            "alert_subtype",
            "alert_type",
            "color",
            "created_dt",
            "dashboard_url",
            "dismissed",
            "icon",
            "id",
            "naturaltime",
            "description",
            "seen",
            "title",
            "updated_dt",
            "user",
        ]
        read_only_fields = ("user",)


class ManualVideoUploadAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManualVideoUploadAlert
        fields = ["created_dt", "updated_dt", "user", "dismissed", "alert_type"]
        read_only_fields = ("user",)


class AlertPolymorphicSerializer(PolymorphicSerializer):
    resource_type_field_name = "type"

    model_serializer_mapping = {
        Alert: AlertSerializer,
        RemoteControlCommandAlert: RemoteControlCommandAlertSerializer,
        ManualVideoUploadAlert: ManualVideoUploadAlertSerializer,
        DefectAlert: DefectAlertSerializer,
        ProgressAlert: ProgressAlertSerializer
    }

    def to_resource_type(self, model_or_instance):
        return model_or_instance._meta.object_name.lower()
