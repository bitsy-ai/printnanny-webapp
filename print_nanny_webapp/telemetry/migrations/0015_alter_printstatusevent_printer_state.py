# Generated by Django 3.2.2 on 2021-05-31 21:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("telemetry", "0014_auto_20210531_1317"),
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
                ],
                max_length=255,
                null=True,
            ),
        ),
    ]
