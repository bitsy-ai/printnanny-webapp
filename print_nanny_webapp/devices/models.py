import logging
from typing import Any
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import UniqueConstraint
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from polymorphic.models import PolymorphicModel
from safedelete.models import SafeDeleteModel, SafeDeleteManager, SOFT_DELETE
from safedelete.signals import pre_softdelete

from .choices import (
    SystemTaskType,
    DeviceReleaseChannel,
    PrinterSoftwareType,
    SystemTaskStatus,
)

UserModel = get_user_model()
logger = logging.getLogger(__name__)


def pre_softdelete_cloudiot_device(instance=None, **kwargs):
    fn = getattr(instance, "pre_softdelete", None)
    if hasattr(fn, "__call__"):
        return fn()


pre_softdelete.connect(pre_softdelete_cloudiot_device)


def _get_default_stable_release() -> int:
    from print_nanny_webapp.releases.models import Release

    release = Release.objects.filter(release_channel="stable").first()
    if release:
        return release.id
    else:
        raise Exception("No release found")


class Device(SafeDeleteModel):
    """ """

    _safedelete_policy = SOFT_DELETE

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["user", "hostname"],
                condition=models.Q(deleted=None),
                name="unique_device_hostname_per_user",
            )
        ]

    created_dt = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_dt = models.DateTimeField(db_index=True, auto_now=True)
    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, related_name="devices"
    )
    hostname = models.CharField(
        max_length=255,
        help_text="Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension)",
        default="printnanny",
    )
    release_channel = models.CharField(
        max_length=8,
        choices=DeviceReleaseChannel.choices,
        default=DeviceReleaseChannel.STABLE,
        help_text="WARNING: you should only use the nightly developer channel when guided by Print Nanny staff! This unstable channel is intended for QA and verifying bug fixes.",
    )
    bootstrap_release = models.ForeignKey(
        "releases.Release",
        db_index=True,
        on_delete=models.CASCADE,
        default=_get_default_stable_release,
    )

    @property
    def active_license(self):
        return self.licenses.first()

    @property
    def last_system_task(self):
        return self.system_tasks.first()

    @property
    def to_cloudiot_id(self):
        return f"device-id-{self.id}"

    @property
    def dashboard_url(self):
        return reverse("devices:detail", kwargs={"pk": self.id})

    @property
    def cloudiot_device(self):
        return self.cloudiot_devices.first()


# method for updating
@receiver(post_save, sender=Device, dispatch_uid="create_device")
def create_verify_license_device_action(sender, instance, created, **kwargs):
    if created:
        action = SystemTask.objects.create(
            status=SystemTaskStatus.WAITING,
            type=SystemTaskType.VERIFY_LICENSE,
            device=instance,
        )
        logger.info(f"Created {instance} and VERIFY_LICENSE action {action}")


class License(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["device"],
                condition=models.Q(deleted=None),
                name="unique_license_per_device",
            )
        ]

    public_key = models.TextField()
    public_key_checksum = models.CharField(max_length=255)
    fingerprint = models.CharField(max_length=255)

    created_dt = models.DateTimeField(db_index=True, auto_now_add=True)
    device = models.ForeignKey(
        Device, on_delete=models.CASCADE, related_name="licenses"
    )


class DeviceInfo(SafeDeleteModel):
    """
    Immutable device info & metadata
    """

    _safedelete_policy = SOFT_DELETE

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["device"],
                condition=models.Q(deleted=None),
                name="unique_device_info_per_device",
            )
        ]

    machine_id = models.CharField(
        max_length=255, help_text="Populated from /etc/machine-id"
    )
    # /proc/cpuinfo HARDWARE
    hardware = models.CharField(
        max_length=255, help_text="Populated from /proc/cpuinfo HARDWARE"
    )
    # /proc/cpuinfo REVISION
    revision = models.CharField(
        max_length=255, help_text="Populated from /proc/cpuinfo REVISION"
    )
    # /proc/cpuinfo MODEL
    model = models.CharField(
        max_length=255, help_text="Populated from /proc/cpuinfo MODEL"
    )
    # /proc/cpuinfo SERIAL
    serial = models.CharField(
        max_length=255, help_text="Populated from /proc/cpuinfo SERIAL"
    )
    # /proc/cpuinfo MAX PROCESSOR
    cores = models.IntegerField()
    ram = models.BigIntegerField()
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    image_version = models.CharField(
        max_length=255,
        help_text="Print Nanny OS version string from /boot/image_version.txt",
    )


class CloudiotDevice(SafeDeleteModel):
    """
    Instance of cloudiot.projects.locations.registries.devices#Device
    https://cloud.google.com/iot/docs/reference/cloudiot/rest/v1/projects.locations.registries.devices#Device
    """  # Create your models here.

    _safedelete_policy = SOFT_DELETE

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["device"],
                condition=models.Q(deleted=None),
                name="unique_cloud_iot_device_per_device",
            )
        ]

    def pre_softdelete(self):
        from print_nanny_webapp.devices.services import (
            delete_cloudiot_device,
        )

        return delete_cloudiot_device(self.num_id)

    num_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    id = models.CharField(max_length=255)

    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,
        related_name="cloudiot_devices",
        db_index=True,
    )

    @property
    def gcp_project_id(self):
        return settings.GCP_PROJECT_ID

    @property
    def gcp_region(self):
        return settings.GCP_CLOUD_IOT_DEVICE_REGISTRY_REGION

    @property
    def gcp_cloudiot_device_registry(self):
        return settings.GCP_CLOUD_IOT_STANDALONE_DEVICE_REGISTRY

    @property
    def mqtt_bridge_hostname(self):
        return settings.GCP_MQTT_BRIDGE_HOSTNAME

    @property
    def mqtt_bridge_port(self):
        return settings.GCP_MQTT_BRIDGE_PORT

    @property
    def mqtt_client_id(self):
        return self.name

    @property
    def desired_config_topic(self):
        return f"/devices/{self.num_id}/config"

    @property
    def current_state_topic(self):
        return f"/devices/{self.num_id}/state"


class DeviceConfig(SafeDeleteModel):
    """
    Append-only log of msgs published to /devices/:id/config FROM webapp controller
    Indicates desired configuration of device

    Fields rendered to extra vars file used with Ansible Playbook
    ansible-playbook playbook.yml --extra-vars "@some_file.json"

    Device will attempt to apply the received config
    Then publish state to /devices/:id/state FROM device
    https://cloud.google.com/iot/docs/concepts/devices#changing_device_behavior_or_state_using_configuration_data
    """

    _safedelete_policy = SOFT_DELETE

    class Meta:
        ordering = ["-created_dt"]

    device = models.ForeignKey(Device, on_delete=models.CASCADE, db_index=True)
    ansible_extra_vars = models.JSONField(default=dict())
    release_channel = models.CharField(
        max_length=8,
        choices=DeviceReleaseChannel.choices,
        default=DeviceReleaseChannel.STABLE,
    )
    created_dt = models.DateTimeField(db_index=True, auto_now_add=True)

    @property
    def mqtt_topic(self):
        return f"/devices/{self.num_id}/config"

    @property
    def user(self):
        return self.device.user

    @property
    def cloudiot_device(self):
        return self.device.cloudiot_device


class SystemTask(SafeDeleteModel):
    """
    Append-only log published to /devices/:id/state FROM device
    Indicates current state of device

    See: desired state design pattern for details
    https://cloud.google.com/iot/docs/concepts/devices#changing_device_behavior_or_state_using_configuration_data
    """

    class Meta:
        ordering = ["-created_dt"]
        index_together = [["device", "type", "status"]]

    _safedelete_policy = SOFT_DELETE
    status = models.CharField(
        max_length=16,
        choices=SystemTaskStatus.choices,
        default=SystemTaskStatus.WAITING,
    )
    type = models.CharField(
        max_length=255,
        choices=SystemTaskType.choices,
        default=SystemTaskType.SOFTWARE_UPDATE,
    )

    device = models.ForeignKey(
        Device, on_delete=models.CASCADE, db_index=True, related_name="system_tasks"
    )
    detail = models.CharField(max_length=1024, null=True)
    ansible_facts = models.JSONField(default=dict())
    created_dt = models.DateTimeField(db_index=True, auto_now_add=True)

    @property
    def status_css_class(self):
        return SystemTaskStatus.get_css_class(self.status)


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
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name="cameras")
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
    device = models.ForeignKey(
        Device, on_delete=models.CASCADE, related_name="printer_controllers"
    )
    software = models.CharField(
        max_length=12,
        choices=PrinterSoftwareType.choices,
        default=PrinterSoftwareType.OCTOPRINT,
    )
