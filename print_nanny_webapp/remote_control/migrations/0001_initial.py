# Generated by Django 3.1.7 on 2021-05-04 09:15

from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="GcodeFile",
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
                ("name", models.CharField(max_length=255)),
                ("file", models.FileField(upload_to="uploads/gcode_file/%Y/%m/%d/")),
                ("file_hash", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="OctoPrintDevice",
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
                ("deleted", models.DateTimeField(editable=False, null=True)),
                ("created_dt", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("name", models.CharField(max_length=255)),
                ("public_key", models.TextField()),
                ("fingerprint", models.CharField(max_length=255)),
                ("cloudiot_device", django.contrib.postgres.fields.jsonb.JSONField()),
                ("cloudiot_device_name", models.CharField(max_length=255)),
                ("cloudiot_device_path", models.CharField(max_length=255)),
                ("cloudiot_device_num_id", models.BigIntegerField()),
                ("model", models.CharField(max_length=255)),
                ("platform", models.CharField(max_length=255)),
                (
                    "cpu_flags",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=255),
                        null=True,
                        size=None,
                    ),
                ),
                ("hardware", models.CharField(max_length=255, null=True)),
                ("revision", models.CharField(max_length=255, null=True)),
                ("serial", models.CharField(max_length=255)),
                ("cores", models.IntegerField()),
                ("ram", models.IntegerField()),
                ("python_version", models.CharField(max_length=255)),
                ("pip_version", models.CharField(max_length=255)),
                ("virtualenv", models.CharField(max_length=255, null=True)),
                ("monitoring_active", models.BooleanField(default=False)),
                (
                    "monitoring_mode",
                    models.CharField(
                        choices=[
                            ("active_learning", "Active Learning"),
                            ("lite", "Lite"),
                        ],
                        default="lite",
                        max_length=32,
                    ),
                ),
                ("octoprint_version", models.CharField(max_length=255)),
                ("plugin_version", models.CharField(max_length=255)),
                ("print_nanny_client_version", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="PrinterProfile",
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
                ("axes_e_inverted", models.BooleanField(null=True)),
                ("axes_e_speed", models.IntegerField(null=True)),
                ("axes_x_speed", models.IntegerField(null=True)),
                ("axes_x_inverted", models.BooleanField(null=True)),
                ("axes_y_inverted", models.BooleanField(null=True)),
                ("axes_y_speed", models.IntegerField(null=True)),
                ("axes_z_inverted", models.BooleanField(null=True)),
                ("axes_z_speed", models.IntegerField(null=True)),
                ("extruder_count", models.IntegerField(null=True)),
                ("extruder_nozzle_diameter", models.FloatField(null=True)),
                ("extruder_shared_nozzle", models.BooleanField(null=True)),
                ("heated_bed", models.BooleanField(null=True)),
                ("heated_chamber", models.BooleanField(null=True)),
                ("model", models.CharField(blank=True, max_length=255, null=True)),
                ("name", models.CharField(max_length=255)),
                ("octoprint_key", models.CharField(db_index=True, max_length=255)),
                (
                    "volume_custom_box",
                    django.contrib.postgres.fields.jsonb.JSONField(default={}),
                ),
                ("volume_depth", models.FloatField(null=True)),
                ("volume_formfactor", models.CharField(max_length=255, null=True)),
                ("volume_height", models.FloatField(null=True)),
                ("volume_origin", models.CharField(max_length=255, null=True)),
                ("volume_width", models.FloatField(null=True)),
                (
                    "octoprint_device",
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
                "unique_together": {("user", "octoprint_key")},
            },
        ),
        migrations.CreateModel(
            name="RemoteControlCommand",
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
                (
                    "command",
                    models.CharField(
                        choices=[
                            ("monitoring_stop", "Stop Print Nanny Monitoring"),
                            ("monitoring_start", "Start Print Nanny Monitoring"),
                            ("print_start", "Start Print"),
                            ("print_stop", "Stop Print"),
                            ("print_pause", "Pause Print"),
                            ("print_resume", "Resume Print"),
                            ("move_nozzle", "Move Nozzle"),
                        ],
                        max_length=255,
                    ),
                ),
                ("received", models.BooleanField(default=False)),
                ("success", models.BooleanField(null=True)),
                (
                    "iotcore_response",
                    django.contrib.postgres.fields.jsonb.JSONField(default={}),
                ),
                (
                    "metadata",
                    django.contrib.postgres.fields.jsonb.JSONField(default={}),
                ),
                (
                    "device",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="commands",
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
        ),
        migrations.CreateModel(
            name="PrintSession",
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
                ("updated_dt", models.DateTimeField(auto_now=True)),
                ("session", models.CharField(db_index=True, max_length=255)),
                ("filepos", models.IntegerField(null=True)),
                ("print_progress", models.IntegerField(null=True)),
                ("time_elapsed", models.IntegerField(null=True)),
                ("time_remaining", models.IntegerField(null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            (
                                "monitoring_active",
                                "Print Nanny is currently monitoring your print job",
                            ),
                            (
                                "rendering_video",
                                "Print Nanny is creating a timelapse video of your print job",
                            ),
                            ("doneA timelapse of your print job is ready!", "Done"),
                        ],
                        db_index=True,
                        default="monitoring_active",
                        max_length=255,
                    ),
                ),
                ("gcode_filename", models.CharField(max_length=255, null=True)),
                (
                    "gcode_file",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="remote_control.gcodefile",
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
                    "printer_profile",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="remote_control.printerprofile",
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
                "unique_together": {("octoprint_device", "session")},
            },
        ),
        migrations.AddField(
            model_name="octoprintdevice",
            name="last_session",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="remote_control.printsession",
            ),
        ),
        migrations.AddField(
            model_name="octoprintdevice",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="gcodefile",
            name="octoprint_device",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="remote_control.octoprintdevice",
            ),
        ),
        migrations.AddField(
            model_name="gcodefile",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddConstraint(
            model_name="octoprintdevice",
            constraint=models.UniqueConstraint(
                condition=models.Q(deleted=None),
                fields=("user", "serial"),
                name="unique_serial_per_user",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="gcodefile",
            unique_together={("user", "file_hash")},
        ),
    ]
