import re
from django.contrib.postgres.fields.jsonb import JSONField
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from google.cloud import iot_v1 as cloudiot_v1
from google.protobuf.json_format import MessageToDict
from django.conf import settings

from polymorphic.models import PolymorphicModel
from safedelete.models import SafeDeleteModel, SOFT_DELETE
from safedelete.managers import SafeDeleteManager
from safedelete.signals import pre_softdelete

from print_nanny_webapp.devices.services import delete_cloudiot_device

UserModel = get_user_model()


def pre_softdelete_cloudiot_device(instance=None, **kwargs):
    fn = getattr(instance, "pre_softdelete", None)
    if hasattr(fn, "__call__"):
        return fn()


pre_softdelete.connect(pre_softdelete_cloudiot_device)


class Device(SafeDeleteModel):
    """
    1-1 relationship with Cloud Iot Device (GCP)
    1-many relationship with PrinterController models
    System-level information
    """

    class Meta:
        unique_together = ("user", "name")

    def pre_softdelete(self):
        return delete_cloudiot_device(self.cloudiot_device_num_id)

    _safedelete_policy = SOFT_DELETE

    created_dt = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_dt = models.DateTimeField(db_index=True, auto_now=True)
    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, related_name="devices"
    )
    name = models.CharField(max_length=255)
    # PKI
    public_key = models.TextField()
    fingerprint = models.CharField(max_length=255)

    # GCP cloudiot API params
    cloudiot_device = JSONField()
    cloudiot_device_name = models.CharField(max_length=255)
    cloudiot_device_path = models.CharField(max_length=255)
    cloudiot_device_num_id = models.BigIntegerField()

    # platform info
    os_version = models.CharField(max_length=255)
    os = models.CharField(max_length=255)
    kernel_version = models.CharField(max_length=255)

    # hardware info
    # /proc/cpuinfo HARDWARE
    hardware = models.CharField(max_length=255)
    # /proc/cpuinfo REVISION
    revision = models.CharField(max_length=255)
    # /proc/cpuinfo MODEL
    model = models.CharField(max_length=255)
    # /proc/cpuinfo SERIAL
    serial = models.CharField(max_length=255)
    # /proc/cpuinfo MAX PROCESSOR
    cores = models.IntegerField()
    ram = models.BigIntegerField()
    cpu_flags = models.CharField(max_length=255)

    # TODO enable front-end views in release v0.8 go-live
    # @property
    # def manage_url(self):
    #     reverse("dashboard:devices:detail", kwargs={"pk": self.id})

    @property
    def cloudiot_device_configs(self):
        """pa
        Lists the last 10 device configurations
        """
        client = cloudiot_v1.DeviceManagerClient()
        device_path = client.device_path(
            settings.GCP_PROJECT_ID,
            settings.GCP_CLOUD_IOT_DEVICE_REGISTRY_REGION,
            settings.GCP_CLOUD_IOT_DEVICE_REGISTRY,
            self.cloudiot_device_name,
        )
        device_configs = client.list_device_config_versions(name=device_path)
        configs_dict = MessageToDict(device_configs._pb)
        return configs_dict


class PrinterController(PolymorphicModel, SafeDeleteModel):

    _safedelete_policy = SOFT_DELETE

    created_dt = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_dt = models.DateTimeField(db_index=True, auto_now=True)
    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, related_name="printer_controllers"
    )
    device = models.ForeignKey(
        Device, on_delete=models.CASCADE, related_name="printer_controllers"
    )
    cli_version = models.CharField(max_length=255)


class OctoprintController(PrinterController):

    python_version = models.CharField(max_length=255)
    pip_version = models.CharField(max_length=255)
    virtualenv = models.CharField(max_length=255, null=True)
    octoprint_version = models.CharField(max_length=255)
    plugin_version = models.CharField(max_length=255)


# TODO
# class RepetierController(PrinterController):
#     pass

# TODO
# class MainsailController(PrinterController):
#     pass


class PrinterProfile(PolymorphicModel, SafeDeleteModel):
    class Meta:
        unique_together = (
            "user",
            "name",
        )

    _safedelete_policy = SOFT_DELETE
    created_dt = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_dt = models.DateTimeField(db_index=True, auto_now=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, related_name="printer_profiles"
    )
    controller = models.ForeignKey(
        PrinterController, on_delete=models.CASCADE, related_name="printer_profiles"
    )
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    local_webcam = models.CharField(max_length=255)


class OctoprintPrinterProfile(PrinterProfile):
    _safedelete_policy = SOFT_DELETE

    octoprint_controller = models.ForeignKey(
        OctoprintController, on_delete=models.CASCADE, db_index=True
    )

    axes_e_inverted = models.BooleanField(null=True)
    axes_e_speed = models.IntegerField(null=True)

    axes_x_speed = models.IntegerField(null=True)
    axes_x_inverted = models.BooleanField(null=True)

    axes_y_inverted = models.BooleanField(null=True)
    axes_y_speed = models.IntegerField(null=True)

    axes_z_inverted = models.BooleanField(null=True)
    axes_z_speed = models.IntegerField(null=True)

    extruder_count = models.IntegerField(null=True)
    extruder_nozzle_diameter = models.FloatField(null=True)
    extruder_shared_nozzle = models.BooleanField(null=True)

    heated_bed = models.BooleanField(null=True)
    heated_chamber = models.BooleanField(null=True)

    model = models.CharField(max_length=255, null=True, blank=True)

    volume_custom_box = JSONField(default={})
    volume_depth = models.FloatField(null=True)
    volume_formfactor = models.CharField(null=True, max_length=255)
    volume_height = models.FloatField(null=True)
    volume_origin = models.CharField(null=True, max_length=255)
    volume_width = models.FloatField(null=True)


# TODO
# class RepetierPrinterProfile(PrinterProfile):
#     pass

# TODO
# class MainsailPrinterProfile(PrinterProfile):
#     pass
