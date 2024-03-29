# Generated by Django 3.2.12 on 2022-02-17 01:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import print_nanny_webapp.devices.models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("devices", "0002_device_setup_complete"),
    ]

    operations = [
        migrations.CreateModel(
            name="JanusCloudAuth",
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
                    "api_token",
                    models.CharField(
                        default=print_nanny_webapp.devices.models.get_random_string_32,
                        max_length=255,
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
            name="JanusCloudMediaStream",
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
                        related_name="janus_media_streams",
                        to="devices.device",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="JanusEdgeAuth",
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
                    "api_token",
                    models.CharField(
                        default=print_nanny_webapp.devices.models.get_random_string_32,
                        max_length=255,
                    ),
                ),
                ("admin_secret", models.CharField(max_length=255)),
                ("created_dt", models.DateTimeField(auto_now_add=True)),
                ("updated_dt", models.DateTimeField(auto_now=True)),
                (
                    "device",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="janus_edge_auth",
                        to="devices.device",
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="onboardingtask",
            name="device",
        ),
        migrations.AlterIndexTogether(
            name="task",
            index_together=None,
        ),
        migrations.RemoveField(
            model_name="task",
            name="device",
        ),
        migrations.AlterIndexTogether(
            name="taskstatus",
            index_together=None,
        ),
        migrations.RemoveField(
            model_name="taskstatus",
            name="task",
        ),
        migrations.DeleteModel(
            name="JanusAuth",
        ),
        migrations.DeleteModel(
            name="OnboardingTask",
        ),
        migrations.DeleteModel(
            name="Task",
        ),
        migrations.DeleteModel(
            name="TaskStatus",
        ),
        migrations.AddConstraint(
            model_name="janusedgeauth",
            constraint=models.UniqueConstraint(
                condition=models.Q(("deleted", None)),
                fields=("device",),
                name="unique_janus_edge_auth_per_device",
            ),
        ),
        migrations.AlterIndexTogether(
            name="janusedgeauth",
            index_together={("device", "created_dt", "updated_dt")},
        ),
        migrations.AddConstraint(
            model_name="januscloudmediastream",
            constraint=models.UniqueConstraint(
                condition=models.Q(("deleted", None)),
                fields=("device",),
                name="unique_janus_cloud_stream_per_device",
            ),
        ),
        migrations.AlterIndexTogether(
            name="januscloudmediastream",
            index_together={("device", "active", "created_dt", "updated_dt")},
        ),
    ]
