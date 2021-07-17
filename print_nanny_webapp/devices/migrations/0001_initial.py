# Generated by Django 3.2.5 on 2021-07-17 06:49

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Device",
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
                ("updated_dt", models.DateTimeField(auto_now=True, db_index=True)),
                ("name", models.CharField(max_length=255)),
                ("public_key", models.TextField()),
                ("fingerprint", models.CharField(max_length=255)),
                ("cloudiot_device_name", models.CharField(max_length=255)),
                ("cloudiot_device_path", models.CharField(max_length=255)),
                ("cloudiot_device_num_id", models.BigIntegerField()),
                ("os_version", models.CharField(max_length=255)),
                ("os", models.CharField(max_length=255)),
                ("kernel_version", models.CharField(max_length=255)),
                ("hardware", models.CharField(max_length=255, null=True)),
                ("revision", models.CharField(max_length=255, null=True)),
                ("model", models.CharField(max_length=255, null=True)),
                ("serial", models.CharField(max_length=255, null=True)),
                ("cores", models.IntegerField()),
                ("ram", models.BigIntegerField()),
                (
                    "cpu_flags",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=255), size=None
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="devices",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("user", "name")},
            },
        ),
        migrations.CreateModel(
            name="PrinterController",
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
                ("updated_dt", models.DateTimeField(auto_now=True, db_index=True)),
                ("cli_version", models.CharField(max_length=255)),
                (
                    "device",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="printer_controllers",
                        to="devices.device",
                    ),
                ),
                (
                    "polymorphic_ctype",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="polymorphic_devices.printercontroller_set+",
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="printer_controllers",
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
            name="PrinterProfile",
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
                ("updated_dt", models.DateTimeField(auto_now=True, db_index=True)),
                ("name", models.CharField(max_length=255)),
                ("local_webcam", models.CharField(max_length=255)),
                (
                    "controller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="printer_profiles",
                        to="devices.printercontroller",
                    ),
                ),
                (
                    "device",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="devices.device"
                    ),
                ),
                (
                    "polymorphic_ctype",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="polymorphic_devices.printerprofile_set+",
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="printer_profiles",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("user", "name")},
            },
        ),
        migrations.CreateModel(
            name="OctoprintController",
            fields=[
                (
                    "printercontroller_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="devices.printercontroller",
                    ),
                ),
                ("python_version", models.CharField(max_length=255)),
                ("pip_version", models.CharField(max_length=255)),
                ("virtualenv", models.CharField(max_length=255, null=True)),
                ("octoprint_version", models.CharField(max_length=255)),
                ("plugin_version", models.CharField(max_length=255)),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("devices.printercontroller",),
        ),
        migrations.CreateModel(
            name="OctoprintPrinterProfile",
            fields=[
                (
                    "printerprofile_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="devices.printerprofile",
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
                ("volume_custom_box", models.JSONField(default=dict)),
                ("volume_depth", models.FloatField(null=True)),
                ("volume_formfactor", models.CharField(max_length=255, null=True)),
                ("volume_height", models.FloatField(null=True)),
                ("volume_origin", models.CharField(max_length=255, null=True)),
                ("volume_width", models.FloatField(null=True)),
                (
                    "octoprint_controller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="devices.octoprintcontroller",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("devices.printerprofile",),
        ),
    ]
