from rest_framework import serializers

from print_nanny_webapp.devices.models import (
    Device,
    Camera,
    CloudiotDevice,
    DeviceConfig,
    DeviceInfo,
    DeviceState,
    License,
    PrinterController,
    # PrinterProfile,
    # OctoprintPrinterProfile,
)
from ..choices import DeviceReleaseChannel, PrinterSoftwareType
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
        fields = "__all__"


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
        fields = "__all__"


class APIConfigSerializer(serializers.Serializer):
    api_token = serializers.CharField()
    api_url = serializers.CharField()


class LicenseSerializer(serializers.ModelSerializer):
    api_config = APIConfigSerializer(read_only=True, required=False, default=None)

    class Meta:
        model = License
        fields = "__all__"
        read_only_fields = ("public_key", "public_key_checksum", "fingerprint", "user")


class CACertsSerializer(serializers.Serializer):
    primary = serializers.CharField(read_only=True)
    primary_checksum = serializers.CharField(read_only=True)
    backup = serializers.CharField(read_only=True)
    backup_checksum = serializers.CharField(read_only=True)


class DeviceConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceConfig
        fields = "__all__"


class DeviceStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceState
        fields = "__all__"


class DeviceSerializer(serializers.ModelSerializer):
    cloudiot_device = CloudiotDeviceSerializer(read_only=True, required=False)
    cameras = CameraSerializer(read_only=True, many=True)
    dashboard_url = serializers.CharField(read_only=True)

    bootstrap_release = ReleaseSerializer(
        read_only=True,
        required=False,
        allow_null=True,
    )

    printer_controllers = PrinterControllerSerializer(read_only=True, many=True)
    release_channel = serializers.ChoiceField(
        choices=DeviceReleaseChannel.choices,
        default=DeviceReleaseChannel.STABLE,
    )

    user = UserSerializer(read_only=True)
    active_license = LicenseSerializer(read_only=True)

    class Meta:
        model = Device
        fields = "__all__"
        depth = 2


class DeviceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceInfo
        fields = "__all__"
