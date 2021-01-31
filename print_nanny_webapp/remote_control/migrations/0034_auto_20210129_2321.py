# Generated by Django 3.1.3 on 2021-01-30 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("remote_control", "0033_remotecontrolsnapshot_created_dt"),
    ]

    operations = [
        migrations.AlterField(
            model_name="remotecontrolcommand",
            name="command",
            field=models.CharField(
                choices=[
                    ("MonitoringStop", "Stop Print Nanny Monitoring"),
                    ("MonitoringStart", "Start Print Nanny Monitoring"),
                    ("Snapshot", "Capture a webcam snapshot"),
                    ("PrintStart", "Start Print"),
                    ("MoveNozzle", "Move Nozzle"),
                    ("PrintStop", "Stop Print"),
                    ("PrintPause", "Pause Print"),
                    ("PrintResume", "Resume Print"),
                ],
                max_length=255,
            ),
        ),
    ]
