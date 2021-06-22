import logging
from typing import Dict, Any
from django.contrib.auth import get_user_model
import json
from django.utils import dateformat
from django.urls import reverse
from django.apps import apps
from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField, JSONField
from google.cloud import iot_v1 as cloudiot_v1
from google.protobuf.json_format import MessageToDict
import stringcase
from safedelete.models import SafeDeleteModel, SOFT_DELETE
from safedelete.managers import SafeDeleteManager
from safedelete.signals import pre_softdelete

from print_nanny_webapp.utils.time import pretty_time_delta
from print_nanny_webapp.utils.storages import PublicGoogleCloudStorage
from print_nanny_webapp.telemetry.types import PrintStatusEventType, PrinterState
from print_nanny_webapp.remote_control.utils import (
    delete_cloudiot_device,
    update_or_create_cloudiot_device,
    generate_keypair,
)

User = get_user_model()

logger = logging.getLogger(__name__)


def pre_softdelete_cloudiot_device(instance=None, **kwargs):
    fn = getattr(instance, "pre_softdelete", None)
    if hasattr(fn, "__call__"):
        return fn()


pre_softdelete.connect(pre_softdelete_cloudiot_device)


class OctoPrintDeviceManager(SafeDeleteManager):
    def update_or_create(self, defaults=None, **kwargs):
        serial = kwargs.get("serial")
        logging.info(f"Creating keypair for device serial={serial}")

        keypair = generate_keypair()

        serial = kwargs["serial"]
        cloudiot_device_name = f"serial-{serial}"
        cloudiot_device_dict, device_path = update_or_create_cloudiot_device(
            name=cloudiot_device_name,
            serial=serial,
            user_id=kwargs["user"].id,
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
            cloudiot_device=cloudiot_device_dict,
            cloudiot_device_path=device_path,
        )

        defaults.update(always_update)

        device, created = super().update_or_create(defaults=defaults, **kwargs)

        for key, value in always_update.items():
            setattr(device, key, value)
        logging.info(f"Device created: {created} with id={device.id}")
        device.cloudiot_device = cloudiot_device_dict
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


class OctoPrintDevice(SafeDeleteModel):

    _safedelete_policy = SOFT_DELETE

    objects = OctoPrintDeviceManager()

    MONITORING_ACTIVE_CSS = {
        True: "text-success",
        False: "text-secondary",
    }

    class MonitoringStatusChoices(models.TextChoices):
        MONITORING_ACTIVE = (
            "monitoring_active",
            "Print Nanny is currently monitoring your print job",
        )
        RENDERING_VIDEO = (
            "rendering_video",
            "Print Nanny is creating a timelapse video of your print job",
        )
        DONE = "done" "A timelapse of your print job is ready!"

    class MonitoringMode(models.TextChoices):
        ACTIVE_LEARNING = "active_learning", "Active Learning"
        LITE = "lite", "Lite"

    def pre_softdelete(self):
        return delete_cloudiot_device(self.cloudiot_device_num_id)

    @property
    def active_config(self):
        from print_nanny_webapp.ml_ops.models import ExperimentDeviceConfig

        active_config = ExperimentDeviceConfig.objects.filter(
            octoprint_device=self, experiment__active=True
        ).first()
        return active_config

    @property
    def last_command(self):
        return self.commands.order_by("-created_dt").first()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "serial"],
                condition=models.Q(deleted=None),
                name="unique_serial_per_user",
            )
        ]

    created_dt = models.DateTimeField(db_index=True, auto_now_add=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)

    last_session = models.ForeignKey(
        "remote_control.PrintSession",
        on_delete=models.CASCADE,
        db_index=True,
        null=True,
    )

    public_key = models.TextField()
    fingerprint = models.CharField(max_length=255)
    cloudiot_device = JSONField()
    cloudiot_device_name = models.CharField(max_length=255)
    cloudiot_device_path = models.CharField(max_length=255)
    cloudiot_device_num_id = models.BigIntegerField()

    model = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
    cpu_flags = ArrayField(models.CharField(max_length=255), null=True)

    hardware = models.CharField(max_length=255, null=True)  # /cat/cpuinfo HARDWARE
    revision = models.CharField(max_length=255, null=True)  # /cat/cpuinfo REVISION
    serial = models.CharField(max_length=255)  # /cat/cpuinfo Serial
    cores = models.IntegerField()
    ram = models.IntegerField()

    python_version = models.CharField(max_length=255)
    pip_version = models.CharField(max_length=255)
    virtualenv = models.CharField(max_length=255, null=True)

    monitoring_active = models.BooleanField(default=False)
    monitoring_mode = models.CharField(
        max_length=32, choices=MonitoringMode.choices, default=MonitoringMode.LITE
    )

    octoprint_version = models.CharField(max_length=255)
    plugin_version = models.CharField(max_length=255)
    print_nanny_client_version = models.CharField(max_length=255)

    monitoring_status = models.CharField(
        max_length=255,
        db_index=True,
        choices=MonitoringStatusChoices.choices,
        default=MonitoringStatusChoices.MONITORING_ACTIVE,
    )

    print_job_status = models.CharField(
        max_length=36, db_index=True, choices=PrintStatusEventType.choices, null=True
    )

    printer_state = models.CharField(
        max_length=36,
        db_index=True,
        choices=PrinterState.choices,
        default=PrinterState.OFFLINE,
    )

    def to_json(self):
        from print_nanny_webapp.remote_control.api.serializers import (
            OctoPrintDeviceSerializer,
        )

        serializer = OctoPrintDeviceSerializer(instance=self, context={"request": None})
        # TODO HyperLinkedIdentitySerialzier requires request context
        return json.dumps(serializer.data, sort_keys=True, indent=2)

    @property
    def manage_url(self):
        reverse("dashboard:octoprint-devices:detail", kwargs={"pk": self.id})

    @property
    def cloudiot_device_configs(self):
        """
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

    @property
    def cloudiot_device_status(self):
        client = cloudiot_v1.DeviceManagerClient()
        device_path = client.device_path(
            settings.GCP_PROJECT_ID,
            settings.GCP_CLOUD_IOT_DEVICE_REGISTRY_REGION,
            settings.GCP_CLOUD_IOT_DEVICE_REGISTRY,
            self.cloudiot_device_name,
        )
        cloudiot_device = client.get_device(name=device_path)
        cloudiot_device_dict = MessageToDict(cloudiot_device._pb)
        self.cloudiot_device = cloudiot_device_dict
        self.save()
        return cloudiot_device_dict

    @property
    def print_session_gcode_file(self):
        PrintStatusEvent = apps.get_model("telemetry", "PrintStatusEvent")

        last_print_session_event = (
            PrintStatusEvent.objects.filter(octoprint_device=self)
            .order_by("-ts")
            .first()
        )
        if last_print_session_event:
            return last_print_session_event.job_data_file
        else:
            return ""

    @property
    def printer_state_css_class(self):
        PrintStatusEvent = apps.get_model("telemetry", "PrintStatusEvent")
        return PrintStatusEvent.PRINTER_STATE_CSS_CLASS.get(
            self.printer_state, "text-warning"
        )

    @property
    def print_job_status_css_class(self):
        PrintStatusEvent = apps.get_model("telemetry", "PrintStatusEvent")
        if self.print_job_status:
            return PrintStatusEvent.JOB_EVENT_TYPE_CSS_CLASS.get(
                self.print_job_status, "text-warning"
            )

    @property
    def monitoring_active_css_class(self):
        return self.MONITORING_ACTIVE_CSS[self.monitoring_active]


class GcodeFile(models.Model):
    class Meta:
        unique_together = ("user", "file_hash")

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to="uploads/gcode_file/%Y/%m/%d/")
    file_hash = models.CharField(max_length=255)
    octoprint_device = models.ForeignKey(
        "remote_control.OctoPrintDevice", on_delete=models.CASCADE
    )


class PrinterProfile(models.Model):
    class Meta:
        unique_together = (
            "user",
            "octoprint_key",
        )

    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    octoprint_device = models.ForeignKey(
        "remote_control.OctoPrintDevice", on_delete=models.CASCADE, db_index=True
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
    name = models.CharField(max_length=255)
    octoprint_key = models.CharField(max_length=255, db_index=True)

    volume_custom_box = JSONField(default={})
    volume_depth = models.FloatField(null=True)
    volume_formfactor = models.CharField(null=True, max_length=255)
    volume_height = models.FloatField(null=True)
    volume_origin = models.CharField(null=True, max_length=255)
    volume_width = models.FloatField(null=True)


class PrintSession(models.Model):
    """
    Represents a unique print job/session
    """

    class Meta:
        unique_together = ("octoprint_device", "session")

    created_dt = models.DateTimeField(db_index=True)
    updated_dt = models.DateTimeField(auto_now=True)
    octoprint_device = models.ForeignKey(
        OctoPrintDevice, on_delete=models.CASCADE, db_index=True
    )
    session = models.CharField(max_length=255, db_index=True)

    filepos = models.IntegerField(null=True)
    print_progress = models.IntegerField(null=True)
    time_elapsed = models.IntegerField(null=True)
    time_remaining = models.IntegerField(null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    printer_profile = models.ForeignKey(
        PrinterProfile, on_delete=models.CASCADE, null=True
    )
    gcode_file = models.ForeignKey(GcodeFile, on_delete=models.CASCADE, null=True)
    gcode_filename = models.CharField(max_length=255, null=True)
    octoprint_job = JSONField(null=True)

    @property
    def datesegment(self):
        return dateformat.format(self.created_dt, "Y/m/d/")

    @property
    def duration(self):
        return pretty_time_delta(
            int((self.created_dt - self.updated_dt).total_seconds())
        )

    def __str__(self):
        return self.session


class RemoteControlCommandManager(models.Manager):
    def create(self, **kwargs):
        client = cloudiot_v1.DeviceManagerClient()
        device: OctoPrintDevice = kwargs["device"]
        device_path = client.device_path(
            settings.GCP_PROJECT_ID,
            settings.GCP_CLOUD_IOT_DEVICE_REGISTRY_REGION,
            settings.GCP_CLOUD_IOT_DEVICE_REGISTRY,
            device.cloudiot_device_name,
        )

        obj = super().create(
            iotcore_response={},
            **kwargs,
        )

        data: Dict[str, Any] = {
            "remote_control_command_id": obj.id,
            "command": kwargs.get("command"),
            "octoprint_event_type": obj.octoprint_event_type,
        }
        data_b: bytes = json.dumps(data).encode("utf-8")

        # https://cloud.google.com/iot/docs/how-tos/commands#commands_compared_to_configurations
        # for faster commands (without state / version checking)
        response = client.send_command_to_device(
            request={
                "name": device_path,
                "binary_data": data_b,
                "subfolder": "remote_control",
            }
        )

        dict_response = MessageToDict(response._pb)
        obj.iotcore_response = dict_response
        obj.save()
        return obj


public_storage = PublicGoogleCloudStorage()


class RemoteControlCommand(models.Model):

    PLUGIN_EVENT_PREFIX = "plugin_octoprint_nanny_"

    objects = RemoteControlCommandManager()

    class Command(models.TextChoices):
        MONITORING_STOP = "monitoring_stop", "Stop Print Nanny Monitoring"
        MONITORING_START = "monitoring_start", "Start Print Nanny Monitoring"
        PRINT_START = "print_start", "Start Print"
        PRINT_STOP = "print_stop", "Stop Print"
        PRINT_PAUSE = "print_pause", "Pause Print"
        PRINT_RESUME = "print_resume", "Resume Print"
        MOVE_NOZZLE = "move_nozzle", "Move Nozzle"
        PONG = "connect_test_mqtt_pong", "Pong"

    COMMAND_CODES = [x.value for x in Command.__members__.values()]

    @classmethod
    def get_valid_actions(cls, print_job_status):
        valid_actions = {
            PrintStatusEventType.PRINT_STARTED: [
                cls.Command.PRINT_STOP,
                cls.Command.PRINT_PAUSE,
            ],
            PrintStatusEventType.PRINT_DONE: [
                # cls.Command.MOVE_NOZZLE,
                cls.Command.MONITORING_START,
                cls.Command.MONITORING_STOP,
            ],
            PrintStatusEventType.PRINT_CANCELLED: [cls.Command.MOVE_NOZZLE],
            PrintStatusEventType.PRINT_CANCELLING: [],
            PrintStatusEventType.PRINT_PAUSED: [
                cls.Command.PRINT_STOP,
                cls.Command.PRINT_RESUME,
                # cls.Command.MOVE_NOZZLE,
            ],
            PrintStatusEventType.PRINT_FAILED: [cls.Command.MOVE_NOZZLE],
            None: [
                cls.Command.MONITORING_START,
                cls.Command.MONITORING_STOP,
            ],
        }
        return valid_actions[print_job_status]

    ACTION_CSS_CLASSES = {
        Command.PRINT_STOP: "danger",
        Command.PRINT_PAUSE: "warning",
        Command.PRINT_RESUME: "info",
    }
    created_dt = models.DateTimeField(auto_now_add=True)
    command = models.CharField(max_length=255, choices=Command.choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device = models.ForeignKey(
        OctoPrintDevice, on_delete=models.CASCADE, related_name="commands"
    )
    received = models.BooleanField(default=False)
    success = models.BooleanField(null=True)
    iotcore_response = JSONField(default={})

    metadata = JSONField(default={})

    @property
    def octoprint_event_type(self):
        return self.PLUGIN_EVENT_PREFIX + stringcase.snakecase(self.command)
