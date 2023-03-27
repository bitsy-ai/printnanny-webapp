# Generated by Django 3.2.12 on 2022-02-17 05:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import print_nanny_webapp.devices.models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("devices", "0003_auto_20220217_0118"),
    ]

    operations = [
        migrations.CreateModel(
            name="JanusAuth",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("deleted", models.DateTimeField(editable=False, null=True)),
                ("admin_secret", models.CharField(max_length=255, null=True)),
                (
                    "api_token",
                    models.CharField(
                        default=print_nanny_webapp.devices.models.get_random_string_32,
                        max_length=255,
                    ),
                ),
                (
                    "config_type",
                    models.CharField(
                        choices=[
                            ("cloud", "Cloud WebRTC Gateway"),
                            ("edge", "Edge WebRTC Gateway"),
                        ],
                        default="cloud",
                        max_length=32,
                    ),
                ),
                ("created_dt", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="janus_cloud_auth",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="JanusStream",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("deleted", models.DateTimeField(editable=False, null=True)),
                (
                    "config_type",
                    models.CharField(
                        choices=[
                            ("cloud", "Cloud WebRTC Gateway"),
                            ("edge", "Edge WebRTC Gateway"),
                        ],
                        default="cloud",
                        max_length=32,
                    ),
                ),
                ("active", models.BooleanField(default=False)),
                (
                    "secret",
                    models.CharField(
                        default=print_nanny_webapp.devices.models.get_random_string_32,
                        max_length=255,
                    ),
                ),
                (
                    "pin",
                    models.CharField(
                        default=print_nanny_webapp.devices.models.get_random_string_32,
                        max_length=255,
                    ),
                ),
                ("info", models.JSONField(default=dict)),
                ("created_dt", models.DateTimeField(auto_now_add=True)),
                ("updated_dt", models.DateTimeField(auto_now=True)),
                (
                    "device",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="janus_streams",
                        to="devices.device",
                    ),
                ),
            ],
        ),
        migrations.AlterIndexTogether(
            name="januscloudmediastream",
            index_together=None,
        ),
        migrations.RemoveField(
            model_name="januscloudmediastream",
            name="device",
        ),
        migrations.AlterIndexTogether(
            name="janusedgeauth",
            index_together=None,
        ),
        migrations.RemoveField(
            model_name="janusedgeauth",
            name="device",
        ),
        migrations.DeleteModel(
            name="JanusCloudAuth",
        ),
        migrations.DeleteModel(
            name="JanusCloudMediaStream",
        ),
        migrations.DeleteModel(
            name="JanusEdgeAuth",
        ),
        migrations.AddConstraint(
            model_name="janusstream",
            constraint=models.UniqueConstraint(
                condition=models.Q(("deleted", None)),
                fields=("device", "config_type"),
                name="unique_janus_stream_per_device",
            ),
        ),
        migrations.AlterIndexTogether(
            name="janusstream",
            index_together={("device", "active", "created_dt", "updated_dt")},
        ),
    ]
