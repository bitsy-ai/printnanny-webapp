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
    # PrinterController,
    # PrinterProfile,
    # OctoprintPrinterProfile,
)
from print_nanny_webapp.devices.services import CACerts


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
