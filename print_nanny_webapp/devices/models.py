import logging
from typing import Callable
from urllib.parse import urlencode
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import UniqueConstraint
from django.urls import reverse
from django.utils.crypto import get_random_string
from google.cloud import iot_v1 as cloudiot_v1
from polymorphic.models import PolymorphicModel
from safedelete.models import SafeDeleteModel, SOFT_DELETE
from safedelete.signals import pre_softdelete

from .enum import (
    CameraType,
    DeviceReleaseChannel,
    JanusConfigType,
    PrinterSoftwareType,
)

UserModel = get_user_model()
logger = logging.getLogger(__name__)


def get_random_string_32():
    return get_random_string(32)


def noop():
    pass


def pre_softdelete_cloudiot_device(instance=None, **kwargs) -> Callable:
    fn = getattr(instance, "pre_softdelete", noop)
    return fn()


pre_softdelete.connect(pre_softdelete_cloudiot_device)


class Device(SafeDeleteModel):
    """ """

    _safedelete_policy = SOFT_DELETE

    class Meta:
        index_together = (("hostname", "created_dt", "updated_dt"),)
        constraints = [
            UniqueConstraint(
                fields=["user", "hostname"],
                condition=models.Q(deleted=None),
                name="unique_device_hostname_per_user",
            )
        ]

    monitoring_active = models.BooleanField(default=False)
    setup_complete = models.BooleanField(default=False)
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
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

    @property
    def public_key(self):
        return self.public_keys.first()

    @property
    def janus_auth(self):
        return self.janus_auths.first()

    @property
    def last_task(self):
        return self.tasks.first()

    # @property
    # def active_tasks(self):
    #     return self.tasks.filter(active=True).all()

    # @property
    # def active_cameras(self):
    #     return self.cameras.filter(active=True).all()

    @property
    def cloudiot_name(self):
        return f"device-id-{self.id}"

    @property
    def dashboard_url(self):
        return reverse("devices:detail", kwargs={"pk": self.id})

    @property
    def video_test_url(self):
        base_url = reverse("devices:welcome-detail", kwargs={"pk": self.id})
        query = urlencode(dict(step=2))
        return f"{base_url}?{query}"

    @property
    def cloudiot_device(self):
        return self.cloudiot_devices.first()

    @property
    def cloudiot(self):
        return self.cloudiot_device

    @property
    def html_id(self) -> str:
        return f"device-{self.id}"

    @property
    def janus_local_url(self):
        return f"http://{self.hostname}:8088/janus"


class AnsibleFactsd(models.Model):

    namespace = models.CharField(max_length=64, default="printnanny")
    created_dt = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_dt = models.DateTimeField(db_index=True, auto_now=True)


class PublicKey(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    class Meta:
        index_together = ("device", "created_dt", "updated_dt")
        constraints = [
            UniqueConstraint(
                fields=["device"],
                condition=models.Q(deleted=None),
                name="unique_public_key_per_device",
            )
        ]

    pem = models.TextField()
    cipher = models.CharField(max_length=32)
    length = models.IntegerField()
    fingerprint = models.CharField(max_length=255)
    device = models.ForeignKey(
        Device, on_delete=models.CASCADE, related_name="public_keys"
    )
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    @property
    def user(self):
        return self.device.user


class SystemInfo(SafeDeleteModel):
    """
    Immutable device info & metadata
    """

    _safedelete_policy = SOFT_DELETE

    class Meta:
        index_together = ("device", "created_dt", "updated_dt")
        constraints = [
            UniqueConstraint(
                fields=["device"],
                condition=models.Q(deleted=None),
                name="unique_device_info_per_device",
            )
        ]

    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

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
                fields=["device", "public_key"],
                condition=models.Q(deleted=None),
                name="unique_cloud_iot_device_per_device",
            )
        ]
        index_together = [["device", "public_key", "created_dt", "updated_dt"]]

    def pre_softdelete(self):
        from print_nanny_webapp.devices.services import (
            delete_cloudiot_device,
        )

        return delete_cloudiot_device(self.num_id)

    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
    num_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    id = models.CharField(max_length=255)

    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,
        related_name="cloudiot_devices",
    )

    public_key = models.ForeignKey(
        PublicKey, on_delete=models.CASCADE, related_name="cloudiot_devices"
    )

    @property
    def client(self):
        return cloudiot_v1.DeviceManagerClient()

    @property
    def gcp_resource(self):
        return self.client.device_path(
            settings.GCP_PROJECT_ID,
            settings.GCP_CLOUD_IOT_DEVICE_REGISTRY_REGION,
            settings.GCP_CLOUD_IOT_STANDALONE_DEVICE_REGISTRY,
            self.num_id,
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
    def command_topic(self):
        """
        Messages sent to device (wildcard topic pattern)
        """
        return f"/devices/{self.num_id}/commands/#"

    @property
    def event_topic(self):
        """
        Topic containing device-published messages
        Additional subfolders may be specified
        For example /devices/:id/events/alerts
        """
        return f"/devices/{self.num_id}/events"

    @property
    def config_topic(self):
        """
        Reference: https://cloud.google.com/iot/docs/how-tos/config/configuring-devices
        With Cloud IoT Core, you can control a device by sending it a device configuration.
        A device configuration is an arbitrary user-defined blob of data sent from Cloud IoT Core to a device.
        The data can be structured or unstructured. It can also be of any format, such as arbitrary binary data, text, JSON, or serialized protocol buffers.

        Device configuration is persisted in storage by Cloud IoT Core.
        The maximum size for configuration data is 64 KB. For additional limits, see Quotas and Limits.
        https://cloud.google.com/iot/quotas

        For best results, a device configuration should focus on desired values or results, rather than on a sequence of commands.
        If you specify commands, intermediate configuration versions may create conflicts,
        and it won't be possible to restore the state of a device (without executing every sequence of commands since the device was first initialized).
        If your configurations emphasize values and results, you'll be able to more easily restore the device state.
        """
        return f"/devices/{self.num_id}/config"

    @property
    def state_topic(self):
        """
        https://cloud.google.com/iot/docs/concepts/devices#device_state
        Device state information captures the current status of the device, not the environment.
        Devices can describe their state with an arbitrary user-defined blob of data sent from the device to the cloud.
        The data can be structured or unstructured. It can also be of any format, such as binary data, text, JSON, or serialized protocol buffers.
        Some examples of device state include the health of the device or its firmware version.
        Typically, device state information is not updated frequently.
        """
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


class JanusEdgeAuth(SafeDeleteModel):
    class Meta:
        index_together = ("device", "created_dt", "updated_dt")
        constraints = [
            UniqueConstraint(
                fields=["device"],
                condition=models.Q(deleted=None),
                name="unique_janus_edge_auth_per_device",
            )
        ]

    api_token = models.CharField(max_length=255, default=get_random_string_32)
    admin_secret = models.CharField(max_length=255)
    device = models.ForeignKey(
        Device, on_delete=models.CASCADE, related_name="janus_edge_auth"
    )
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    @property
    def user(self):
        return self.device.user

    @property
    def gateway_url(self):
        return f"http://{self.device.hostname}/janus"

    @property
    def gateway_admin_url(self):
        return f"http://{self.device.hostname}/admin"

    @property
    def websocket_url(self):
        return f"ws://{self.device.hostname}"


class JanusCloudAuth(SafeDeleteModel):
    api_token = models.CharField(max_length=255, default=get_random_string_32)
    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="janus_cloud_auth"
    )
    created_dt = models.DateTimeField(auto_now_add=True)

    @property
    def gateway_url(self):
        return f"https://{settings.JANUS_CLOUD_DOMAIN}/janus"

    @property
    def gateway_admin_url(self):
        return f"https://{settings.JANUS_CLOUD_DOMAIN}/admin"

    @property
    def websocket_url(self):
        return f"wss://{settings.JANUS_CLOUD_DOMAIN}"


class JanusStreamConfig(SafeDeleteModel):
    class Meta:
        index_together = ("device", "active", "created_dt", "updated_dt")
        constraints = [
            UniqueConstraint(
                fields=["device"],
                condition=models.Q(deleted=None),
                name="unique_janus_cloud_stream_per_device",
            )
        ]

    config_type = models.CharField(
        max_length=32, choices=JanusConfigType.choices, default=JanusConfigType.CLOUD
    )
    device = models.ForeignKey(
        Device, on_delete=models.CASCADE, related_name="janus_media_streams"
    )
    active = models.BooleanField(default=False)
    secret = models.CharField(max_length=255, default=get_random_string_32)
    pin = models.CharField(max_length=255, default=get_random_string_32)
    # streaming.info response documented in https://janus.conf.meetecho.com/docs/streaming"
    info = models.JSONField(default=dict)

    @property
    def janus_api_token(self):
        return self.device.user.janus_cloud_auth

    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)


class Camera(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    class Meta:
        unique_together = ("device", "name")

    _safedelete_policy = SOFT_DELETE

    created_dt = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_dt = models.DateTimeField(db_index=True, auto_now=True)
    active = models.BooleanField(default=False)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name="cameras")
    name = models.CharField(
        max_length=255,
        default="Raspberry Pi Cam",
        help_text="Descriptive name to identify this camera",
    )
    camera_type = models.CharField(
        max_length=255,
        choices=CameraType.choices,
        default=CameraType.choices,
        help_text="Specify camera connection type",
    )


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
