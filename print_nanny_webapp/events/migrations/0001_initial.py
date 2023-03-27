# Generated by Django 3.2.9 on 2022-01-30 20:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("devices", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
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
                ("created_dt", models.DateTimeField(auto_now_add=True, db_index=True)),
                (
                    "source",
                    models.CharField(
                        choices=[
                            ("octoprint", "Events originating from OctoPrint"),
                            ("printnanny", "Events originating from Print Nanny"),
                            ("mainsail", "Events originating from moonraker"),
                        ],
                        max_length=32,
                    ),
                ),
                (
                    "polymorphic_ctype",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="polymorphic_events.event_set+",
                        to="contenttypes.contenttype",
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
                "base_manager_name": "objects",
            },
        ),
        migrations.CreateModel(
            name="DeviceEvent",
            fields=[
                (
                    "event_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="events.event",
                    ),
                ),
                (
                    "command",
                    models.BooleanField(
                        default=False,
                        help_text="Indicates whether event should be sent to Device on command topic",
                    ),
                ),
                (
                    "device",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="devices.device"
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("events.event",),
        ),
        migrations.CreateModel(
            name="TestEvent",
            fields=[
                (
                    "deviceevent_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="events.deviceevent",
                    ),
                ),
                (
                    "event_type",
                    models.CharField(
                        choices=[
                            ("mqtt_ping", "MQTT Ping Event"),
                            ("mqtt_pong", "MQTT Pong Event"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("sent", "Sent"),
                            ("ack", "Acknowledged"),
                            ("success", "Success"),
                            ("failed", "Failed"),
                            ("timeout", "Timeout"),
                        ],
                        default="sent",
                        max_length=255,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("events.deviceevent",),
        ),
    ]
