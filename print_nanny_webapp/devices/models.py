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

from .choices import ApplianceReleaseChannel, PrinterSoftware

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
        Appliance, on_delete=models.CASCADE, related_name="cloudiot_device"
    )


class AppliancePKI(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    public_key = models.TextField()
    public_key_checksum = models.CharField(max_length=255)
    private_key_checksum = models.CharField(max_length=255)
    fingerprint = models.CharField(max_length=255)
    appliance = models.OneToOneField(
        Appliance, on_delete=models.CASCADE, related_name="pki"
    )


class ApplianceAnsibleFacts(SafeDeleteModel):
    appliance = models.OneToOneField(
        Appliance, on_delete=models.CASCADE, related_name="ansible_facts"
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

    release_channel = models.TextField(
        max_length=8, choices=ApplianceReleaseChannel.choices
    )
    json = models.JSONField()


class DeviceManager(SafeDeleteManager):
    def update_or_create(self, defaults=None, **kwargs):
        name = kwargs.get("name")
        logger.info(f"Creating keypair for device serial={name}")

        keypair = generate_keypair()

        name = kwargs["name"]
        user_id = kwargs["user"].id
        serial = kwargs.get("serial", "Raspberry Pi Hardware not detected")
        cloudiot_device_name = f"{name}-{user_id}"
        cloudiot_device_dict, device_path = update_or_create_cloudiot_device(
            name=cloudiot_device_name,
            serial=serial,
            user_id=user_id,
            metadata=kwargs,
            fingerprint=keypair["fingerprint"],
            public_key_content=keypair["public_key_content"].strip(),
        )

        logger.info(f"iot create_device() succeeded {cloudiot_device_dict}")

        cloudiot_device_num_id = cloudiot_device_dict.get("numId")

        always_update = dict(
            public_key=keypair["public_key_content"],
            fingerprint=keypair["fingerprint"],
            cloudiot_device_num_id=cloudiot_device_num_id,
            cloudiot_device_name=cloudiot_device_name,
            cloudiot_device_path=device_path,
        )

        defaults.update(always_update)

        device, created = super().update_or_create(defaults=defaults, **kwargs)

        for key, value in always_update.items():
            setattr(device, key, value)
        logging.info(f"Device created: {created} with id={device.id}")
        device.private_key = keypair["private_key_content"]
        device.private_key_checksum = keypair["private_key_checksum"]
        device.public_key_checksum = keypair["public_key_checksum"]
        device.ca_certs = keypair["ca_certs"]
        device.save()

        from print_nanny_webapp.ml_ops.models import (
            Experiment,
            ExperimentDeviceConfig,
        )

        active_experiment = Experiment.objects.filter(active=True).first()
        if active_experiment is not None:
            experiment_device_config = ExperimentDeviceConfig.objects.create(
                octoprint_device=device,
                experiment=active_experiment,
            )

        return device, created


class Device(SafeDeleteModel):
    """
    1-1 relationship with Cloud Iot Device (GCP)
    1-many relationship with PrinterController models
    System-level information
    """

    objects = DeviceManager()

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
    cloudiot_device_name = models.CharField(max_length=255)
    cloudiot_device_path = models.CharField(max_length=255)
    cloudiot_device_num_id = models.BigIntegerField()

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


class CameraController(SafeDeleteModel):
    class Meta:
        unique_together = ("user", "name")

    class CameraType(models.TextChoices):
        RPI_CAMERA = "Raspberry Pi Camera Module", "Raspberry Pi Camera Module"
        USB_CAMERA = (
            "Raspberry Pi USB Camera",
            "Raspberry Pi USB Camera",
        )
        IP_CAMERA = "Generic RTSP/RTMP IP Camera", "Generic RTSP/RTMP IP Camera"

    class CameraSourceType(models.TextChoices):
        MJPG_STREAMER = "MJPG Streamer", "Software-encoded JPG frames over HTTP"
        GSTREAMER = "Gstreamer", "Hardware-encoded h264"

    _safedelete_policy = SOFT_DELETE

    created_dt = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_dt = models.DateTimeField(db_index=True, auto_now=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    camera_type = models.CharField(max_length=255, choices=CameraType.choices)
    camera_source = models.CharField(max_length=255)
    camera_source_type = models.CharField(
        max_length=255, choices=CameraSourceType.choices
    )


# class PrinterController(PolymorphicModel, SafeDeleteModel):

#     _safedelete_policy = SOFT_DELETE

#     created_dt = models.DateTimeField(db_index=True, auto_now_add=True)
#     updated_dt = models.DateTimeField(db_index=True, auto_now=True)
#     user = models.ForeignKey(
#         UserModel, on_delete=models.CASCADE, related_name="printer_controllers"
#     )
#     appliance = models.ForeignKey(
#         Device, on_delete=models.CASCADE, related_name="printer_controllers"
#     )
#     software = models.CharField(max_length=12, choices=PrinterSoftware.choices)


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
