import base64
import hashlib
import logging
import subprocess
import tempfile
import os
from django.contrib.auth import get_user_model

from django.apps import apps
from django.db import models
from django.utils import timezone
from urllib.parse import urljoin
from django.core.files.base import ContentFile
from django.conf import settings
from django.contrib.postgres.fields import ArrayField, JSONField
from django.contrib.sites.shortcuts import get_current_site
from google.cloud import iot_v1 as cloudiot_v1
from google.protobuf.json_format import MessageToDict
import google.api_core.exceptions

User = get_user_model()

logger = logging.getLogger(__name__)

class KeyPairProvisioning(Exception):
    pass

class OctoPrintDeviceManager(models.Manager):
    def update_or_create(self, defaults=None, **kwargs):
        logging.info(f'Defaults: {defaults} Kwargs: {kwargs}')
        with tempfile.TemporaryDirectory() as tmp:
            tmp_private_key_filename = f"{tmp}/rsa_private.pem"
            tmp_public_key_filename = f"{tmp}/rsa_public.pem"
            p = subprocess.run(
                [
                    "openssl",
                    "genpkey",
                    "-algorithm",
                    "RSA",
                    "-out",
                    tmp_private_key_filename,
                    "-pkeyopt",
                    "rsa_keygen_bits:2048",
                ],
                capture_output=True
            )
            logger.debug(p.stdout)
            if p.stderr != b'':
                logger.error(f'Error running openssl genpkey {p.stderr}')
                #raise KeyPairProvisioning(p.stderr)

            p = subprocess.run(
                [
                    "openssl",
                    "rsa",
                    "-in",
                    tmp_private_key_filename,
                    "-pubout",
                    "-out",
                    tmp_public_key_filename,
                ],
                capture_output=True
            )
            logger.debug(p.stdout)
            if p.stderr != b'':
                logger.error(f'Error running openssl rsa {p.stderr}')
                #raise KeyPairProvisioning(p.stderr)

            p = subprocess.run(
                [
                    "openssl",
                    "sha3-512",
                    "-c",
                    tmp_public_key_filename,
                ],
                capture_output=True,
            )
            logger.debug(p.stdout)
            if p.stderr != b'':
                logger.error(p.stderr)
                #raise KeyPairProvisioning(p.stderr)

            fingerprint = p.stdout
            fingerprint = fingerprint.decode().split("=")[-1]
            fingerprint = fingerprint.strip()

            client = cloudiot_v1.DeviceManagerClient()

            with open(tmp_public_key_filename) as pub_f:
                public_key_content = pub_f.read().strip()
                public_key_file = ContentFile(public_key_content.encode())

            with open(tmp_private_key_filename) as priv_f:
                private_key_content = priv_f.read().strip()
                private_key_file = ContentFile(private_key_content.encode())

            parent = client.registry_path(
                settings.GCP_PROJECT_ID,
                settings.GCP_CLOUD_IOT_DEVICE_REGISTRY_REGION,
                settings.GCP_CLOUD_IOT_DEVICE_REGISTRY,
            )

            serial = kwargs.get("serial")
            cloudiot_device_name = f"serial-{serial}"
            device_template = {
                "id": cloudiot_device_name,
                "credentials": [
                    {
                        "public_key": {
                            "format": cloudiot_v1.PublicKeyFormat.RSA_PEM,
                            "key": public_key_content,
                        }
                    }
                ],
            }

            device_path = client.device_path(
                settings.GCP_PROJECT_ID,
                settings.GCP_CLOUD_IOT_DEVICE_REGISTRY_REGION,
                settings.GCP_CLOUD_IOT_DEVICE_REGISTRY,
                cloudiot_device_name
            )

            try:
                cloudiot_device = client.delete_device(
                    name=device_path
                )
                logger.info(f'Deleted existing device {device_path}')
            except google.api_core.exceptions.NotFound:
                pass

            cloudiot_device = client.create_device(
                parent=parent, device=device_template
            )
            cloudiot_device_created = True

            logger.info(f'Created new deivce in registry {device_path}')


            cloudiot_device_dict = MessageToDict(cloudiot_device._pb)
            logger.info(f"iot create_device() succeeded {cloudiot_device_dict}")

            cloudiot_device_num_id = cloudiot_device_dict.get("numId")

            always_update = dict(
                private_key=private_key_file,
                public_key=public_key_file,
                fingerprint=fingerprint,
                cloudiot_device_num_id=cloudiot_device_num_id,
                cloudiot_device_name=cloudiot_device_name,
                cloudiot_device=cloudiot_device_dict,    
            )

            defaults.update(always_update)

            device, created = super().update_or_create(
                defaults=defaults,
                **kwargs
            )

            for key, value in always_update.items():
                setattr(device, key, value)
            logging.info(f'Device created: {created} with id={device.id}')
            device.cloudiot_device = cloudiot_device_dict
            device.private_key.save(f"{serial}_private.pem", private_key_file)
            device.public_key.save(f"{serial}_public.pem", public_key_file)
            device.save()
            return device, created


class OctoPrintDevice(models.Model):
    objects = OctoPrintDeviceManager()

    class Meta:
        unique_together = ("user", "serial")

    created_dt = models.DateTimeField(db_index=True, auto_now_add=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)

    private_key = models.FileField(upload_to="uploads/private_key/")
    public_key = models.FileField(upload_to="uploads/public_key/")
    fingerprint = models.CharField(max_length=255)
    cloudiot_device = JSONField()
    cloudiot_device_name = models.CharField(max_length=255)
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

    octoprint_version = models.CharField(max_length=255)
    plugin_version = models.CharField(max_length=255)
    print_nanny_client_version = models.CharField(max_length=255)

    @property
    def active_print_job(self):
        pass


class GcodeFile(models.Model):
    class Meta:
        unique_together = ("user", "file_hash")

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to="uploads/gcode_file/%Y/%m/%d/")
    file_hash = models.CharField(max_length=255)


class PrinterProfile(models.Model):
    class Meta:
        unique_together = (
            "user",
            "octoprint_id",
        )

    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)

    axes_e_inverted = models.BooleanField()
    axes_e_speed = models.IntegerField()

    axes_x_speed = models.IntegerField()
    axes_x_inverted = models.BooleanField()

    axes_y_inverted = models.BooleanField()
    axes_y_speed = models.IntegerField()

    axes_z_inverted = models.BooleanField()
    axes_z_speed = models.IntegerField()

    extruder_count = models.IntegerField()
    extruder_nozzle_diameter = models.FloatField()
    extruder_shared_nozzle = models.BooleanField()

    heated_bed = models.BooleanField()
    heated_chamber = models.BooleanField()

    model = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)
    octoprint_id = models.CharField(max_length=255, db_index=True)

    volume_custom_box = models.BooleanField()
    volume_depth = models.FloatField()
    volume_formfactor = models.CharField(max_length=255)
    volume_height = models.FloatField()
    volume_origin = models.CharField(max_length=255)
    volume_width = models.FloatField()


class PrintJob(models.Model):
    class Meta:
        unique_together = ("user", "name", "dt")

    class StatusChoices(models.TextChoices):
        STARTED = "STARTED", "Started"
        DONE = "DONE", "Done"
        FAILED = "FAILED", "Failed"
        CANCELLING = "CANCELLING", "Cancelling"
        CANCELLED = "CANCELLED", "Cancelled"
        PAUSED = "PAUSED", "Paused"
        RESUMED = "RESUMED", "Resumed"

    dt = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    printer_profile = models.ForeignKey(PrinterProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    gcode_file = models.ForeignKey(GcodeFile, on_delete=models.CASCADE, null=True)
    last_status = models.CharField(
        max_length=12, choices=StatusChoices.choices, default=StatusChoices.STARTED
    )
    last_seen = models.DateTimeField(auto_now=True)

    progress = models.IntegerField(default=0)
    octoprint_device = models.ForeignKey(
        "remote_control.OctoPrintDevice", on_delete=models.SET_NULL, null=True
    )

    @property
    def filename(self):
        return self.gcode_file.file.name
