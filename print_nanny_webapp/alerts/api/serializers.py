import logging
import inspect

from django.apps import apps
from django.urls import reverse
from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime

from rest_polymorphic.serializers import PolymorphicSerializer

logger = logging.getLogger(__name__)

Alert = apps.get_model("alerts", "Alert")
AlertSettings = apps.get_model("alerts", "AlertSettings")
ManualVideoUploadAlert = apps.get_model("alerts", "ManualVideoUploadAlert")
RemoteControlCommandAlert = apps.get_model("alerts", "RemoteControlCommandAlert")
ProgressAlert = apps.get_model("alerts", "ProgressAlert")
RemoteControlCommand = apps.get_model("remote_control", "RemoteControlCommand")
PrintSessionAlert = apps.get_model("alerts", "PrintSessionAlert")
PrintSessionAlertSettings = apps.get_model("alerts", "PrintSessionAlertSettings")
RemoteControlCommandAlertSettings = apps.get_model("alerts", "RemoteControlCommandAlertSettings")
ProgressAlertSettings = apps.get_model("alerts", "ProgressAlertSettings")

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
        read_only_fields = ("user", "alert_methods", "alert_type", "polymorphic_ctype")


class CreatePrintSessionAlertSerializer(AlertSerializer):
    print_session = serializers.CharField()
    # dataflow writes uploaded video to gcs, so create method acccepts path string
    # this saves having to buffer the file bytes via django's http1 api
    annotated_video = serializers.CharField()

    def create(self, validated_data):
        PrintSession = apps.get_model("remote_control", "PrintSession")
        annotated_video = validated_data["annotated_video"]
        print_session = validated_data["print_session"]
        print_session = PrintSession.objects.get(session=print_session)
        return PrintSessionAlert.objects.create(
            user=print_session.user,
            print_session=print_session,
            annotated_video=annotated_video,
            octoprint_device=print_session.octoprint_device,
        )

    class Meta:
        model = PrintSessionAlert
        fields = ("print_session", "annotated_video")


class PrintSessionAlertSerializer(AlertSerializer):
    class Meta:
        model = PrintSessionAlert
        fields = "__all__"

        read_only_fields = (
            "alert_methods",
            "alert_type",
            "polymorphic_ctype",
            "user",
            "octoprint_device",
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


class RemoteControlCommandAlertSerializer(AlertSerializer):

    dashboard_url = serializers.SerializerMethodField()

    def get_dashboard_url(self, obj):
        return reverse(
            "dashboard:octoprint-devices:detail", kwargs={"pk": obj.command.device.id}
        )

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
            "alert_methods",
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
        ProgressAlert: ProgressAlertSerializer,
        PrintSessionAlert: PrintSessionAlertSerializer,
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
        ProgressAlert: ProgressAlertSettingsSerializer,
        # PrintSessionAlert: PrintSessionAlertSettingsSerializer
    }

    def to_resource_type(self, model_or_instance):
        return model_or_instance._meta.object_name.lower()


class AlertMethodSerializer(serializers.Serializer):

    label = serializers.CharField()
    value = serializers.CharField()
