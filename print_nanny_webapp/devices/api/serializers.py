import logging
from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from django.contrib.auth import get_user_model
from print_nanny_webapp.devices.models import (
    Device,
    CloudiotDevice,
    License,
    JanusAuth,
    JanusStream,
    PublicKey,
    SystemInfo,
)
from ..enum import (
    DeviceReleaseChannel,
    JanusConfigType,
)
from print_nanny_webapp.users.api.serializers import UserSerializer

User = get_user_model()

logger = logging.getLogger(__name__)

##
# v1 Device Identity Provisioning (distributed via rpi-imager)
##


@extend_schema_field(OpenApiTypes.INT64)
class Int64Field(serializers.Field):
    def to_representation(self, value):
        return value


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


class JanusAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = JanusAuth
        exclude = ("deleted",)
        read_only_fields = ("device",)

    def update_or_create(self, validated_data, user):
        return JanusAuth.objects.filter(user=user).update_or_create(
            user=user, defaults=validated_data
        )

    def get_or_create(self, validated_data, user, config_type):
        return JanusAuth.objects.get_or_create(
            user=user, config_type=config_type, defaults=validated_data
        )


class JanusStreamSerializer(serializers.ModelSerializer):
    auth = JanusAuthSerializer(read_only=True)
    api_domain = serializers.CharField(read_only=True)
    api_port = serializers.IntegerField(read_only=True)
    api_url = serializers.CharField(read_only=True)
    admin_url = serializers.CharField(read_only=True)
    admin_port = serializers.IntegerField(read_only=True)
    rtp_domain = serializers.CharField(read_only=True)
    ws_url = serializers.CharField(read_only=True)
    ws_port = serializers.IntegerField(read_only=True)
    config_type = serializers.CharField(read_only=True)

    class Meta:
        model = JanusStream
        exclude = ("deleted",)
        read_only_fields = ("device", "rtp_port", "pin", "secret", "active", "info")

    def update_or_create(self, validated_data, device_id):
        return JanusStream.objects.filter(device=device_id).update_or_create(
            device=device_id, defaults=validated_data
        )

    def get_or_create(self, validated_data, device_id):
        logger.info(
            "Attempting JanusStream.objects.get_or_create with validated_data=%s",
            validated_data,
        )
        # get_or_create method requires fkey relationship be 1) instance or 2) use __id field syntax
        device = Device.objects.get(id=device_id)
        return JanusStream.objects.get_or_create(device=device, defaults=validated_data)


class JanusCloudStreamSerializer(serializers.ModelSerializer):
    auth = JanusAuthSerializer(read_only=True)
    api_domain = serializers.CharField(read_only=True)
    api_port = serializers.IntegerField(read_only=True)
    api_url = serializers.CharField(read_only=True)
    admin_url = serializers.CharField(read_only=True)
    admin_port = serializers.IntegerField(read_only=True)
    rtp_port = serializers.IntegerField(read_only=True)
    rtp_domain = serializers.CharField(read_only=True)
    ws_url = serializers.CharField(read_only=True)
    ws_port = serializers.IntegerField(read_only=True)
    config_type = serializers.SerializerMethodField(read_only=True)

    def get_config_type(self, _obj) -> str:
        return JanusConfigType.CLOUD

    class Meta:
        model = JanusStream
        exclude = ("deleted",)

    def update_or_create(self, validated_data, device_id):
        return JanusStream.objects.filter(device=device_id).update_or_create(
            device=device_id, config_type=JanusConfigType.CLOUD, defaults=validated_data
        )

    def get_or_create(self, validated_data, device_id):
        logger.info(
            "Attempting JanusStream.objects.get_or_create with validated_data=%s",
            validated_data,
        )
        # get_or_create method requires fkey relationship be 1) instance or 2) use __id field syntax
        device = Device.objects.get(id=device_id)
        return JanusStream.objects.get_or_create(
            device=device, config_type=JanusConfigType.CLOUD, defaults=validated_data
        )


class JanusEdgeStreamSerializer(serializers.ModelSerializer):
    auth = JanusAuthSerializer()
    api_domain = serializers.CharField()
    api_port = serializers.IntegerField()
    api_url = serializers.CharField(read_only=True)
    admin_url = serializers.CharField(read_only=True)
    admin_port = serializers.IntegerField()
    ws_port = serializers.IntegerField()
    rtp_domain = serializers.CharField()
    ws_url = serializers.CharField(read_only=True)
    config_type = serializers.SerializerMethodField()

    def get_config_type(self, _obj) -> str:
        return JanusConfigType.EDGE

    class Meta:
        model = JanusStream
        exclude = ("deleted",)

    def update_or_create(self, validated_data, device_id):
        return JanusStream.objects.filter(device=device_id).update_or_create(
            device=device_id, config_type=JanusConfigType.EDGE, defaults=validated_data
        )

    def get_or_create(self, validated_data, device_id):
        logger.info(
            "Attempting JanusStream.objects.get_or_create with validated_data=%s",
            validated_data,
        )
        # get_or_create method requires fkey relationship be 1) instance or 2) use __id field syntax
        device = Device.objects.get(id=device_id)
        return JanusStream.objects.get_or_create(
            device=device, config_type=JanusConfigType.EDGE, defaults=validated_data
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

    cloudiot_device = CloudiotDeviceSerializer(read_only=True)
    cloud_url = serializers.CharField(read_only=True)
    edge_url = serializers.CharField(read_only=True)
    video_test_url = serializers.CharField(read_only=True)
    janus_auth = JanusAuthSerializer(read_only=True)
    janus_local_url = serializers.CharField(read_only=True)
    monitoring_active = serializers.BooleanField(default=False)
    setup_complete = serializers.BooleanField(default=False)
    user = UserSerializer(read_only=True)
    octoprint_url = serializers.CharField(read_only=True)

    release_channel = serializers.ChoiceField(
        choices=DeviceReleaseChannel.choices,
        default=DeviceReleaseChannel.STABLE,
    )
    system_info = SystemInfoSerializer(read_only=True)
    public_key = PublicKeySerializer(read_only=True)

    class Meta:
        model = Device
        depth = 2
        exclude = ("deleted",)


class LicenseSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=True)
    user = serializers.PrimaryKeyRelatedField(
        required=True, queryset=User.objects.all()
    )

    class Meta:
        model = License
        exclude = ("deleted",)
