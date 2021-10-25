from rest_framework import serializers

from print_nanny_webapp.devices.models import (
    Device,
    Camera,
    CloudiotDevice,
    DesiredConfig,
    CurrentState,
    DevicePublicKey,
    PrinterController,
    # PrinterProfile,
    # OctoprintPrinterProfile,
)
from ..choices import DeviceReleaseChannel, PrinterSoftwareType
from print_nanny_webapp.devices.services import CACerts
from print_nanny_webapp.users.api.serializers import UserSerializer


class CameraSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    device = serializers.PrimaryKeyRelatedField(read_only=True)
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
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    device = serializers.PrimaryKeyRelatedField(read_only=True)
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
    config_topic = serializers.CharField(read_only=True)
    state_topic = serializers.CharField(read_only=True)

    gcp_project_id = serializers.CharField(read_only=True)
    gcp_region = serializers.CharField(read_only=True)
    gcp_cloudiot_device_registry = serializers.CharField(read_only=True)
    mqtt_bridge_hostname = serializers.CharField(read_only=True)
    mqtt_bridge_port = serializers.IntegerField(read_only=True)
    mqtt_client_id = serializers.CharField(read_only=True)

    user = serializers.PrimaryKeyRelatedField(read_only=True)
    device = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = CloudiotDevice
        fields = "__all__"


class DevicePublicKeySerializer(serializers.ModelSerializer):
    private_key = serializers.CharField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    device = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = DevicePublicKey
        fields = "__all__"
        read_only_fields = ("public_key", "public_key_checksum", "fingerprint", "user")


class CACertsSerializer(serializers.Serializer):
    primary = serializers.CharField(read_only=True)
    primary_checksum = serializers.CharField(read_only=True)
    backup = serializers.CharField(read_only=True)
    backup_checksum = serializers.CharField(read_only=True)


class DeviceKeyPairSerializer(serializers.Serializer):

    private_key = serializers.CharField(read_only=True)
    private_key_checksum = serializers.CharField(read_only=True)

    public_key = serializers.CharField(read_only=True)
    public_key_checksum = serializers.CharField(read_only=True)
    fingerprint_checksum = serializers.CharField(read_only=True)
    ca_certs = CACertsSerializer(read_only=True)


class DesiredConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesiredConfig
        fields = "__all__"


class CurrentStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentState
        fields = "__all__"


class DeviceSerializer(serializers.ModelSerializer):
    cloudiot_device = CloudiotDeviceSerializer(read_only=True, required=False)
    cameras = CameraSerializer(read_only=True, many=True)
    dashboard_url = serializers.CharField(read_only=True)

    desired_config = DesiredConfigSerializer(
        read_only=True,
        required=False,
        allow_null=True,
    )
    desired_config_topic = serializers.CharField(read_only=True)

    current_state = CurrentStateSerializer(
        read_only=True,
        required=False,
        allow_null=True,
    )
    current_state_topic = serializers.CharField(read_only=True)

    printer_controllers = PrinterControllerSerializer(read_only=True, many=True)
    public_key = DevicePublicKeySerializer(
        read_only=True, required=False, allow_null=True
    )

    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Device
        fields = "__all__"
