import logging
import tempfile
import os
from django.contrib.auth import get_user_model

import json
from django.apps import apps
from django.db import models
from django.utils import timezone
from urllib.parse import urljoin
from django.core.files.base import ContentFile, File
from django.conf import settings
from django.contrib.postgres.fields import ArrayField, JSONField
from django.contrib.sites.shortcuts import get_current_site
from google.cloud import iot_v1 as cloudiot_v1
from google.protobuf.json_format import MessageToDict
import google.api_core.exceptions
import stringcase

from print_nanny_webapp.client_events.models import PrintJobEventTypeChoices
from print_nanny_webapp.utils.storages import PublicGoogleCloudStorage
from print_nanny_webapp.remote_control.utils import (
    update_or_create_cloudiot_device,
    generate_keypair,
)

User = get_user_model()

logger = logging.getLogger(__name__)


class OctoPrintDeviceManager(models.Manager):
    def update_or_create(self, defaults=None, **kwargs):
        serial = kwargs.get("serial")
        logging.info(f"Creating keypair for device serial={serial}")

        keypair = generate_keypair()

        serial = kwargs.get("serial")
        cloudiot_device_name = f"serial-{serial}"
        cloudiot_device_dict, device_path = update_or_create_cloudiot_device(
            name=cloudiot_device_name,
            serial=serial,
            user_id=kwargs.get("user").id,
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
                device=device,
                experiment=active_experiment,
            )

        return device, created


class OctoPrintDevice(models.Model):
    objects = OctoPrintDeviceManager()

    MONITORING_ACTIVE_CSS = {
        True: "text-success",
        False: "text-secondary",
    }

    @property
    def active_config(self):
        from print_nanny_webapp.ml_ops.models import ExperimentDeviceConfig

        active_config = ExperimentDeviceConfig.objects.filter(
            device=self, experiment__active=True
        ).first()
        return active_config

    @property
    def last_snapshot(self):
        if self.last_command:
            return self.last_command.last_snapshot

    @property
    def last_command(self):
        return self.commands.order_by("-created_dt").first()

    class Meta:
        unique_together = ("user", "serial")

    created_dt = models.DateTimeField(db_index=True, auto_now_add=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)

    public_key = models.TextField()
    fingerprint = models.CharField(max_length=255)
    cloudiot_device = JSONField()
    cloudiot_device_name = models.CharField(max_length=255)
    cloudiot_device_path = models.CharField(max_length=255)
    cloudiot_device_num_id = models.BigIntegerField()

    model = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
    cpu_flags = ArrayField(models.CharField(max_length=255))

    hardware = models.CharField(max_length=255)  # /cat/cpuinfo HARDWARE
    revision = models.CharField(max_length=255)  # /cat/cpuinfo REVISION
    serial = models.CharField(max_length=255)  # /cat/cpuinfo Serial
    cores = models.IntegerField()
    ram = models.IntegerField()

    python_version = models.CharField(max_length=255)
    pip_version = models.CharField(max_length=255)
    virtualenv = models.CharField(max_length=255)
    monitoring_active = models.BooleanField(default=False)

    octoprint_version = models.CharField(max_length=255)
    plugin_version = models.CharField(max_length=255)
    print_nanny_client_version = models.CharField(max_length=255)

    def to_json(self):
        from print_nanny_webapp.remote_control.api.serializers import (
            OctoPrintDeviceSerializer,
        )

        serializer = OctoPrintDeviceSerializer(instance=self)
        return json.dumps(serializer.data, sort_keys=True, indent=2)

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
    def print_job_status(self):
        PrintJobEvent = apps.get_model("client_events", "PrintJobEvent")

        last_print_job_event = (
            PrintJobEvent.objects.filter(device=self).order_by("-created_dt").first()
        )
        if last_print_job_event:
            return last_print_job_event.event_type
        else:
            return "Idle"

    @property
    def print_job_gcode_file(self):
        PrintJobEvent = apps.get_model("client_events", "PrintJobEvent")

        last_print_job_event = (
            PrintJobEvent.objects.filter(device=self).order_by("-created_dt").first()
        )
        if last_print_job_event:
            return last_print_job_event.job_data_file
        else:
            return ""

    @property
    def print_job_status_css_class(self):
        PrintJobEvent = apps.get_model("client_events", "PrintJobEvent")

        return PrintJobEvent.JOB_EVENT_TYPE_CSS_CLASS[self.print_job_status]

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


class PrintJob(models.Model):
    class Meta:
        unique_together = ("user", "name", "created_dt")

    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    printer_profile = models.ForeignKey(PrinterProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    gcode_file = models.ForeignKey(GcodeFile, on_delete=models.CASCADE, null=True)

    last_status = models.CharField(
        max_length=56,
        choices=PrintJobEventTypeChoices.choices,
        default=PrintJobEventTypeChoices.PRINT_STARTED,
    )
    last_seen = models.DateTimeField(auto_now=True)

    # {'completion': 0.0008570890761342134, 'filepos': 552, 'printTime': 0, 'printTimeLeft': 29826, 'printTimeLeftOrigin': 'analysis'}.
    progress = JSONField(default={})
    octoprint_device = models.ForeignKey(
        "remote_control.OctoPrintDevice", on_delete=models.SET_NULL, null=True
    )

    @property
    def filename(self):
        return self.gcode_file.file.name


class RemoteControlCommandManager(models.Manager):
    def create(self, **kwargs):
        client = cloudiot_v1.DeviceManagerClient()

        device = kwargs.get("device")
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

        data = {
            "remote_control_command_id": obj.id,
            "command": kwargs.get("command"),
            "octoprint_event_type": obj.octoprint_event_type,
        }
        data = json.dumps(data).encode("utf-8")

        # https://cloud.google.com/iot/docs/how-tos/commands#commands_compared_to_configurations
        # for faster commands (without state / version checking)
        response = client.send_command_to_device(
            request={
                "name": device_path,
                "binary_data": data,
                "subfolder": "remote_control",
            }
        )

        dict_response = MessageToDict(response._pb)
        obj.iotcore_response = dict_response
        obj.save()
        return obj


public_storage = PublicGoogleCloudStorage()


class RemoteControlSnapshot(models.Model):
    created_dt = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to="uploads/remote_control_snapshot/%Y/%m/%d/", storage=public_storage
    )
    command = models.ForeignKey(
        "remote_control.RemoteControlCommand",
        on_delete=models.CASCADE,
        related_name="snapshots",
    )


class RemoteControlCommand(models.Model):
    objects = RemoteControlCommandManager()

    PLUGIN_EVENT_PREFIX = "plugin_octoprint_nanny_"

    class CommandChoices(models.TextChoices):
        MONITORING_STOP = "MonitoringStop", "Stop Print Nanny Monitoring"
        MONITORING_START = "MonitoringStart", "Start Print Nanny Monitoring"
        SNAPSHOT = "Snapshot", "Capture a webcam snapshot"
        PRINT_START = "PrintStart", "Start Print"
        MOVE_NOZZLE = "MoveNozzle", "Move Nozzle"
        PRINT_STOP = "PrintStop", "Stop Print"
        PRINT_PAUSE = "PrintPause", "Pause Print"
        PRINT_RESUME = "PrintResume", "Resume Print"

    @property
    def last_snapshot(self):
        last_snapshot = self.snapshots.order_by("-created_dt").first()
        return last_snapshot

    @classmethod
    def to_octoprint_events(cls):
        return [
            cls.PLUGIN_EVENT_PREFIX + stringcase.snakecase(x) for x in cls.COMMAND_CODES
        ]

    COMMAND_CODES = [x.value for x in CommandChoices.__members__.values()]

    VALID_ACTIONS = {
        PrintJobEventTypeChoices.PRINT_STARTED: [
            CommandChoices.PRINT_STOP,
            CommandChoices.PRINT_PAUSE,
        ],
        PrintJobEventTypeChoices.PRINT_DONE: [
            CommandChoices.MOVE_NOZZLE,
            CommandChoices.MONITORING_START,
            CommandChoices.MONITORING_STOP,
            CommandChoices.SNAPSHOT,
        ],
        PrintJobEventTypeChoices.PRINT_CANCELLED: [CommandChoices.MOVE_NOZZLE],
        PrintJobEventTypeChoices.PRINT_CANCELLING: [],
        PrintJobEventTypeChoices.PRINT_PAUSED: [
            CommandChoices.PRINT_STOP,
            CommandChoices.PRINT_RESUME,
            CommandChoices.MOVE_NOZZLE,
        ],
        PrintJobEventTypeChoices.PRINT_FAILED: [CommandChoices.MOVE_NOZZLE],
        "Idle": [
            CommandChoices.MONITORING_START,
            CommandChoices.MONITORING_STOP,
            CommandChoices.SNAPSHOT,
        ],
    }

    ACTION_CSS_CLASSES = {
        CommandChoices.PRINT_STOP: "danger",
        CommandChoices.PRINT_PAUSE: "warning",
        CommandChoices.PRINT_RESUME: "info",
    }
    created_dt = models.DateTimeField(auto_now_add=True)
    command = models.CharField(max_length=255, choices=CommandChoices.choices)
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
