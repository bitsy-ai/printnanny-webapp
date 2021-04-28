# Generated by Django 3.1.3 on 2020-12-25 00:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("remote_control", "0002_auto_20201126_1453_squashed_0040_octoprintdevice_configs"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="PredictEventFile",
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
                    "annotated_image",
                    models.ImageField(upload_to="uploads/predict_event/%Y/%m/%d/"),
                ),
                ("hash", models.CharField(max_length=255)),
                (
                    "original_image",
                    models.ImageField(upload_to="uploads/predict_event/%Y/%m/%d/"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PredictSession",
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
                ("closed_dt", models.DateTimeField(auto_now=True, db_index=True)),
                ("closed", models.BooleanField(default=False)),
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
            name="PredictEvent",
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
                ("dt", models.DateTimeField(auto_now=True, db_index=True)),
                ("predict_data", models.JSONField()),
                (
                    "files",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="client_events.predicteventfile",
                    ),
                ),
                (
                    "predict_session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="client_events.predictsession",
                    ),
                ),
                # (
                #     "print_job",
                #     models.ForeignKey(
                #         null=True,
                #         on_delete=django.db.models.deletion.CASCADE,
                #         to="remote_control.printjob",
                #     ),
                # ),
            ],
        ),
        migrations.CreateModel(
            name="OctoPrintEvent",
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
                ("dt", models.DateTimeField(db_index=True)),
                (
                    "event_type",
                    models.CharField(
                        choices=[
                            ("ClientAuthed", "ClientAuthed"),
                            ("ClientClosed", "ClientClosed"),
                            ("ClientDeauthed", "ClientDeauthed"),
                            ("ClientOpened", "ClientOpened"),
                            ("SettingsUpdated", "SettingsUpdated"),
                            ("FileAdded", "FileAdded"),
                            ("FileRemoved", "FileRemoved"),
                            ("FolderAdded", "FolderAdded"),
                            ("FolderRemoved", "FolderRemoved"),
                            ("TransferDone", "TransferDone"),
                            ("TransferFailed", "TransferFailed"),
                            ("TransferStarted", "TransferStarted"),
                            ("UpdatedFiles", "UpdatedFiles"),
                            ("Upload", "Upload"),
                            ("CaptureDone", "CaptureDone"),
                            ("CaptureFailed", "CaptureFailed"),
                            ("CaptureStart", "CaptureStart"),
                            ("MovieDone", "MovieDone"),
                            ("MovieFailed", "MovieFailed"),
                            ("MovieRendering", "MovieRendering"),
                            ("PostRollEnd", "PostRollEnd"),
                            ("PostRollStart", "PostRollStart"),
                            ("SlicingCancelled", "SlicingCancelled"),
                            ("SlicingDone", "SlicingDone"),
                            ("SlicingFailed", "SlicingFailed"),
                            ("SlicingProfileAdded", "SlicingProfileAdded"),
                            ("SlicingProfileDeleted", "SlicingProfileDeleted"),
                            ("SlicingProfileModified", "SlicingProfileModified"),
                            ("SlicingStarted", "SlicingStarted"),
                            ("Connected", "Connected"),
                            ("Disconnected", "Disconnected"),
                            ("PrinterReset", "PrinterReset"),
                            ("PrinterProfileAdded", "PrinterProfileAdded"),
                            ("PrinterProfileDeleted", "PrinterProfileDeleted"),
                            ("PrinterProfileModified", "PrinterProfileModified"),
                            ("Error", "Error"),
                            ("PrintCancelled", "PrintCancelled"),
                            ("PrintCancelling", "PrintCancelling"),
                            ("PrintDone", "PrintDone"),
                            ("PrintFailed", "PrintFailed"),
                            ("PrintPaused", "PrintPaused"),
                            ("PrintResumed", "PrintResumed"),
                            ("PrintStarted", "PrintStarted"),
                            ("Shutdown", "Shutdown"),
                            ("Startup", "Startup"),
                        ],
                        db_index=True,
                        max_length=30,
                    ),
                ),
                ("event_data", models.JSONField()),
                ("plugin_version", models.CharField(max_length=30)),
                ("octoprint_version", models.CharField(max_length=30)),
                # (
                #     "print_job",
                #     models.ForeignKey(
                #         null=True,
                #         on_delete=django.db.models.deletion.CASCADE,
                #         to="remote_control.printjob",
                #     ),
                # ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
