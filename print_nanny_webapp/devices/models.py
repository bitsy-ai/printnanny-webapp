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
    NatsOrganizationAppManager,
    AbstractNatsOrganizationApp,
)
from print_nanny_webapp.devices.utils import (
    get_available_data_rtp_port,
    get_available_video_rtp_port,
)
from print_nanny_webapp.devices.enum import (
    JanusConfigType,
    SingleBoardComputerType,
    PreferredDnsType,
)
from print_nanny_webapp.octoprint.models import OctoPrintSettings, OctoPrintServer

UserModel = get_user_model()
logger = logging.getLogger(__name__)


def get_random_string_32():
    return get_random_string(32)


class PiUrls(TypedDict):
    moonraker_api: str
    mission_control: str
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
    favorite = models.BooleanField(default=True)
    setup_finished = models.BooleanField(default=False)

    @property
    def mdns_hostname(self):
        return f"{self.hostname}.local"

    @property
    def mdns_urls(self) -> PiUrls:
        moonraker_api = f"http://{self.mdns_hostname}/mainsail/api/"  # moonraker api is served by nginx @ /mainsail/api/ because mainsail doesn't allow us to configure a base url for moonraker services
        mission_control = f"http://{self.mdns_hostname}/"
        swupdate = f"http://{self.mdns_hostname}/update/"
        octoprint = f"http://{self.mdns_hostname}{settings.OCTOPRINT_URL}"
        syncthing = f"http://{self.mdns_hostname}/syncthing/"
        return PiUrls(
            swupdate=swupdate,
            octoprint=octoprint,
            syncthing=syncthing,
            mission_control=mission_control,
            moonraker_api=moonraker_api,
        )

    @property
    def shortname_urls(self) -> PiUrls:
        moonraker_api = f"http://{self.hostname}/mainsail/api/"  # moonraker api is served by nginx @ /mainsail/api/ because mainsail doesn't allow us to configure a base url for moonraker services
        mission_control = f"http://{self.hostname}/"
        swupdate = f"http://{self.hostname}/update/"
        octoprint = f"http://{self.hostname}{settings.OCTOPRINT_URL}"
        syncthing = f"http://{self.hostname}/syncthing/"
        return PiUrls(
            swupdate=swupdate,
            octoprint=octoprint,
            syncthing=syncthing,
            mission_control=mission_control,
            moonraker_api=moonraker_api,
        )

    @property
    def urls(self) -> PiUrls:
        if self.network_settings.preferred_dns == PreferredDnsType.MULTICAST:
            return self.mdns_urls
        elif self.network_settings.preferred_dns == PreferredDnsType.TAILSCALE:
            return self.shortname_urls
        else:
            raise ValueError(
                f"Pi.urls gettr is not implemented for {self.network_settings.preferred_dns}"
            )

    @property
    def octoprint_server(self) -> OctoPrintServer:
        obj, _ = OctoPrintServer.objects.get_or_create(user=self.user, pi=self)
        return obj

    @property
    def octoprint_settings(self) -> OctoPrintSettings:
        obj, _ = OctoPrintSettings.objects.get_or_create(
            octoprint_server=self.octoprint_server
        )
        return obj

    @property
    def alert_settings(self):
        AlertSettings = apps.get_model("alerts", "AlertSettings")
        obj, _ = AlertSettings.objects.get_or_create(user=self.user)
        return obj

    @property
    def network_settings(self):
        obj, _ = NetworkSettings.objects.get_or_create(user=self.user)
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
        result = self.nats_apps.first()
        # if no active nats app is associated with this Pi, create one
        if result is None:
            result = PiNatsApp.objects.create_nsc(pi=self)
        return result

    @property
    def system_info(self):
        return self.system_infos.first()

    @property
    def is_active(self) -> bool:
        return self.system_info is not None

    @property
    def last_boot(self) -> Optional[datetime]:
        if self.system_info is not None:
            return self.system_info.updated_dt
        return None

    @property
    def cloudiot_name(self):
        return f"pi-id-{self.id}"

    def latest_camera_snapshot(self):
        return self.camera_snapshots.first()


class PiNatsAppManager(SafeDeleteManager, NatsOrganizationAppManager):
    def create(self, **kwargs):
        from django_nats_nkeys.services import (
            get_or_create_org_owner_units_for_authenticated_user,
        )

        pi = kwargs.get("pi")
        if pi is None:
            raise ValueError("PiNatsApp.pi is required, but received None value")

        # is there already an org/org user associated with Pi owner?
        _created, (
            org,
            _org_owner,
            org_user,
        ) = get_or_create_org_owner_units_for_authenticated_user(pi.user)

        organization = kwargs.pop("organization", None)
        if organization is None:
            organization = org
        organization_user = kwargs.pop("organization_user", None)
        if organization_user is None:
            organization_user = org_user
        return super().create(
            organization=organization, organization_user=organization_user, **kwargs
        )


# add Pi foreign key reference to NatsApp
class PiNatsApp(AbstractNatsOrganizationApp, SafeDeleteModel):
    objects = PiNatsAppManager()
    pi = models.ForeignKey(Pi, on_delete=models.CASCADE, related_name="nats_apps")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["app_name"], name="unique_nats_app_name"),
            UniqueConstraint(
                fields=["pi"],
                condition=models.Q(deleted=None),
                name="unique_nats_app_per_pi",
            ),
        ]

    @property
    def mqtt_subject_template_moonraker_request(self) -> str:
        return "{app_name}/moonraker/api/request"

    @property
    def mqtt_subject_moonraker_request(self) -> str:
        return self.mqtt_subject_template_moonraker_request.format(
            app_name=self.app_name
        )

    @property
    def mqtt_subject_template_moonraker_response(self) -> str:
        return "{app_name}/moonraker/api/response"

    @property
    def mqtt_subject_moonraker_response(self) -> str:
        return self.mqtt_subject_template_moonraker_response.format(
            app_name=self.app_name
        )

    @property
    def mqtt_subject_template_klipper_status(self) -> str:
        return "{app_name}/klipper/status"

    @property
    def mqtt_subject_klipper_status(self) -> str:
        return self.mqtt_subject_template_klipper_status.format(app_name=self.app_name)

    @property
    def mqtt_broker_host(self) -> str:
        return settings.NATS_MQTT_BROKER_HOST

    @property
    def mqtt_broker_port(self) -> int:
        return settings.NATS_MQTT_BROKER_PORT

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


class NetworkSettings(SafeDeleteModel):
    """
    User-facing settings, configurable per account
    """

    class Meta:
        index_together = ("user", "updated_dt")
        constraints = [
            UniqueConstraint(
                fields=["user"],
                condition=models.Q(deleted=None),
                name="unique_pi_settings_per_user",
            )
        ]

    updated_dt = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    preferred_dns = models.CharField(
        max_length=32,
        choices=PreferredDnsType.choices,
        default=PreferredDnsType.MULTICAST,
    )


class SystemInfo(SafeDeleteModel):
    """
    Raspberry Pi device info & metadata
    """

    _safedelete_policy = SOFT_DELETE

    class Meta:
        index_together = (
            ("pi", "created_dt", "updated_dt"),
            ("os_build_id", "os_version_id", "pi"),
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
        blank=True,
        max_length=255,
        help_text="PrintNanny OS VERSION_ID from /etc/os-release",
    )
    os_build_id = models.CharField(
        blank=True,
        max_length=255,
        help_text="PrintNanny OS BUILD_ID from /etc/os-release",
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
        if self.bootfs_size > 0:
            perc = self.bootfs_used / self.bootfs_size
            return f"{convert_size(self.bootfs_used)} ({perc:.0%} used)"
        return "Unknown"

    @property
    def bootfs_size_pretty(self) -> str:
        if self.bootfs_size > 0:
            return convert_size(self.bootfs_size)
        return "Unknown"

    @property
    def bootfs_available(self) -> int:
        return self.bootfs_size - self.bootfs_used

    @property
    def bootfs_available_pretty(self) -> str:
        if self.bootfs_size > 0:
            perc = self.bootfs_available / self.bootfs_size
            return f"{convert_size(self.bootfs_size_pretty)} ({perc:.0%} free)"
        return "Unknown"

    # end bootfs

    # start datafs

    @property
    def datafs_available(self) -> int:
        return self.datafs_size - self.datafs_used

    @property
    def datafs_available_pretty(self) -> str:
        if self.datafs_size > 0:
            perc = self.datafs_available / self.datafs_size
            return f"{convert_size(self.datafs_size)} ({perc:.0%} free)"
        return "Unknown"

    @property
    def datafs_size_pretty(self) -> str:
        if self.datafs_size > 0:
            return convert_size(self.datafs_size)
        return "Unknown"

    @property
    def datafs_used_pretty(self) -> str:
        if self.datafs_size:
            perc = self.datafs_used / self.datafs_size
            return f"{convert_size(self.datafs_used)} ({perc:.0%} used)"
        return "Unknown"

    # end datafs
    @property
    def rootfs_size_pretty(self) -> str:
        if self.rootfs_size > 0:
            return convert_size(self.rootfs_size)
        return "Unknown"

    @property
    def rootfs_used_pretty(self) -> str:
        if self.rootfs_size > 0:
            perc = self.rootfs_used / self.rootfs_size
            return f"{convert_size(self.rootfs_used)} ({perc:.0%} used)"
        return "Unknown"

    @property
    def rootfs_available(self) -> int:
        return self.rootfs_size - self.rootfs_used

    @property
    def rootfs_available_pretty(self) -> str:
        if self.rootfs_size > 0:
            perc = self.rootfs_available / self.rootfs_size
            return f"{convert_size(self.rootfs_size)} ({perc:.0%} free)"
        return "Unknown"


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
    mountpoint = models.CharField(max_length=255)

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
        if self.pi.network_settings.preferred_dns == PreferredDnsType.MULTICAST:
            return self.pi.mdns_hostname
        elif self.pi.network_settings.preferred_dns == PreferredDnsType.TAILSCALE:
            return self.pi.hostname
        raise ValueError(
            f"WebrtcStream.api_domain not implemented for {self.pi.network_settings.preferred_dns}"
        )

    @property
    def rtp_domain(self) -> str:
        if self.config_type == JanusConfigType.CLOUD:
            return settings.JANUS_CLOUD_RTP_DOMAIN
        if self.pi.network_settings.preferred_dns == PreferredDnsType.MULTICAST:
            return self.pi.mdns_hostname
        elif self.pi.network_settings.preferred_dns == PreferredDnsType.TAILSCALE:
            return self.pi.hostname
        raise ValueError(
            f"WebrtcStream.rtp_domain not implemented for {self.pi.network_settings.preferred_dns}"
        )

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
