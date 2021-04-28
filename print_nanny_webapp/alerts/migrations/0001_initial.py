# Generated by Django 3.1.3 on 2020-12-07 00:27

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import print_nanny_webapp.alerts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("remote_control", "0002_auto_20201126_1453_squashed_0040_octoprintdevice_configs"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="AlertVideoMessage",
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
                (
                    "provider_id",
                    models.CharField(db_index=True, max_length=255, null=True),
                ),
                ("seen", models.BooleanField(default=False)),
                (
                    "job_status",
                    models.CharField(
                        choices=[
                            ("Processing", "Processing"),
                            ("SUCCESS", "Success"),
                            ("FAILURE", "Failure"),
                        ],
                        default="Processing",
                        max_length=32,
                    ),
                ),
                ("created_dt", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_dt", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "dataframe",
                    models.FileField(
                        null=True, upload_to=print_nanny_webapp.alerts.models._upload_to
                    ),
                ),
                (
                    "original_video",
                    models.FileField(
                        null=True, upload_to=print_nanny_webapp.alerts.models._upload_to
                    ),
                ),
                (
                    "annotated_video",
                    models.FileField(
                        null=True, upload_to=print_nanny_webapp.alerts.models._upload_to
                    ),
                ),
                ("feedback", models.BooleanField(null=True)),
                ("length", models.FloatField(null=True)),
                ("fps", models.FloatField(null=True)),
                (
                    "polymorphic_ctype",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="polymorphic_alerts.alertvideomessage_set+",
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
            name="TimelapseAlert",
            fields=[
                (
                    "alertvideomessage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="alerts.alertvideomessage",
                    ),
                ),
                ("notify_seconds", models.IntegerField(null=True)),
                ("notify_timecode", models.CharField(max_length=32, null=True)),
                (
                    "tags",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=255),
                        default=["timelapse-alert"],
                        size=None,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("alerts.alertvideomessage",),
        ),
        migrations.CreateModel(
            name="AlertPlot",
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
                (
                    "image",
                    models.ImageField(
                        upload_to=print_nanny_webapp.alerts.models._upload_to
                    ),
                ),
                (
                    "html",
                    models.FileField(
                        upload_to=print_nanny_webapp.alerts.models._upload_to
                    ),
                ),
                ("title", models.CharField(max_length=65)),
                ("description", models.CharField(max_length=255)),
                ("function", models.CharField(max_length=65)),
                (
                    "alert",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="alerts.alertvideomessage",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProgressAlert",
            fields=[
                (
                    "alertvideomessage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="alerts.alertvideomessage",
                    ),
                ),
                (
                    "tags",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=255),
                        default=["progress-alert"],
                        size=None,
                    ),
                ),
                # (
                #     "print_job",
                #     models.ForeignKey(
                #         on_delete=django.db.models.deletion.CASCADE,
                #         to="remote_control.printjob",
                #     ),
                # ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("alerts.alertvideomessage",),
        ),
        migrations.CreateModel(
            name="DefectAlert",
            fields=[
                (
                    "alertvideomessage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="alerts.alertvideomessage",
                    ),
                ),
                (
                    "last_action",
                    models.CharField(
                        choices=[
                            ("PENDING", "Pending User Action"),
                            ("RESUME_ALERTS", "Resume for Print Job"),
                            ("CANCEL_PRINT", "Cancel Print Job Cancel"),
                        ],
                        default="PENDING",
                        max_length=16,
                    ),
                ),
                (
                    "tags",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=255),
                        default=["defect-alert"],
                        size=None,
                    ),
                ),
                # (
                #     "print_job",
                #     models.ForeignKey(
                #         on_delete=django.db.models.deletion.CASCADE,
                #         to="remote_control.printjob",
                #     ),
                # ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("alerts.alertvideomessage",),
        ),
    ]
