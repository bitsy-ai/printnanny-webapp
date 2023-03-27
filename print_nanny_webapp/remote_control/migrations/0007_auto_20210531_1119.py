# Generated by Django 3.2.2 on 2021-05-31 18:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("remote_control", "0006_auto_20210531_1015"),
    ]

    operations = [
        migrations.RenameField(
            model_name="octoprintdevice",
            old_name="active_session",
            new_name="last_session",
        ),
        migrations.AddField(
            model_name="printsession",
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
                    ("closedOrError", "Printer Disconnected"),
                ],
                db_index=True,
                max_length=36,
                null=True,
            ),
        ),
    ]
