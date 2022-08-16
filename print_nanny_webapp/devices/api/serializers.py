import logging
from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from django.contrib.auth import get_user_model
from print_nanny_webapp.devices.models import (
    Pi,
    PiNatsApp,
    PiSettings,
    PiUrls,
    WebrtcStream,
    PublicKey,
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


class PublicKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicKey
        exclude = ("deleted",)

    def update_or_create(self, validated_data, pi):
        return PublicKey.objects.filter(pi=pi).update_or_create(
            pi=pi, defaults=validated_data
        )


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
            "created_dt",
            "updated_dt",
            "config_type",
            "active",
            "pi",
            "stream_secret",
            "stream_pin",
            "api_token",
            "admin_secret",
            "rtp_port",
            "rtp_domain",
            "pt",
            "rtpmap",
            "admin_port",
            "admin_url",
            "api_port",
            "api_url",
            "api_domain",
            "rtp_domain",
            "ws_port",
            "ws_url",
        )
        read_only_fields = ("pi", "config_type", "updated_dt", "created_dt")

    def update_or_create(self, validated_data, pi_id):
        return WebrtcStream.objects.filter(pi=pi_id).update_or_create(
            pi=pi_id, defaults=validated_data
        )

    def get_or_create(self, validated_data, pi_id):
        logger.info(
            "Attempting WebrtcStream.objects.get_or_create with validated_data=%s",
            validated_data,
        )
        # get_or_create method requires fkey relationship be 1) instance or 2) use __id field syntax
        pi = Pi.objects.get(id=pi_id)
        return WebrtcStream.objects.get_or_create(pi=pi, defaults=validated_data)


class SystemInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemInfo
        exclude = ("deleted",)

    def update_or_create(self, validated_data, pi):
        return SystemInfo.objects.filter(pi=pi).update_or_create(
            pi=pi, defaults=validated_data
        )


class PiSerializer(serializers.ModelSerializer):
    last_boot = serializers.CharField(read_only=True, allow_null=True)
    # alert_settings = AlertSettingsSerializer(read_only=True)
    settings = PiSettingsSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    system_info = SystemInfoSerializer(read_only=True)
    public_key = PublicKeySerializer(read_only=True)

    webrtc_edge = WebrtcStreamSerializer(read_only=True)
    webrtc_cloud = WebrtcStreamSerializer(read_only=True)

    octoprint_server = OctoPrintServerSerializer(read_only=True)

    urls = serializers.SerializerMethodField()

    def get_urls(self, obj) -> PiUrls:
        return obj.urls

    class Meta:
        model = Pi
        depth = 1
        exclude = ("deleted",)


class NatsAppSerializer(serializers.ModelSerializer):
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


class PrintNannyLicenseSerializer(serializers.Serializer):
    nats_app = NatsAppSerializer(read_only=True)
    api = PrintNannyApiConfigSerializer(read_only=True)
    pi = PiSerializer(read_only=True)

    class Meta:
        fields = ("pi", "api", "nats_app")

    def update(self, _instance, _validated_data):
        pass

    def create(self, _validated_data):
        pass
