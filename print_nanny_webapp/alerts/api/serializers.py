import logging
import inspect

from django.urls import reverse
from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime

from rest_polymorphic.serializers import PolymorphicSerializer

from ..models import (
    ManualVideoUploadAlert,
    RemoteControlCommandAlert,
    Alert,
    ProgressAlert,
    DefectAlert,
    AlertSettings,
    ProgressAlertSettings,
    RemoteControlCommandAlertSettings,
    DefectAlertSettings,
)

logger = logging.getLogger(__name__)


class AlertSerializer(serializers.ModelSerializer):

    time = serializers.SerializerMethodField()

    def get_time(self, obj):
        return naturaltime(obj.updated_dt)

    class Meta:
        model = Alert
        fields = ["created_dt", "updated_dt", "user", "dismissed", "time"]
        read_only_fields = ("user",)


class ProgressAlertSerializer(AlertSerializer):
    class Meta:
        model = ProgressAlert
        fields = "__all__"
        read_only_fields = ("user", "alert_method", "alert_type", "polymorphic_ctype")


class DefectAlertSerializer(AlertSerializer):

    print_session = serializers.CharField()
    class Meta:
        model = DefectAlert
        fields = ["print_session", "octoprint_device", "print_job", "print_session", "seen", "dismissed", "user"]
        read_only_fields = ("alert_method", "alert_type", "polymorphic_ctype", "print_job")


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


class RemoteControlCommandAlertSerializer(AlertSerializer):

    dashboard_url = serializers.SerializerMethodField()

    def get_dashboard_url(self, obj):
        return reverse(
            "dashboard:octoprint-devices:detail", kwargs={"pk": obj.command.device.id}
        )

    snapshot_url = serializers.SerializerMethodField()

    def get_snapshot_url(self, obj):
        lastest_snapshot = obj.command.snapshots.order_by("-created_dt").first()
        if lastest_snapshot:
            return lastest_snapshot.image.url

    metadata = serializers.SerializerMethodField()

    def get_metadata(self, obj):
        return obj.command.metadata

    icon = serializers.CharField()
    description = serializers.CharField()
    color = serializers.CharField()
    title = serializers.CharField()

    class Meta:
        model = RemoteControlCommandAlert
        fields = [
            "alert_subtype",
            "alert_method",
            "alert_type",
            "color",
            "created_dt",
            "dashboard_url",
            "dismissed",
            "metadata",
            "icon",
            "id",
            "time",
            "description",
            "seen",
            "snapshot_url",
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
        ProgressAlert: ProgressAlertSerializer,
    }

    def to_resource_type(self, model_or_instance):
        return model_or_instance._meta.object_name.lower()


class AlertSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertSettings
        fields = "__all__"
        read_only_fields = ("user",)


class CommandAlertSettingsSerializer(AlertSettingsSerializer):
    class Meta:
        model = RemoteControlCommandAlertSettings
        fields = "__all__"
        read_only_fields = ("user",)


class DefectAlertSettingsSerializer(AlertSettingsSerializer):
    class Meta:
        model = DefectAlertSettings
        fields = "__all__"
        read_only_fields = ("user",)


class ProgressAlertSettingsSerializer(AlertSettingsSerializer):
    class Meta:
        model = ProgressAlertSettings
        fields = "__all__"
        read_only_fields = ("user",)


class AlertSettingsPolymorphicSerializer(PolymorphicSerializer):
    resource_type_field_name = "type"

    model_serializer_mapping = {
        AlertSettings: AlertSettingsSerializer,
        RemoteControlCommandAlertSettings: CommandAlertSettingsSerializer,
        DefectAlertSettings: DefectAlertSettingsSerializer,
        ProgressAlert: ProgressAlertSettingsSerializer,
    }

    def to_resource_type(self, model_or_instance):
        return model_or_instance._meta.object_name.lower()


class AlertMethodSerializer(serializers.Serializer):

    label = serializers.CharField()
    value = serializers.CharField()

