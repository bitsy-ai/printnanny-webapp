import logging
from datetime import datetime
from typing import Optional, TypedDict
from django.apps import apps
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import UniqueConstraint
from django.utils.crypto import get_random_string
from safedelete.models import SafeDeleteModel, SOFT_DELETE, SafeDeleteManager
from print_nanny_webapp.devices.utils import convert_size
from django_nats_nkeys.models import (
    AbstractNatsApp,
    NatsOrganization,
    NatsOrganizationUser,
    NatsOrganizationAppManager,
)
from print_nanny_webapp.devices.utils import (
    get_available_data_rtp_port,
    get_available_video_rtp_port,
)
from print_nanny_webapp.devices.enum import (
    JanusConfigType,
    SingleBoardComputerType,
)
from print_nanny_webapp.octoprint.models import OctoPrintSettings, OctoPrintServer

UserModel = get_user_model()
logger = logging.getLogger(__name__)


def get_random_string_32():
    return get_random_string(32)


class PiUrls(TypedDict):
    octoprint: str
    swupdate: str
    syncthing: str


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
    favorite = models.BooleanField(default=True)
    setup_finished = models.BooleanField(default=False)

    @property
    def urls(self) -> PiUrls:
        swupdate = f"http://{self.fqdn}/update/"
        octoprint = f"http://{self.fqdn}{settings.OCTOPRINT_URL}"
        syncthing = f"http://{self.fqdn}/syncthing/"
        return PiUrls(swupdate=swupdate, octoprint=octoprint, syncthing=syncthing)

    @property
    def octoprint_server(self) -> OctoPrintServer:
        return OctoPrintServer.objects.get_or_create(user=self.user, pi=self)

    @property
    def octoprint_settings(self) -> OctoPrintSettings:
        return OctoPrintSettings.objects.get_or_create(
            octoprint_server=self.octoprint_server
        )

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
    def webrtc_edge(self):
        obj, _ = WebrtcStream.objects.get_or_create(
            pi=self,
            video_rtp_port=settings.JANUS_EDGE_VIDEO_RTP_PORT,
            data_rtp_port=settings.JANUS_EDGE_DATA_RTP_PORT,
            config_type=JanusConfigType.EDGE,
        )
        return obj

    @property
    def webrtc_cloud(self):
        # RTP port is automatically assigned from available open ports
        # admin_secret intentionally set to Null to avoid leaking cloud gateway secret via API responses
        obj, _ = WebrtcStream.objects.get_or_create(
            pi=self, config_type=JanusConfigType.CLOUD
        )
        if obj.video_rtp_port is None:
            obj.video_rtp_port = get_available_video_rtp_port()
            obj.save()
        if obj.data_rtp_port is None:
            obj.data_rtp_port = get_available_data_rtp_port()
            obj.save()
        return obj

    @property
    def nats_app(self):
        return self.nats_apps.first()

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


class PiNatsAppManager(SafeDeleteManager, NatsOrganizationAppManager):
    pass


# add Pi foreign key reference to NatsApp
class PiNatsApp(AbstractNatsApp, SafeDeleteModel):
    objects = PiNatsAppManager()
    pi = models.ForeignKey(Pi, on_delete=models.CASCADE, related_name="nats_apps")
    organization_user = models.ForeignKey(
        NatsOrganizationUser, on_delete=models.CASCADE, related_name="nats_pi_apps"
    )
    organization = models.ForeignKey(
        NatsOrganization,
        on_delete=models.CASCADE,
        related_name="nats_pi_apps",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["app_name", "organization"], name="unique_nats_app_name_per_org"
            ),
            UniqueConstraint(
                fields=["pi"],
                condition=models.Q(deleted=None),
                name="unique_nats_app_per_pi",
            ),
        ]

    @property
    def nats_subject_pattern_template(self) -> str:
        return "pi.{pi_id}.>"

    @property
    def nats_subject_pattern(self) -> str:
        return self.nats_subject_pattern_template.format(pi_id=self.id)

    @property
    def nats_server_uri(self) -> str:
        if settings.DEBUG is False:
            return settings.NATS_SERVER_URI
        # replace nats://nats:4222 with dev machine hostname in debug mode
        dev_hostname = getattr(settings, "DEV_SERVER_HOSTNAME", None)
        if dev_hostname is None:
            logger.warning(
                "settings.DEV_SERVER_HOSTNAME is not set! PrintNanny licenses will contain Docker network hosts instead of LAN hosts. Raspberry Pis will be unable to connect with provided NATS server URI."
            )
            return settings.NATS_SERVER_URI
        return settings.NATS_SERVER_URI.replace("nats:4", f"{dev_hostname}:4")

    @property
    def nats_ws_uri(self) -> str:
        if settings.DEBUG is False:
            return settings.NATS_WS_URI
        # replace nats://nats:4222 with dev machine hostname in debug mode
        dev_hostname = getattr(settings, "DEV_SERVER_HOSTNAME", None)
        if dev_hostname is None:
            logger.warning(
                "settings.DEV_SERVER_HOSTNAME is not set! PrintNanny licenses will contain Docker network hosts instead of LAN hosts. Raspberry Pis will be unable to connect with provided NATS server URI."
            )
            return settings.NATS_WS_URI
        return settings.NATS_WS_URI.replace("nats:", f"{dev_hostname}:")

    def nsc_validate(self):
        from django_nats_nkeys.services import nsc_validate

        return nsc_validate(account_name=self.organization.name)


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

    uptime = models.BigIntegerField(help_text="system uptime (in seconds)")

    rootfs_size = models.BigIntegerField(
        help_text="Size of /dev/root filesystem in bytes"
    )
    rootfs_used = models.BigIntegerField(
        help_text="Space used in /dev/root filesystem in bytes"
    )

    bootfs_size = models.BigIntegerField(
        help_text="Size of /dev/mmcblk0p1 filesystem in bytes"
    )
    bootfs_used = models.BigIntegerField(
        help_text="Space used in /dev/mmcblk0p1 filesystem in bytes"
    )

    datafs_size = models.BigIntegerField(
        help_text="Size of /dev/mmcblk0p4 filesystem in bytes"
    )
    datafs_used = models.BigIntegerField(
        help_text="Space used in /dev/mmcblk0p4 filesystem in bytes"
    )

    # start bootfs
    @property
    def bootfs_used_pretty(self) -> str:
        perc = self.bootfs_used / self.bootfs_size
        return f"{convert_size(self.bootfs_used)} ({perc:.0%} used)"

    @property
    def bootfs_size_pretty(self) -> str:
        return convert_size(self.bootfs_size)

    @property
    def bootfs_available(self) -> int:
        return self.bootfs_size - self.bootfs_used

    @property
    def bootfs_available_pretty(self) -> str:
        perc = self.bootfs_available / self.bootfs_size
        return f"{convert_size(self.bootfs_size_pretty)} ({perc:.0%} free)"

    # end bootfs

    # start datafs

    @property
    def datafs_available(self) -> int:
        return self.datafs_size - self.datafs_used

    @property
    def datafs_available_pretty(self) -> str:
        perc = self.datafs_available / self.datafs_size
        return f"{convert_size(self.datafs_size)} ({perc:.0%} free)"

    @property
    def datafs_size_pretty(self) -> str:
        return convert_size(self.datafs_size)

    @property
    def datafs_used_pretty(self) -> str:
        perc = self.datafs_used / self.datafs_size
        return f"{convert_size(self.datafs_used)} ({perc:.0%} used)"

    # end datafs
    @property
    def rootfs_size_pretty(self) -> str:
        return convert_size(self.rootfs_size)

    @property
    def rootfs_used_pretty(self) -> str:
        perc = self.rootfs_used / self.rootfs_size
        return f"{convert_size(self.rootfs_used)} ({perc:.0%} used)"

    @property
    def rootfs_available(self) -> int:
        return self.rootfs_size - self.rootfs_used

    @property
    def rootfs_available_pretty(self) -> str:
        perc = self.rootfs_available / self.rootfs_size
        return f"{convert_size(self.rootfs_size)} ({perc:.0%} free)"


class WebrtcStream(SafeDeleteModel):
    """
    Configuration model intended for use with Janus Gateway Streaming Plugin API

    2 config_type variations: JanusConfigType.CLOUD JanusConfigType.EDGE


    """

    class Meta:
        index_together = (
            ("pi", "created_dt", "updated_dt"),
            ("pi", "config_type", "video_rtp_port", "data_rtp_port"),
        )

        constraints = [
            UniqueConstraint(
                fields=["pi", "config_type"],
                condition=models.Q(deleted=None),
                name="unique_janus_stream_per_pi",
            ),
            UniqueConstraint(
                fields=["video_rtp_port"],
                condition=models.Q(deleted=None, config_type=JanusConfigType.CLOUD),
                name="unique_video_rtp_port",
            ),
            UniqueConstraint(
                fields=["data_rtp_port"],
                condition=models.Q(deleted=None, config_type=JanusConfigType.CLOUD),
                name="unique_data_rtp_port",
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
    video_rtp_port = models.PositiveSmallIntegerField(null=True)
    data_rtp_port = models.PositiveSmallIntegerField(null=True)

    info = models.JSONField(default=dict)

    def get_or_create_mountpoint(self):
        from print_nanny_webapp.devices.services import (
            janus_streaming_get_or_create_mountpoint,
        )

        return janus_streaming_get_or_create_mountpoint(self)

    def plugin_handle_endpoint(self, session, handle) -> str:
        return f"{self.session_endpoint(session)}/{handle}"

    def session_endpoint(self, session) -> str:
        return f"{self.api_url}/{session}"

    @property
    def is_admin(self) -> bool:
        # api clients should receive janus admin api credentials for edge deployments belonging to authenticated user
        return self.config_type == JanusConfigType.EDGE

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
