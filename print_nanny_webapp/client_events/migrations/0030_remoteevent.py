# Generated by Django 3.1.7 on 2021-04-28 03:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("remote_control", "0061_auto_20210425_2253"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("client_events", "0029_auto_20210328_1610"),
    ]

    operations = [
        migrations.CreateModel(
            name="RemoteEvent",
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
                ("created_dt", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("event_data", models.JSONField(null=True)),
                ("plugin_version", models.CharField(max_length=60)),
                ("client_version", models.CharField(max_length=60)),
                ("octoprint_version", models.CharField(max_length=60)),
                (
                    "event_type",
                    models.CharField(
                        choices=[
                            (
                                "monitoring_start_received",
                                "MONITORING_START command was received by device",
                            ),
                            (
                                "monitoring_start_failed",
                                "MONITORING_START command failed. Please download your Octoprint logs and open a Github issue to get this fixed.",
                            ),
                            (
                                "monitoring_start_success",
                                "MONITORING_START command succeeded. Live monitoring feed enabled",
                            ),
                            (
                                "monitoring_stop_received",
                                "MONITORING_STOP command was received by device",
                            ),
                            (
                                "monitoring_stop_failed",
                                "MONITORING_STOP command failed. Please download your Octoprint logs and open a Github issue to get this fixed.",
                            ),
                            (
                                "monitoring_stop_success",
                                "MONITORING_STOP command succeeded. Monitoring feed is now disabled.",
                            ),
                        ],
                        db_index=True,
                        max_length=255,
                    ),
                ),
                (
                    "device",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="remote_control.octoprintdevice",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
