# Generated by Django 3.2.12 on 2022-03-20 04:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("octoprint", "0005_octoprintsettings"),
    ]

    operations = [
        migrations.AddField(
            model_name="octoprintbackup",
            name="deleted",
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.CreateModel(
            name="OctoPrinterProfile",
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
                ("volume_custom_box", models.JSONField(default={})),
                ("volume_depth", models.FloatField(null=True)),
                ("volume_formfactor", models.CharField(max_length=255, null=True)),
                ("volume_height", models.FloatField(null=True)),
                ("volume_origin", models.CharField(max_length=255, null=True)),
                ("volume_width", models.FloatField(null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="octo_printer_profiles",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GcodeFile",
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
                ("name", models.CharField(max_length=255)),
                ("file", models.FileField(upload_to="uploads/gcode_file/%Y/%m/%d/")),
                ("hash", models.CharField(max_length=255)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="gcode_files",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="octoprinterprofile",
            constraint=models.UniqueConstraint(
                condition=models.Q(("deleted", None)),
                fields=("user", "octoprint_key"),
                name="unique_printer_profile_name_per_user",
            ),
        ),
        migrations.AddConstraint(
            model_name="gcodefile",
            constraint=models.UniqueConstraint(
                condition=models.Q(("deleted", None)),
                fields=("user", "hash"),
                name="unique_gcode_file_hash_per_user",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="gcodefile",
            unique_together={("user", "name", "hash")},
        ),
    ]
