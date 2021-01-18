# Generated by Django 3.1.3 on 2021-01-17 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("remote_control", "0019_auto_20210109_2034"),
        ("alerts", "0016_auto_20210116_1604"),
    ]

    operations = [
        migrations.AddField(
            model_name="remotecontrolcommandalert",
            name="alert_subtype",
            field=models.CharField(
                choices=[
                    ("RECEIVED", "Command was received by"),
                    ("SUCCESS", "Command succeeded"),
                    ("FAILED", "Command failed"),
                ],
                default="RECEIVED",
                max_length=255,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="remotecontrolcommandalert",
            name="command",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="remote_control.remotecontrolcommand",
            ),
            preserve_default=False,
        ),
    ]
