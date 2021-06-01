# Generated by Django 3.2.2 on 2021-05-31 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("telemetry", "0015_alter_printstatusevent_printer_state"),
    ]

    operations = [
        migrations.AlterField(
            model_name="printstatusevent",
            name="printer_state",
            field=models.CharField(
                choices=[
                    ("Operational", "Printer Connected"),
                    ("Paused", "Paused"),
                    ("Cancelling", "Cancelling"),
                    ("Printing", "Printing"),
                    ("Pausing", "Pausing"),
                    ("sdReady", "SD Card Available"),
                    ("Error", "Error"),
                    ("ReadyPrinter Ready", "Ready"),
                    ("closedOrError", "Printer Connection Closed"),
                    ("Offline", "Printer Offline"),
                    ("Opening serial connection", "Opening serial connection"),
                    ("Connection", "Establishing printer connection"),
                    ("Resuming", "Resuming"),
                    ("Finishing", "Finishing"),
                ],
                max_length=255,
                null=True,
            ),
        ),
    ]
