from rest_framework import serializers

from print_nanny_webapp.devices.models import (
    Appliance,
    Camera,
    CloudIoTDevice,
    AppliancePublicKey,
    AnsibleFacts,
    PrinterController,
    # PrinterProfile,
    # OctoprintPrinterProfile,
)
from ..choices import ApplianceReleaseChannel, PrinterSoftwareType
from print_nanny_webapp.devices.services import CACerts
from print_nanny_webapp.users.api.serializers import UserSerializer


class CameraSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    appliance = serializers.PrimaryKeyRelatedField(read_only=True)
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
    appliance = serializers.PrimaryKeyRelatedField(read_only=True)
    software = serializers.ChoiceField(
        choices=PrinterSoftwareType.choices,
        default=PrinterSoftwareType.OCTOPRINT,
    )

    class Meta:
        model = PrinterController
        fields = "__all__"


##
# v1 Appliance Identity Provisioning (distributed via rpi-imager)
##
class CloudIoTDeviceSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    appliance = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = CloudIoTDevice
        fields = "__all__"


class AppliancePublicKeySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    appliance = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = AppliancePublicKey
        fields = "__all__"


class AnsibleFactsSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    appliance = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = AnsibleFacts
        fields = "__all__"


class ApplianceSerializer(serializers.ModelSerializer):

    public_key = AppliancePublicKeySerializer(
        read_only=True, required=False, allow_null=True
    )

    last_ansible_facts = AnsibleFactsSerializer(
        read_only=True,
        required=False,
        allow_null=True,
    )
    cameras = CameraSerializer(read_only=True, many=True)
    printer_controllers = PrinterControllerSerializer(read_only=True, many=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Appliance
        fields = "__all__"
