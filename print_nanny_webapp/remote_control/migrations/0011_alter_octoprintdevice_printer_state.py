# Generated by Django 3.2.2 on 2021-05-31 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("remote_control", "0010_auto_20210531_1234"),
    ]

    operations = [
        migrations.AlterField(
            model_name="octoprintdevice",
            name="printer_state",
            field=models.CharField(
                choices=[
                    ("operational", "Printer Connected"),
                    ("paused", "Paused"),
                    ("cancelling", "Cancelling"),
                    ("printing", "Printing"),
                    ("pausing", "Pausing"),
                    ("sdReady", "SD Card Available"),
                    ("error", "Error"),
                    ("readyPrinter Ready", "Ready"),
                    ("closedOrError", "Printer Connection Closed"),
                    ("offline", "Printer Offline"),
                ],
                db_index=True,
                default="offline",
                max_length=36,
            ),
        ),
    ]
