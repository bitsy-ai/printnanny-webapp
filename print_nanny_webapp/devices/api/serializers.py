from rest_framework import serializers
from django.conf import settings

from django.contrib.auth import get_user_model
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
from ..enum import (
    CameraType,
    DeviceReleaseChannel,
    PrinterSoftwareType,
    TaskType,
    TaskStatusType,
)
from print_nanny_webapp.users.api.serializers import UserSerializer
from print_nanny_webapp.releases.api.serializers import ReleaseSerializer

User = get_user_model()


class CameraSerializer(serializers.ModelSerializer):
    camera_type = serializers.ChoiceField(
        choices=CameraType.choices,
        default=CameraType.PICAM,
    )

    class Meta:
        model = Camera
        fields = [field.name for field in Camera._meta.fields] + [
            "camera_type",
        ]


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
    task_topic = serializers.CharField(read_only=True)
    config_topic = serializers.CharField(read_only=True)
    state_topic = serializers.CharField(read_only=True)

    gcp_project_id = serializers.CharField(read_only=True)
    gcp_region = serializers.CharField(read_only=True)
    gcp_cloudiot_device_registry = serializers.CharField(read_only=True)
    mqtt_bridge_hostname = serializers.CharField(read_only=True)
    mqtt_bridge_port = serializers.IntegerField(read_only=True)
    mqtt_client_id = serializers.CharField(read_only=True)

    class Meta:
        model = CloudiotDevice
        exclude = ("deleted",)


class DeviceConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceConfig
        exclude = ("deleted",)


class TaskStatusSerializer(serializers.ModelSerializer):
    detail = serializers.CharField(required=False, allow_null=True)
    wiki_url = serializers.CharField(required=False, allow_null=True)

    class Meta:
        model = TaskStatus
        exclude = ("deleted",)


class TaskSerializer(serializers.ModelSerializer):
    last_status = TaskStatusSerializer(read_only=True)

    class Meta:
        model = Task
        exclude = ("deleted",)


class DeviceSerializer(serializers.ModelSerializer):

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
    active_cameras = CameraSerializer(many=True, read_only=True)

    class Meta:
        model = Device
        depth = 2
        read_only = ("bootstrap_release", "user", "last_task")
        exclude = ("deleted",)


class DeviceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceInfo
        exclude = ("deleted",)

    def update_or_create(self, validated_data, device):
        return DeviceInfo.objects.filter(device=device).update_or_create(
            device=device, defaults=validated_data
        )


class LicenseSerializer(serializers.ModelSerializer):
    """
    Deserialize data/license info into /opt/printnanny during License Activation
    """

    user = serializers.SerializerMethodField(read_only=True)

    def get_user(self, obj) -> int:
        return obj.user.id

    cloudiot_device = serializers.SerializerMethodField(read_only=True)

    def get_cloudiot_device(self, obj) -> int:
        return obj.cloudiot_device.num_id

    last_check_task = TaskSerializer(read_only=True)

    honeycomb_dataset = serializers.SerializerMethodField(read_only=True)

    def get_honeycomb_dataset(self, obj) -> str:
        return settings.HONEYCOMB_DATASET

    honeycomb_api_key = serializers.SerializerMethodField(read_only=True)

    def get_honeycomb_api_key(self, obj) -> str:
        return settings.HONEYCOMB_API_KEY

    class Meta:
        model = License
        read_only_fields = (
            "cloudiot_device" "device",
            "fingerprint",
            "honeycomb_api_key",
            "honeycomb_dataset",
            "janus_admin_secret",
            "janus_token",
            "last_check_task",
            "public_key",
            "user",
        )
        exclude = ("deleted",)
