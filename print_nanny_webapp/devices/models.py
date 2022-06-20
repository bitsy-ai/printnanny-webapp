import logging
from datetime import datetime
from typing import Callable, Optional
from uuid import uuid4
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import UniqueConstraint
from django.urls import reverse
from django.utils.crypto import get_random_string
from google.cloud import iot_v1 as cloudiot_v1
from safedelete.models import SafeDeleteModel, SOFT_DELETE
from safedelete.signals import pre_softdelete

from .utils import get_available_rtp_port
from .enum import (
    JanusConfigType,
)

UserModel = get_user_model()
logger = logging.getLogger(__name__)


def get_random_string_32():
    return get_random_string(32)


# TODO remove cloudiot_device from registry
def delete_cloudiot_device_from_gcp_registry():
    pass


def pre_softdelete_cloudiot_device(instance=None, **kwargs) -> Callable:
    fn = getattr(instance, "pre_softdelete", delete_cloudiot_device_from_gcp_registry)
    return fn()


pre_softdelete.connect(pre_softdelete_cloudiot_device)


class Device(SafeDeleteModel):
    """
    Raspberry Pi running PrintNanny OS
    """

    _safedelete_policy = SOFT_DELETE

    class Meta:
        index_together = (("hostname", "created_dt"),)
        constraints = [
            UniqueConstraint(
                fields=["user", "hostname"],
                condition=models.Q(deleted=None),
                name="unique_device_hostname_per_user",
            )
        ]

    created_dt = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, related_name="devices"
    )
    hostname = models.CharField(
        max_length=255,
        help_text="Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension)",
        default="printnanny",
    )

    @property
    def system_info(self):
        return self.system_infos.first()

    @property
    def is_active(self) -> bool:
        return self.system_info is not None

    @property
    def is_octoprint(self) -> bool:
        if self.system_info is not None:
            return "octoprint" in self.system_info.os_variant_id
        return False

    @property
    def last_seen(self) -> Optional[datetime]:
        if self.system_info is not None:
            return self.system_info.updated_dt
        return None

    @property
    def public_key(self):
        return self.public_keys.first()

    @property
    def janus_auth(self):
        return self.janus_auths.first()

    @property
    def cloudiot_name(self):
        return f"device-id-{self.id}"

    @property
    def edge_dash_url(self):
        # NOTE: http:// protocol + mDNS hostname is hard-coded here while PrintNanny Network is WIP
        # TODO: f"https://{self.fqdn}{settings.OCTOPRINT_URL}"
        return f"http://{self.hostname}/"

    @property
    def cloud_url(self):
        return reverse("devices:detail", kwargs={"pk": self.id})

    @property
    def octoprint_url(self):
        # NOTE: http:// protocol + mDNS hostname is hard-coded here while PrintNanny Network is WIP
        # TODO: f"https://{self.fqdn}{settings.OCTOPRINT_URL}"
        return f"http://{self.hostname}{settings.OCTOPRINT_URL}"

    @property
    def video_test_url(self):
        return reverse("devices:video", kwargs={"pk": self.id})

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
        index_together = (
            ("device", "created_dt", "updated_dt"),
            ("os_build_id", "os_variant_id", "os_version_id", "device"),
        )
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
    device = models.ForeignKey(
        Device, on_delete=models.CASCADE, related_name="system_infos"
    )

    os_version_id = models.CharField(
        max_length=255,
        help_text="PrintNanny OS VERSION_ID from /etc/os-release",
    )
    os_build_id = models.DateTimeField(
        max_length=255, help_text="PrintNanny OS BUILD_ID from /etc/os-release"
    )

    os_variant_id = models.CharField(
        max_length=255, help_text="PrintNanny OS VARIANT_ID from /etc/os-release"
    )

    os_release_json = models.JSONField(
        default=dict, help_text="Full contents of /etc/os-release in key:value format"
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
            settings.GCP_CLOUDIOT_DEVICE_REGISTRY_REGION,
            settings.GCP_CLOUDIOT_STANDALONE_DEVICE_REGISTRY,
            self.num_id,
        )

    @property
    def gcp_project_id(self):
        return settings.GCP_PROJECT_ID

    @property
    def gcp_region(self):
        return settings.GCP_CLOUDIOT_DEVICE_REGISTRY_REGION

    @property
    def gcp_cloudiot_device_registry(self):
        return settings.GCP_CLOUDIOT_STANDALONE_DEVICE_REGISTRY

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


class JanusAuth(SafeDeleteModel):
    class Meta:
        index_together = ("user", "config_type", "created_dt")
        constraints = [
            UniqueConstraint(
                fields=["user", "config_type"],
                condition=models.Q(deleted=None),
                name="unique_janus_auth_per_config_type_per_user",
            )
        ]

    admin_secret = models.CharField(max_length=255, null=True)
    api_token = models.CharField(max_length=255, default=get_random_string_32)
    config_type = models.CharField(
        max_length=32, choices=JanusConfigType.choices, default=JanusConfigType.CLOUD
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="janus_auth"
    )
    created_dt = models.DateTimeField(auto_now_add=True)


class JanusStream(SafeDeleteModel):
    class Meta:
        index_together = (
            ("device", "created_dt", "updated_dt"),
            ("device", "active", "config_type"),
        )

        constraints = [
            UniqueConstraint(
                fields=["device", "config_type"],
                condition=models.Q(deleted=None),
                name="unique_janus_stream_per_device",
            ),
            UniqueConstraint(
                fields=["rtp_port"],
                condition=models.Q(deleted=None, config_type=JanusConfigType.CLOUD),
                name="unique_port",
            ),
        ]

    created_dt = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_dt = models.DateTimeField(db_index=True, auto_now=True)
    config_type = models.CharField(
        max_length=32, choices=JanusConfigType.choices, default=JanusConfigType.CLOUD
    )
    device = models.ForeignKey(
        Device, on_delete=models.CASCADE, related_name="janus_streams"
    )
    active = models.BooleanField(default=False)
    secret = models.CharField(max_length=255, default=get_random_string_32)
    pin = models.CharField(max_length=255, default=get_random_string_32)
    info = models.JSONField(default=dict)

    api_port = models.IntegerField(default=settings.JANUS_CLOUD_API_PORT)
    admin_port = models.IntegerField(default=settings.JANUS_CLOUD_ADMIN_PORT)
    ws_port = models.IntegerField(default=settings.JANUS_CLOUD_WS_PORT)
    api_domain = models.CharField(max_length=255, default=settings.JANUS_CLOUD_DOMAIN)

    rtp_port = models.PositiveSmallIntegerField(default=get_available_rtp_port)
    rtp_domain = models.CharField(
        max_length=255, default=settings.JANUS_CLOUD_RTP_DOMAIN
    )

    @property
    def auth(self) -> JanusAuth:
        from .services import janus_admin_add_token

        janus_auth, _created = JanusAuth.objects.get_or_create(
            config_type=self.config_type, user=self.device.user
        )
        if self.config_type == JanusConfigType.CLOUD:
            res = janus_admin_add_token(janus_auth, self)
            logger.info("Synced JanusStream.auth %s to %s", res, self.api_domain)
        return janus_auth

    @property
    def api_url(self):
        if self.config_type == JanusConfigType.CLOUD:
            return settings.JANUS_CLOUD_API_URL
        return f"http://{self.api_domain}:{self.api_port}/janus"

    @property
    def admin_url(self):
        if self.config_type == JanusConfigType.CLOUD:
            return settings.JANUS_CLOUD_ADMIN_URL
        return f"http://{self.api_domain}:{self.api_port}/admin"

    @property
    def ws_url(self):
        if self.config_type == JanusConfigType.CLOUD:
            return settings.JANUS_CLOUD_WS_URL
        return f"ws://{self.api_domain}:{self.ws_port}"
