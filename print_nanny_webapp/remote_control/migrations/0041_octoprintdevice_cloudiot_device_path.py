# Generated by Django 3.1.3 on 2021-02-06 22:28

from django.db import migrations, models
from django.conf import settings
from google.cloud import iot_v1 as cloudiot_v1


def set_cloudiot_device_path(apps, schema_editor):
    OctoPrintDevice = apps.get_model("remote_control", "OctoPrintDevice")
    client = cloudiot_v1.DeviceManagerClient()

    for device in OctoPrintDevice.objects.all().iterator():
        device_path = client.device_path(
            settings.GCP_PROJECT_ID,
            settings.GCP_CLOUD_IOT_DEVICE_REGISTRY_REGION,
            settings.GCP_CLOUD_IOT_DEVICE_REGISTRY,
            device.cloudiot_device_name,
        )
        device.cloudiot_device_path = device_path
        device.save()


def reverse_cloudiot_device_path(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        (
            "remote_control",
            "0002_auto_20201126_1453_squashed_0040_octoprintdevice_configs",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="octoprintdevice",
            name="cloudiot_device_path",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.RunPython(set_cloudiot_device_path, reverse_cloudiot_device_path),
        migrations.AlterField(
            model_name="octoprintdevice",
            name="cloudiot_device_path",
            field=models.CharField(max_length=255),
        ),
    ]
