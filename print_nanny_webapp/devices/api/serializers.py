from rest_framework import serializers
from django.contrib.auth import get_user_model
from print_nanny_webapp.devices.models import (
    Device,
    Camera,
    CloudiotDevice,
    DeviceConfig,
    JanusAuth,
    PublicKey,
    SystemInfo,
    Task,
    TaskStatus,
    PrinterController,
    OnboardingTask,
)
from ..enum import (
    CameraType,
    DeviceReleaseChannel,
    PrintNannyEnv,
    PrinterSoftwareType,
    TaskType,
    TaskStatusType,
    PrintNannyEnv,
    OnboardingTaskType,
)
from print_nanny_webapp.users.api.serializers import UserSerializer

User = get_user_model()


class OnboardingTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnboardingTask
        fields = "__all__"


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
    status = serializers.ChoiceField(choices=TaskStatusType.choices)
    status_display = serializers.CharField(source="get_status_display", read_only=True)
    css_class = serializers.CharField(read_only=True)

    class Meta:
        model = TaskStatus
        exclude = ("deleted",)


class TaskSerializer(serializers.ModelSerializer):
    last_status = TaskStatusSerializer(read_only=True)
    task_type = serializers.ChoiceField(choices=TaskType.choices)
    active = serializers.BooleanField(default=True)
    task_type_display = serializers.CharField(
        source="get_task_type_display", read_only=True
    )

    class Meta:
        model = Task
        exclude = ("deleted",)


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

    def update_or_create(self, validated_data, device):
        return JanusAuth.objects.filter(device=device).update_or_create(
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

    active_cameras = CameraSerializer(many=True, read_only=True)
    active_tasks = TaskSerializer(many=True, read_only=True)
    cameras = CameraSerializer(read_only=True, many=True)
    cloudiot_device = CloudiotDeviceSerializer(read_only=True)
    dashboard_url = serializers.CharField(read_only=True)
    janus_local_url = serializers.CharField(read_only=True)
    last_task = TaskSerializer(read_only=True)
    monitoring_active = serializers.BooleanField(default=False)
    printer_controllers = PrinterControllerSerializer(read_only=True, many=True)
    user = UserSerializer(read_only=True)

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
