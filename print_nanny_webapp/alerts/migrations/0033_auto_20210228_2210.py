# Generated by Django 3.1.7 on 2021-03-01 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("remote_control", "0047_remove_printjob_last_status"),
        ("alerts", "0032_merge_20210228_1735"),
    ]

    operations = [
        migrations.AddField(
            model_name="alert",
            name="octoprint_device",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="remote_control.octoprintdevice",
            ),
        ),
        migrations.AlterField(
            model_name="discordmethodsettings",
            name="target_id_type",
            field=models.CharField(
                choices=[("USER", "User"), ("CHANNEL", "Channel")],
                db_index=True,
                max_length=255,
            ),
        ),
    ]
