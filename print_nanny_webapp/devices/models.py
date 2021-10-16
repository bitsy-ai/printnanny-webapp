import logging
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth import get_user_model
from google.cloud import iot_v1 as cloudiot_v1
from google.protobuf.json_format import MessageToDict
from django.conf import settings

from polymorphic.models import PolymorphicModel
from safedelete.models import SafeDeleteModel, SOFT_DELETE
from safedelete.managers import SafeDeleteManager
from safedelete.signals import pre_softdelete

from .choices import ApplianceReleaseChannel, PrinterSoftwareType

from print_nanny_webapp.devices.services import (
    delete_cloudiot_device,
    generate_keypair,
    update_or_create_cloudiot_device,
)

UserModel = get_user_model()
logger = logging.getLogger(__name__)


def pre_softdelete_cloudiot_device(instance=None, **kwargs):
    fn = getattr(instance, "pre_softdelete", None)
    if hasattr(fn, "__call__"):
        return fn()


pre_softdelete.connect(pre_softdelete_cloudiot_device)


class Appliance(SafeDeleteModel):
    """ """

    class Meta:
        unique_together = ("user", "hostname")

    _safedelete_policy = SOFT_DELETE
    created_dt = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_dt = models.DateTimeField(db_index=True, auto_now=True)
    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, related_name="appliances"
    )
    hostname = models.CharField(max_length=255)


class CloudIoTDevice(SafeDeleteModel):
    """
    Instance of cloudiot.projects.locations.registries.devices#Device
    https://cloud.google.com/iot/docs/reference/cloudiot/rest/v1/projects.locations.registries.devices#Device
    """

    def pre_softdelete(self):
        return delete_cloudiot_device(self.numId)

    numId = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    id = models.CharField(max_length=255)

    appliance = models.OneToOneField(
        Appliance,
        on_delete=models.CASCADE,
        related_name="cloudiot_device",
        db_index=True,
    )


class AppliancePKI(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    public_key_path = models.CharField(max_length=255)
    private_key_path = models.CharField(max_length=255)
    public_key = models.TextField()
    public_key_checksum = models.CharField(max_length=255)
    fingerprint = models.CharField(max_length=255)
    appliance = models.OneToOneField(
        Appliance, on_delete=models.CASCADE, related_name="pki", db_index=True
    )


class AnsibleFacts(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    appliance = models.OneToOneField(
        Appliance, on_delete=models.CASCADE, related_name="ansible_facts", db_index=True
    )
    # platform info
    os_version = models.CharField(max_length=255)
    os = models.CharField(max_length=255)
    kernel_version = models.CharField(max_length=255)
    # hardware info
    # /proc/cpuinfo HARDWARE
    hardware = models.CharField(max_length=255, null=True)
    # /proc/cpuinfo REVISION
    revision = models.CharField(max_length=255, null=True)
    # /proc/cpuinfo MODEL
    model = models.CharField(max_length=255, null=True)
    # /proc/cpuinfo SERIAL
    serial = models.CharField(max_length=255, null=True)
    # /proc/cpuinfo MAX PROCESSOR
    cores = models.IntegerField()
    ram = models.BigIntegerField()
    cpu_flags = ArrayField(models.CharField(max_length=255))

    release_channel = models.CharField(
        max_length=8,
        choices=ApplianceReleaseChannel.choices,
        default=ApplianceReleaseChannel.MAIN,
    )
    json = models.JSONField()


class Camera(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    class Meta:
        unique_together = ("user", "name")

    class CameraType(models.TextChoices):
        RPI_CAMERA = "Raspberry Pi Camera Module", "Raspberry Pi Camera Module"
        USB_CAMERA = (
            "Raspberry Pi USB Camera",
            "Raspberry Pi USB Camera",
        )
        IP_CAMERA = "Generic RTSP/RTMP IP Camera", "Generic RTSP/RTMP IP Camera"

    _safedelete_policy = SOFT_DELETE

    created_dt = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_dt = models.DateTimeField(db_index=True, auto_now=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    appliance = models.ForeignKey(
        Appliance, on_delete=models.CASCADE, related_name="cameras"
    )
    name = models.CharField(max_length=255)
    camera_type = models.CharField(max_length=255, choices=CameraType.choices)
    camera_source = models.CharField(max_length=255)


class PrinterController(PolymorphicModel, SafeDeleteModel):

    _safedelete_policy = SOFT_DELETE

    created_dt = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_dt = models.DateTimeField(db_index=True, auto_now=True)
    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, related_name="printer_controllers"
    )
    appliance = models.ForeignKey(
        Appliance, on_delete=models.CASCADE, related_name="printer_controllers"
    )
    software = models.CharField(max_length=12, choices=PrinterSoftwareType.choices)


# class PrinterProfile(SafeDeleteModel):
#     class Meta:
#         unique_together = (
#             "user",
#             "name",
#         )
#         abstract = True

#     _safedelete_policy = SOFT_DELETE
#     created_dt = models.DateTimeField(db_index=True, auto_now_add=True)
#     updated_dt = models.DateTimeField(db_index=True, auto_now=True)
#     name = models.CharField(max_length=255)
#     user = models.ForeignKey(
#         UserModel, on_delete=models.CASCADE, related_name="printer_profiles"
#     )
#     controller = models.ForeignKey(
#         PrinterController, on_delete=models.CASCADE, related_name="printer_profiles"
#     )
#     device = models.ForeignKey(Device, on_delete=models.CASCADE)


# class OctoprintPrinterProfile(PrinterProfile):
#     _safedelete_policy = SOFT_DELETE

#     printer_controller = models.ForeignKey(
#         PrinterController, on_delete=models.CASCADE, db_index=True
#     )

#     axes_e_inverted = models.BooleanField(null=True)
#     axes_e_speed = models.IntegerField(null=True)

#     axes_x_speed = models.IntegerField(null=True)
#     axes_x_inverted = models.BooleanField(null=True)

#     axes_y_inverted = models.BooleanField(null=True)
#     axes_y_speed = models.IntegerField(null=True)

#     axes_z_inverted = models.BooleanField(null=True)
#     axes_z_speed = models.IntegerField(null=True)

#     extruder_count = models.IntegerField(null=True)
#     extruder_nozzle_diameter = models.FloatField(null=True)
#     extruder_shared_nozzle = models.BooleanField(null=True)

#     heated_bed = models.BooleanField(null=True)
#     heated_chamber = models.BooleanField(null=True)

#     model = models.CharField(max_length=255, null=True, blank=True)

#     volume_custom_box = models.JSONField(default=dict)
#     volume_depth = models.FloatField(null=True)
#     volume_formfactor = models.CharField(null=True, max_length=255)
#     volume_height = models.FloatField(null=True)
#     volume_origin = models.CharField(null=True, max_length=255)
#     volume_width = models.FloatField(null=True)


# TODO
# class RepetierPrinterProfile(PrinterProfile):
#     pass

# TODO
# class MainsailPrinterProfile(PrinterProfile):
#     pass
