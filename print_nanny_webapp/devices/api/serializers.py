from collections.abc import Mapping
from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes

from print_nanny_webapp.devices.models import (
    Appliance,
    Camera,
    CloudIoTDevice,
    AppliancePKI,
    AnsibleFacts,
    PrinterController,
    # PrinterProfile,
    # OctoprintPrinterProfile,
)
from print_nanny_webapp.devices.services import CACerts


class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = "__all__"


class PrinterControllerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrinterController
        fields = "__all__"


##
# v1 Appliance Identity Provisioning (distributed via rpi-imager)
##
class CloudIoTDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CloudIoTDevice
        fields = "__all__"


class AppliancePKISerializer(serializers.ModelSerializer):
    class Meta:
        model = AppliancePKI
        fields = "__all__"


class AnsibleFactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppliancePKI
        fields = "__all__"


class ApplianceSerializer(serializers.ModelSerializer):
    pki = AppliancePKISerializer()
    ansible_facts = AnsibleFactsSerializer()
    cameras = CameraSerializer()
    printer_controllers = PrinterControllerSerializer()

    class Meta:
        model = Appliance
        fields = "__all__"


class CreateAppliancePKISerializer(serializers.ModelSerializer):
    class Meta:
        model = AppliancePKI
        fields = (
            "public_key",
            "public_key_checksum",
            "fingerprint",
        )


class CreateAnsibleFactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnsibleFacts
        fields = (
            "os_version",
            "os",
            "kernel_version",
            "hardware",
            "revision",
            "model",
            "serial",
            "cores",
            "ram",
            "cpu_flags",
            "release_channel",
            "json",
        )


class CreateApplianceSerializer(serializers.ModelSerializer):
    pki = CreateAppliancePKISerializer()
    ansible_facts = CreateAnsibleFactsSerializer()

    class Meta:
        model = Appliance
        fields = (
            "ansible_facts",
            "hostname",
            "pki",
        )

    def update_or_create(self, user, hostname, validated_data):
        return Appliance.objects.update_or_create(
            user=user, hostname=hostname, defaults=validated_data
        )
