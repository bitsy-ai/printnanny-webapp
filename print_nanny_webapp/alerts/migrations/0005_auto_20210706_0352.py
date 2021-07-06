# Generated by Django 3.2.5 on 2021-07-06 03:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import print_nanny_webapp.alerts.models


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("telemetry", "0020_alter_printerevent_printer_state"),
        ("remote_control", "0024_alter_printsession_print_job_status"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("alerts", "0004_alter_alertsettings_event_types"),
    ]

    operations = [
        migrations.CreateModel(
            name="Alert",
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
                ("updated_dt", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "alert_method",
                    models.CharField(
                        choices=[
                            ("UI", "Print Nanny UI"),
                            ("EMAIL", "Email notifications"),
                            ("DISCORD", "Discord channel (webhook)"),
                            ("PARTNER_3DGEEKS", "3D Geeks mobile app"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "polymorphic_ctype",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="polymorphic_alerts.alert_set+",
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
            name="TestAlert",
            fields=[
                (
                    "alert_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="alerts.alert",
                    ),
                ),
                (
                    "event_type",
                    models.CharField(
                        choices=[
                            (
                                "PrintNannyWebapp",
                                "Test triggered via Print Nanny UI or webapp",
                            )
                        ],
                        max_length=36,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("alerts.alert",),
        ),
        migrations.CreateModel(
            name="VideoStatusAlert",
            fields=[
                (
                    "alert_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="alerts.alert",
                    ),
                ),
                (
                    "event_type",
                    models.CharField(
                        choices=[("VideoDone", "{{ GCODE_FILE }} - timelapse done 🎥")],
                        max_length=36,
                    ),
                ),
                (
                    "annotated_video",
                    models.FileField(
                        upload_to=print_nanny_webapp.alerts.models._upload_to
                    ),
                ),
                (
                    "octoprint_device",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="remote_control.octoprintdevice",
                    ),
                ),
                (
                    "print_session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="remote_control.printsession",
                    ),
                ),
            ],
            bases=("alerts.alert",),
        ),
        migrations.CreateModel(
            name="PrintStatusAlert",
            fields=[
                (
                    "alert_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="alerts.alert",
                    ),
                ),
                (
                    "event_type",
                    models.CharField(
                        choices=[
                            ("PrintDone", "{{ GCODE_FILE }} - job finished ✅"),
                            ("PrintFailed", "{{ GCODE_FILE }} - job failed ❌"),
                            ("PrintPaused", "{{ GCODE_FILE }} - job paused ⏸️"),
                            ("PrintResumed", "{{ GCODE_FILE }} - job resumed ⏯️"),
                            ("PrintStarted", "{{ GCODE_FILE }} - job started 🏁"),
                            ("PrintCancelled", "{{ GCODE_FILE }} - job cancelled ❌"),
                        ],
                        max_length=36,
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="telemetry.telemetryevent",
                    ),
                ),
                (
                    "octoprint_device",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="remote_control.octoprintdevice",
                    ),
                ),
                (
                    "print_session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="remote_control.printsession",
                    ),
                ),
            ],
            bases=("alerts.alert",),
        ),
        migrations.CreateModel(
            name="PrintProgressAlert",
            fields=[
                (
                    "alert_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="alerts.alert",
                    ),
                ),
                (
                    "event_type",
                    models.CharField(
                        choices=[
                            (
                                "PrintProgress",
                                "{{ GCODE_FILE }} - {{ PRINT_PROGRESS }}% complete ⏳",
                            )
                        ],
                        max_length=36,
                    ),
                ),
                ("print_progress", models.IntegerField()),
                ("needs_review", models.BooleanField(default=False)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="telemetry.telemetryevent",
                    ),
                ),
                (
                    "octoprint_device",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="remote_control.octoprintdevice",
                    ),
                ),
                (
                    "print_session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="remote_control.printsession",
                    ),
                ),
            ],
            bases=("alerts.alert",),
        ),
        migrations.AddConstraint(
            model_name="videostatusalert",
            constraint=models.UniqueConstraint(
                fields=("print_session", "event_type"), name="unique_video_status_alert"
            ),
        ),
        migrations.AddConstraint(
            model_name="printstatusalert",
            constraint=models.UniqueConstraint(
                fields=("print_session", "event_type"), name="unique_print_status_alert"
            ),
        ),
        migrations.AddConstraint(
            model_name="printprogressalert",
            constraint=models.UniqueConstraint(
                fields=("print_session", "print_progress"),
                name="unique_print_progress_alert",
            ),
        ),
    ]
