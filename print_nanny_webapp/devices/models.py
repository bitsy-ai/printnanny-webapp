import logging
from datetime import datetime
from typing import Callable, Optional, TypedDict
from django.apps import apps
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
    OsEdition,
    SingleBoardComputerType,
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


class PiUrls(TypedDict):
    swupdate: str
    octoprint: str


class Pi(SafeDeleteModel):
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

    sbc = models.CharField(
        max_length=32,
        choices=SingleBoardComputerType.choices,
        default=SingleBoardComputerType.RPI_4,
    )
    edition = models.CharField(
        max_length=32, choices=OsEdition.choices, default=OsEdition.OCTOPRINT_LITE
    )

    created_dt = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, related_name="devices"
    )
    hostname = models.CharField(
        max_length=255,
        help_text="Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension)",
        default="printnanny",
    )

    fqdn = models.CharField(max_length=255, default="printnanny.local")
    favorite = models.BooleanField(default=False)

    @property
    def urls(self) -> PiUrls:
        swupdate = f"http://{self.fqdn}/update/"
        octoprint = f"http://{self.fqdn}{settings.OCTOPRINT_URL}"
        return PiUrls(
            swupdate=swupdate,
            octoprint=octoprint,
        )

    @property
    def octoprint_server(self):
        OctoPrintServer = apps.get_model("octoprint", "OctoPrintServer")
        obj, _ = OctoPrintServer.objects.get_or_create(user=self.user, pi=self)
        return obj

    @property
    def octoprint_settings(self):
        server = self.octoprint_server
        OctoPrintSettings = apps.get_model("octoprint", "OctoPrintSettings")
        obj, _ = OctoPrintSettings.objects.get_or_create(octoprint_server=server)
        return obj

    @property
    def alert_settings(self):
        AlertSettings = apps.get_model("alerts", "AlertSettings")
        obj, _ = AlertSettings.objects.get_or_create(user=self.user)
        return obj

    @property
    def settings(self):
        obj, _ = PiSettings.objects.get_or_create(pi=self)
        return obj

    @property
    def janus_edge(self):
        obj, _ = WebrtcStream.objects.get_or_create(
            pi=self,
            rtp_port=settings.JANUS_EDGE_VIDEO_RTP_PORT,
            config_type=JanusConfigType.EDGE,
        )
        return obj

    @property
    def janus_cloud(self):
        # RTP port is automatically assigned from available open ports
        # admin_secret intentionally set to Null to avoid leaking cloud gateway secret via API responses
        obj, _ = WebrtcStream.objects.get_or_create(
            pi=self, config_type=JanusConfigType.CLOUD
        )
        return obj

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
    def last_boot(self) -> Optional[datetime]:
        if self.system_info is not None:
            return self.system_info.updated_dt
        return None

    @property
    def public_key(self):
        return self.public_keys.first()

    @property
    def cloudiot_name(self):
        return f"pi-id-{self.id}"

    @property
    def cloudiot_device(self):
        return self.cloudiot_devices.first()

    @property
    def cloudiot(self):
        return self.cloudiot_device


class PiSettings(SafeDeleteModel):
    """
    User-facing settings, configurable per device
    """

    class Meta:
        index_together = ("pi", "updated_dt")
        constraints = [
            UniqueConstraint(
                fields=["pi"],
                condition=models.Q(deleted=None),
                name="unique_settings_per_pi",
            )
        ]

    pi = models.ForeignKey(Pi, on_delete=models.CASCADE)
    updated_dt = models.DateTimeField(auto_now=True)
    cloud_video_enabled = models.BooleanField(
        default=True, help_text="Send camera stream to PrintNanny Cloud"
    )
    telemetry_enabled = models.BooleanField(
        default=False,
        help_text="Send telemetry and performance profiling data to PrintNanny Cloud",
    )

    @property
    def user(self):
        return self.pi.user


class PublicKey(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    class Meta:
        index_together = ("pi", "created_dt", "updated_dt")
        constraints = [
            UniqueConstraint(
                fields=["pi"],
                condition=models.Q(deleted=None),
                name="unique_public_key_per_pi",
            )
        ]

    pem = models.TextField()
    cipher = models.CharField(max_length=32)
    length = models.IntegerField()
    fingerprint = models.CharField(max_length=255)
    pi = models.ForeignKey(Pi, on_delete=models.CASCADE, related_name="public_keys")
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    @property
    def user(self):
        return self.pi.user


class SystemInfo(SafeDeleteModel):
    """
    Raspberry Pi device info & metadata
    """

    _safedelete_policy = SOFT_DELETE

    class Meta:
        index_together = (
            ("pi", "created_dt", "updated_dt"),
            ("os_build_id", "os_variant_id", "os_version_id", "pi"),
        )
        constraints = [
            UniqueConstraint(
                fields=["pi"],
                condition=models.Q(deleted=None),
                name="unique_system_info_per_pi",
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
    pi = models.ForeignKey(Pi, on_delete=models.CASCADE, related_name="system_infos")

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
                fields=["pi"],
                condition=models.Q(deleted=None),
                name="unique_cloud_iot_device_per_pi",
            )
        ]
        index_together = [["pi", "public_key", "created_dt", "updated_dt"]]

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

    pi = models.ForeignKey(
        Pi,
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


class WebrtcStream(SafeDeleteModel):
    """
    Configuration model intended for use with Janus Gateway Streaming Plugin API

    2 config_type variations: JanusConfigType.CLOUD JanusConfigType.EDGE


    """

    class Meta:
        index_together = (
            ("pi", "created_dt", "updated_dt"),
            ("pi", "config_type"),
        )

        constraints = [
            UniqueConstraint(
                fields=["pi", "config_type"],
                condition=models.Q(deleted=None),
                name="unique_janus_stream_per_pi",
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
    active = models.BooleanField(default=False)
    pi = models.ForeignKey(Pi, on_delete=models.CASCADE, related_name="janus_streams")
    stream_secret = models.CharField(max_length=255, default=get_random_string_32)
    stream_pin = models.CharField(max_length=255, default=get_random_string_32)

    api_token = models.CharField(max_length=255, default=get_random_string_32)
    admin_secret = models.CharField(
        max_length=255,
        default=get_random_string_32,
        null=True,
        help_text="Janus Gateway Admin API secret. Will be null if config_type=CLOUD",
    )
    rtp_port = models.PositiveSmallIntegerField(default=get_available_rtp_port)

    @property
    def pt(self) -> int:
        return 96

    @property
    def rtpmap(self) -> str:
        return "H264/90000"

    @property
    def admin_port(self) -> int:
        if self.config_type == JanusConfigType.CLOUD:
            return settings.JANUS_CLOUD_ADMIN_PORT
        return settings.JANUS_EDGE_ADMIN_PORT

    @property
    def admin_url(self):
        if self.config_type == JanusConfigType.CLOUD:
            return settings.JANUS_CLOUD_ADMIN_URL
        return f"http://{self.api_domain}:{self.api_port}/admin"

    @property
    def api_port(self) -> int:
        if self.config_type == JanusConfigType.CLOUD:
            return settings.JANUS_CLOUD_API_PORT
        return settings.JANUS_EDGE_API_PORT

    @property
    def api_url(self):
        if self.config_type == JanusConfigType.CLOUD:
            return settings.JANUS_CLOUD_API_URL
        return f"http://{self.api_domain}:{self.api_port}/janus"

    @property
    def api_domain(self) -> str:
        if self.config_type == JanusConfigType.CLOUD:
            return settings.JANUS_CLOUD_DOMAIN
        return self.pi.fqdn

    @property
    def rtp_domain(self) -> str:
        if self.config_type == JanusConfigType.CLOUD:
            return settings.JANUS_CLOUD_RTP_DOMAIN
        return self.pi.fqdn

    @property
    def ws_port(self) -> int:
        if self.config_type == JanusConfigType.CLOUD:
            return settings.JANUS_CLOUD_WS_PORT
        else:
            return settings.JANUS_EDGE_WS_PORT

    @property
    def ws_url(self):
        if self.config_type == JanusConfigType.CLOUD:
            return settings.JANUS_CLOUD_WS_URL
        return f"ws://{self.api_domain}:{self.ws_port}"
