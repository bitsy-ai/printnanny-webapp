# Generated by Django 3.2.12 on 2022-08-11 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("octoprint", "0021_baseoctoprintevent"),
    ]

    operations = [
        migrations.CreateModel(
            name="OctoPrintClientStatus",
            fields=[
                (
                    "baseoctoprintevent_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="octoprint.baseoctoprintevent",
                    ),
                ),
                (
                    "event_type",
                    models.CharField(
                        choices=[
                            (
                                "ClientOpened",
                                "Client has connected to OctoPrint push socket.",
                            ),
                            (
                                "ClientAuthed",
                                "Client has authenticated user session on OctoPrint psuh socket.",
                            ),
                            (
                                "ClientClosed",
                                "Client has disconnected from push socket",
                            ),
                        ],
                        db_index=True,
                        max_length=32,
                    ),
                ),
            ],
            bases=("octoprint.baseoctoprintevent",),
        ),
        migrations.CreateModel(
            name="OctoPrintPrinterStatus",
            fields=[
                (
                    "baseoctoprintevent_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="octoprint.baseoctoprintevent",
                    ),
                ),
                (
                    "event_type",
                    models.CharField(
                        choices=[
                            ("PrinterOffline", "Printer is offline"),
                            ("PrinterOpenSerial", "Opening serial connection"),
                            ("PrinterConnecting", "Printer connecting"),
                            ("PrinterOperational", "Printer is ready to use"),
                            ("PrinterStarting", "Printer is starting job"),
                            ("PrinterInProgress", "Printer is running job"),
                            ("PrinterCancelling", "Printer is cancelling job"),
                            ("PrinterPausing", "Printer is pausing job"),
                            ("PrinterPaused", "Printer paused job"),
                            ("PrinterResuming", "Printer is resuming job"),
                            ("PrinterFinishing", "Printer is finishing job"),
                            ("PrinterError", "Printer connection error"),
                        ],
                        db_index=True,
                        max_length=32,
                    ),
                ),
            ],
            bases=("octoprint.baseoctoprintevent",),
        ),
        migrations.CreateModel(
            name="OctoPrintPrintJobStatus",
            fields=[
                (
                    "baseoctoprintevent_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="octoprint.baseoctoprintevent",
                    ),
                ),
                (
                    "event_type",
                    models.CharField(
                        choices=[
                            ("PrintProgress", "Print Progress"),
                            ("PrintStarted", "Print Job Started"),
                            ("PrintFailed", "Print Job Failed"),
                            ("PrintDone", "Print Job Done"),
                            ("PrintCancelling", "Print Job Cancelling"),
                            ("PrintCancelled", "Print Job Cancelled"),
                            ("PrintPaused", "Print Job Paused"),
                            ("PrintResumed", "Print Job Resumed"),
                        ],
                        db_index=True,
                        max_length=32,
                    ),
                ),
            ],
            bases=("octoprint.baseoctoprintevent",),
        ),
        migrations.CreateModel(
            name="OctoPrintServerEvent",
            fields=[
                (
                    "baseoctoprintevent_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="octoprint.baseoctoprintevent",
                    ),
                ),
                (
                    "event_type",
                    models.CharField(
                        choices=[
                            ("Startup", "Server Startup"),
                            ("Shutdown", "Server Shutdown"),
                        ],
                        db_index=True,
                        max_length=32,
                    ),
                ),
            ],
            bases=("octoprint.baseoctoprintevent",),
        ),
    ]
