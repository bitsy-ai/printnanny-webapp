from typing import TypedDict
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.conf import settings

from print_nanny_webapp.devices.models import (
    Device,
    Camera,
    CloudiotDevice,
    DeviceConfig,
    DeviceInfo,
    Task,
    TaskStatus,
    License,
    PrinterController,
    # PrinterProfile,
    # OctoprintPrinterProfile,
)
from ..enum import DeviceReleaseChannel, PrinterSoftwareType, FileLocator
from print_nanny_webapp.users.api.serializers import UserSerializer
from print_nanny_webapp.releases.api.serializers import ReleaseSerializer


class CameraSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(read_only=True)
    # device = serializers.PrimaryKeyRelatedField(read_only=True)
    camera_type = serializers.ChoiceField(
        choices=Camera.CameraType.choices,
        default=Camera.CameraType.RPI_CAMERA,
    )

    class Meta:
        model = Camera
        fields = [field.name for field in Camera._meta.fields] + [
            "url",
            "camera_type",
        ]
        extra_kwargs = {
            "url": {"view_name": "api:devices:camera-detail", "lookup_field": "id"},
        }


class PrinterControllerSerializer(serializers.ModelSerializer):
    software = serializers.ChoiceField(
        choices=PrinterSoftwareType.choices,
        default=PrinterSoftwareType.OCTOPRINT,
    )

    class Meta:
        model = PrinterController
        exclude = ("deleted",)


##
# v1 Device Identity Provisioning (distributed via rpi-imager)
##
class CloudiotDeviceSerializer(serializers.ModelSerializer):
    desired_config_topic = serializers.CharField(read_only=True)
    current_state_topic = serializers.CharField(read_only=True)

    gcp_project_id = serializers.CharField(read_only=True)
    gcp_region = serializers.CharField(read_only=True)
    gcp_cloudiot_device_registry = serializers.CharField(read_only=True)
    mqtt_bridge_hostname = serializers.CharField(read_only=True)
    mqtt_bridge_port = serializers.IntegerField(read_only=True)
    mqtt_client_id = serializers.CharField(read_only=True)

    class Meta:
        model = CloudiotDevice
        exclude = ("deleted",)


class Tokens(TypedDict):
    printnanny_api_token: str
    printnanny_api_url: str
    honeycomb_dataset: str  # distributed tracing dataset
    honeycomb_api_key: str  # write-only token


class LicenseSerializer(serializers.ModelSerializer):
    """
    Deserialize data/license info into /opt/printnanny during License Activation
    """

    tokens = serializers.SerializerMethodField(read_only=True)

    def get_tokens(self, obj) -> Tokens:
        api_token, _ = Token.objects.get_or_create(user=obj.device.user)
        return dict(
            printnanny_api_token=str(api_token),
            printnanny_api_url=self.context["request"].build_absolute_uri("/")[
                :-1
            ],  # remove trailing slash for use in API client base_url
            honeycomb_dataset=settings.HONEYCOMB_DATASET,
            honeycomb_api_key=settings.HONEYCOMB_API_KEY,
        )

    class Meta:
        model = License
        read_only_fields = (
            "tokens",
            "device",
            "public_key",
            "fingerprint",
            "user",
        )
        exclude = ("deleted",)


class CACertsSerializer(serializers.Serializer):
    primary = serializers.CharField(read_only=True)
    primary_checksum = serializers.CharField(read_only=True)
    backup = serializers.CharField(read_only=True)
    backup_checksum = serializers.CharField(read_only=True)


class DeviceConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceConfig
        exclude = ("deleted",)


class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        exclude = ("deleted",)


class TaskSerializer(serializers.ModelSerializer):
    last_status = TaskStatusSerializer(read_only=True)

    class Meta:
        model = Task
        exclude = ("deleted",)


class DeviceSerializer(serializers.ModelSerializer):

    install_path = serializers.ChoiceField(
        choices=FileLocator.choices, default=FileLocator.INSTALL_PATH, read_only=True
    )

    bootstrap_release = ReleaseSerializer(read_only=True)
    cloudiot_device = CloudiotDeviceSerializer(
        read_only=True, required=False, allow_null=True
    )
    cameras = CameraSerializer(read_only=True, many=True)
    dashboard_url = serializers.CharField(read_only=True)
    printer_controllers = PrinterControllerSerializer(read_only=True, many=True)
    release_channel = serializers.ChoiceField(
        choices=DeviceReleaseChannel.choices,
        default=DeviceReleaseChannel.STABLE,
    )

    user = UserSerializer(read_only=True)
    last_task = TaskSerializer(read_only=True)
    active_tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Device
        depth = 2
        read_only = ("bootstrap_release", "user", "last_task", "file_locator")
        exclude = ("deleted",)


class DeviceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceInfo
        exclude = ("deleted",)

    def update_or_create(self, validated_data, device):
        return DeviceInfo.objects.filter(device=device).update_or_create(
            device=device, defaults=validated_data
        )
