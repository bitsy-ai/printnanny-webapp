# Generated by Django 3.1.3 on 2021-02-14 00:00

from django.db import migrations, models
from django.apps import apps
import django.db.models.deletion

DeviceCalibration = apps.get_model("ml_ops", "DeviceCalibration")


class Migration(migrations.Migration):

    dependencies = [
        ("remote_control", "0042_auto_20210207_2249_squashed_0049_auto_20210321_1313"),
        ("ml_ops", "0010_devicecalibration_coordinates"),
    ]

    operations = [
        migrations.DeleteModel(
            name="devicecalibration",
        )
    ]
