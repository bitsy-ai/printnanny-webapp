from django.contrib.postgres.fields.jsonb import JSONField
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from google.cloud import iot_v1 as cloudiot_v1
from google.protobuf.json_format import MessageToDict
from django.conf import settings

from safedelete.models import SafeDeleteModel, SOFT_DELETE
from safedelete.managers import SafeDeleteManager
from safedelete.signals import pre_softdelete

UserModel = get_user_model()


class Device(SafeDeleteModel):
    """
    1-1 relationship with Cloud Iot Device (GCP)
    1-many relationship with PrinterController models
    System-level information

    """

    def pre_softdelete(self):
        return delete_cloudiot_device(self.cloudiot_device_num_id)

    _safedelete_policy = SOFT_DELETE

    created_dt = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_dt = models.DateTimeField(db_index=True, auto_now=True)
    user = models.ForeignKey(UserModel)

    hostname = models.CharField(max_length=255)

    # PKI
    public_key = models.TextField()
    fingerprint = models.CharField(max_length=255)

    # GCP cloudiot API params
    cloudiot_device = JSONField()
    cloudiot_device_name = models.CharField(max_length=255)
    cloudiot_device_path = models.CharField(max_length=255)
    cloudiot_device_num_id = models.BigIntegerField()

    # System info

    platform = models.CharField(max_length=255)
    cpu_flags = models.CharField(max_length=255)

    # /proc/cpuinfo HARDWARE
    hardware = models.CharField(max_length=255, null=True)
    # /proc/cpuinfo REVISION
    revision = models.CharField(max_length=255, null=True)
    # /proc/cpuinfo MODEL
    model = models.CharField(max_length=255)
    # /proc/cpuinfo SERIAL
    serial = models.CharField(max_length=255)
    # /proc/cpuinfo MAX PROCESSOR
    cores = models.IntegerField()
    ram = models.IntegerField()

    # TODO enable front-end views in release v0.8 go-live
    # @property
    # def manage_url(self):
    #     reverse("dashboard:devices:detail", kwargs={"pk": self.id})

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


class OctoprintController(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    created_dt = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_dt = models.DateTimeField(db_index=True, auto_now=True)
    user = models.ForeignKey(UserModel)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    python_version = models.CharField(max_length=255)
    pip_version = models.CharField(max_length=255)
    virtualenv = models.CharField(max_length=255, null=True)

    octoprint_version = models.CharField(max_length=255)
    plugin_version = models.CharField(max_length=255)
    print_nanny_client_version = models.CharField(max_length=255)
