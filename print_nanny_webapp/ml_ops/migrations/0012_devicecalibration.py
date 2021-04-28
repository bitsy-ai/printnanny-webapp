# Generated by Django 3.1.3 on 2021-02-14 00:05

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("remote_control", "0042_auto_20210207_2249_squashed_0049_auto_20210321_1313"),
        ("ml_ops", "0011_auto_20210213_1600"),
    ]

    operations = [
        migrations.CreateModel(
            name="DeviceCalibration",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_dt", models.DateTimeField(auto_now_add=True)),
                ("updated_dt", models.DateTimeField(auto_now=True)),
                ("fpm", models.IntegerField(null=True)),
                (
                    "coordinates",
                    django.contrib.postgres.fields.jsonb.JSONField(null=True),
                ),
                ("mask", django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                (
                    "octoprint_device",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="remote_control.octoprintdevice",
                    ),
                ),
            ],
        ),
    ]
