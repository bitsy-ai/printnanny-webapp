import logging
from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from django.contrib.auth import get_user_model
from django_nats_nkeys.api.serializers import (
    NatsOrganizationSerializer,
)


from print_nanny_webapp.devices.models import (
    Pi,
    PiNatsApp,
    PiSettings,
    PiUrls,
    WebrtcStream,
    SystemInfo,
)
from print_nanny_webapp.devices.enum import (
    JanusConfigType,
)
from print_nanny_webapp.users.api.serializers import UserSerializer
from print_nanny_webapp.utils.api.serializers import PrintNannyApiConfigSerializer
from print_nanny_webapp.octoprint.api.serializers import OctoPrintServerSerializer

User = get_user_model()

logger = logging.getLogger(__name__)

##
# v1 Pi Identity Provisioning (distributed via rpi-imager)
##


@extend_schema_field(OpenApiTypes.INT64)
class Int64Field(serializers.Field):
    def to_representation(self, value):
        return value


class PiSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PiSettings
        exclude = ("deleted",)


class WebrtcStreamSerializer(serializers.ModelSerializer):
    admin_secret = serializers.SerializerMethodField()

    def get_admin_secret(self, obj):
        """
        Do not leak Cloud admin secret in API responses
        """
        if obj.config_type == JanusConfigType.CLOUD:
            return ""
        return obj.admin_secret

    class Meta:
        model = WebrtcStream
        fields = (
            "active",
            "admin_port",
            "admin_secret",
            "admin_url",
            "api_domain",
            "api_port",
            "api_token",
            "api_url",
            "config_type",
            "created_dt",
            "id",
            "info",
            "is_admin",
            "pi",
            "pt",
            "rtp_domain",
            "video_rtp_port",
            "data_rtp_port",
            "rtpmap",
            "stream_pin",
            "stream_secret",
            "updated_dt",
            "ws_port",
            "ws_url",
        )
        read_only_fields = (
            "admin_port",
            "admin_secret",
            "admin_url",
            "api_port",
            "api_token",
            "api_url",
            "created_dt",
            "id",
            "info",
            "is_admin",
            "is_admin",
            "pi",
            "pt",
            "rtp_domain",
            "video_rtp_port",
            "data_rtp_port",
            "rtpmap",
            "stream_pin",
            "stream_secret",
            "updated_dt",
            "ws_port",
            "ws_url",
        )

    def update_or_create(self, validated_data, pi_id, config_type):
        return WebrtcStream.objects.filter(
            pi_id=pi_id, config_type=config_type
        ).update_or_create(
            pi_id=pi_id, config_type=config_type, defaults=validated_data
        )

    def get_or_create(self, validated_data, pi_id, config_type):
        logger.info(
            "Attempting WebrtcStream.objects.get_or_create with validated_data=%s",
            validated_data,
        )
        # get_or_create method requires fkey relationship be 1) instance or 2) use __id field syntax
        pi = Pi.objects.get(pi_id=pi_id, config_type=config_type)
        return WebrtcStream.objects.get_or_create(
            pi=pi, config_type=config_type, defaults=validated_data
        )


class SystemInfoSerializer(serializers.ModelSerializer):

    bootfs_available = serializers.IntegerField(read_only=True)
    bootfs_available_pretty = serializers.CharField(read_only=True)
    bootfs_used_pretty = serializers.CharField(read_only=True)
    bootfs_size_pretty = serializers.CharField(read_only=True)

    datafs_available = serializers.IntegerField(read_only=True)
    datafs_available_pretty = serializers.CharField(read_only=True)
    datafs_used_pretty = serializers.CharField(read_only=True)
    datafs_size_pretty = serializers.CharField(read_only=True)

    rootfs_available = serializers.IntegerField(read_only=True)
    rootfs_available_pretty = serializers.CharField(read_only=True)
    rootfs_size_pretty = serializers.CharField(read_only=True)
    rootfs_used_pretty = serializers.CharField(read_only=True)

    class Meta:
        model = SystemInfo

        exclude = ("deleted",)

    def update_or_create(self, validated_data, pi):
        return SystemInfo.objects.filter(pi=pi).update_or_create(
            pi=pi, defaults=validated_data
        )


class PiNatsAppSerializer(serializers.ModelSerializer):

    organization = NatsOrganizationSerializer()

    class Meta:
        model = PiNatsApp
        fields = (
            "id",
            "app_name",
            "json",
            "pi",
            "organization",
            "organization_user",
            "nats_server_uri",
            "nats_ws_uri",
            "nats_subject_pattern",
            "nats_subject_pattern_template",
        )


class PiSerializer(serializers.ModelSerializer):
    last_boot = serializers.CharField(read_only=True, allow_null=True)
    # alert_settings = AlertSettingsSerializer(read_only=True)
    settings = PiSettingsSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    system_info = SystemInfoSerializer(read_only=True)
    webrtc_edge = WebrtcStreamSerializer(read_only=True)
    webrtc_cloud = WebrtcStreamSerializer(read_only=True)

    octoprint_server = OctoPrintServerSerializer(
        read_only=True, required=False, allow_null=True
    )

    urls = serializers.SerializerMethodField(read_only=True)

    nats_app = PiNatsAppSerializer(read_only=True)

    def get_urls(self, obj) -> PiUrls:
        return obj.urls

    class Meta:
        model = Pi
        depth = 1
        exclude = ("deleted",)

    def update_or_create(self, validated_data, user_id, hostname):
        return Pi.objects.filter(user_id, hostname=hostname).update_or_create(
            user_id, hostname=hostname, defaults=validated_data
        )


class PrintNannyLicenseSerializer(serializers.Serializer):
    api = PrintNannyApiConfigSerializer(read_only=True)
    pi = PiSerializer(read_only=True)

    class Meta:
        fields = ("pi", "api")

    def update(self, _instance, _validated_data):
        pass

    def create(self, _validated_data):
        pass
