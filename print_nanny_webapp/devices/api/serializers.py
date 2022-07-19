import logging
from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from django.contrib.auth import get_user_model
from print_nanny_webapp.devices.models import (
    Device,
    DeviceSettings,
    CloudiotDevice,
    DeviceUrls,
    WebrtcStream,
    PublicKey,
    SystemInfo,
)
from ..enum import (
    JanusConfigType,
)
from print_nanny_webapp.users.api.serializers import UserSerializer
from print_nanny_webapp.utils.api.serializers import PrintNannyApiConfigSerializer
from print_nanny_webapp.alerts.api.serializers import AlertSettingsSerializer
from print_nanny_webapp.octoprint.api.serializers import OctoPrintServerSerializer

User = get_user_model()

logger = logging.getLogger(__name__)

##
# v1 Device Identity Provisioning (distributed via rpi-imager)
##


@extend_schema_field(OpenApiTypes.INT64)
class Int64Field(serializers.Field):
    def to_representation(self, value):
        return value


class DeviceSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceSettings
        exclude = ("deleted",)


class CloudiotDeviceSerializer(serializers.ModelSerializer):
    command_topic = serializers.CharField(read_only=True)
    event_topic = serializers.CharField(read_only=True)
    config_topic = serializers.CharField(read_only=True)
    state_topic = serializers.CharField(read_only=True)

    gcp_resource = serializers.CharField(read_only=True)
    gcp_project_id = serializers.CharField(read_only=True)
    gcp_region = serializers.CharField(read_only=True)
    gcp_cloudiot_device_registry = serializers.CharField(read_only=True)
    mqtt_bridge_hostname = serializers.CharField(read_only=True)
    mqtt_bridge_port = serializers.IntegerField(read_only=True)
    mqtt_client_id = serializers.CharField(read_only=True)
    num_id = Int64Field(read_only=True)

    class Meta:
        model = CloudiotDevice
        exclude = ("deleted",)
        read_only_fields = (
            "num_id",
            "name",
            "device",
            "id",
        )


class PublicKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicKey
        exclude = ("deleted",)

    def update_or_create(self, validated_data, device):
        return PublicKey.objects.filter(device=device).update_or_create(
            device=device, defaults=validated_data
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
            "device",
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
        read_only_fields = ("device", "config_type", "updated_dt", "created_dt")

    def update_or_create(self, validated_data, device_id):
        return WebrtcStream.objects.filter(device=device_id).update_or_create(
            device=device_id, defaults=validated_data
        )

    def get_or_create(self, validated_data, device_id):
        logger.info(
            "Attempting WebrtcStream.objects.get_or_create with validated_data=%s",
            validated_data,
        )
        # get_or_create method requires fkey relationship be 1) instance or 2) use __id field syntax
        device = Device.objects.get(id=device_id)
        return WebrtcStream.objects.get_or_create(
            device=device, defaults=validated_data
        )


class SystemInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemInfo
        exclude = ("deleted",)

    def update_or_create(self, validated_data, device):
        return SystemInfo.objects.filter(device=device).update_or_create(
            device=device, defaults=validated_data
        )


class DeviceSerializer(serializers.ModelSerializer):
    last_boot = serializers.CharField(read_only=True)
    alert_settings = AlertSettingsSerializer(read_only=True)
    settings = DeviceSettingsSerializer(read_only=True)
    cloudiot_device = CloudiotDeviceSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    system_info = SystemInfoSerializer(read_only=True)
    public_key = PublicKeySerializer(read_only=True)

    janus_edge = WebrtcStreamSerializer(read_only=True)
    janus_cloud = WebrtcStreamSerializer(read_only=True)

    octoprint_server = OctoPrintServerSerializer(read_only=True)

    urls = serializers.SerializerMethodField()

    def get_urls(self, obj) -> DeviceUrls:
        return obj.urls

    class Meta:
        model = Device
        depth = 1
        exclude = ("deleted",)


class ConfigSerializer(serializers.Serializer):
    api = PrintNannyApiConfigSerializer(read_only=True)
    device = DeviceSerializer(read_only=True)

    class Meta:
        fields = (
            "device",
            "api",
        )
