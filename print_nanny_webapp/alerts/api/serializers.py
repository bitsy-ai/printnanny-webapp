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
            "alert_method",
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


class AlertPolymorphicSerializer(PolymorphicSerializer):
    resource_type_field_name = "type"

    model_serializer_mapping = {
        Alert: AlertSerializer,
        PrintSessionAlert: PrintSessionAlertSerializer,
    }

    def to_resource_type(self, model_or_instance):
        return model_or_instance._meta.object_name.lower()


class AlertMethodSerializer(serializers.Serializer):

    label = serializers.CharField()
    value = serializers.CharField()
