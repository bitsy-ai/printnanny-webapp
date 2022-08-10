# Generated by Django 3.2.12 on 2022-08-05 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0017_auto_20220803_1800"),
    ]

    operations = [
        migrations.CreateModel(
            name="PiGstreamerEvent",
            fields=[
                (
                    "basepievent_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="events.basepievent",
                    ),
                ),
                (
                    "event_type",
                    models.CharField(
                        choices=[
                            ("StartCommand", "Start gstreamer pipelines"),
                            ("StartSuccess", "gstreamer pipeline started successfully"),
                            ("StartError", "error starting gstreamer pipeline"),
                            ("StopCommand", "Stop gstreamer pipelines"),
                            ("StopSuccess", "gstreamer pipeline stopped"),
                            (
                                "StopError",
                                "error attempting to stop gstreamer pipeline",
                            ),
                        ],
                        db_index=True,
                        max_length=32,
                    ),
                ),
            ],
            bases=("events.basepievent",),
        ),
        migrations.RemoveField(
            model_name="pigstreamercommand",
            name="basepievent_ptr",
        ),
        migrations.AlterField(
            model_name="pibootevent",
            name="event_type",
            field=models.CharField(
                choices=[
                    ("RebootCommand", "Reboot Raspberry Pi"),
                    ("RebootStarted", "Raspberry Pi will reboot soon"),
                    ("RebootError", "Unexpected error during reboot"),
                    ("ShutdownCommand", "Shutdown Raspberry Pi"),
                    ("ShutdownStarted", "Raspberry Pi will shutdown soon"),
                    ("ShutdownError", "Unexpected error during shutdown"),
                    (
                        "BootStarted",
                        "Emitted during boot process, typically after systemd network-online.target",
                    ),
                    (
                        "BootSuccess",
                        "Boot reached default.target with no errors or degraded services",
                    ),
                    (
                        "BootDegraded",
                        "At least one systemd service reports degraded state",
                    ),
                ],
                db_index=True,
                max_length=32,
            ),
        ),
        migrations.DeleteModel(
            name="PiBootCommand",
        ),
        migrations.DeleteModel(
            name="PiGstreamerCommand",
        ),
    ]