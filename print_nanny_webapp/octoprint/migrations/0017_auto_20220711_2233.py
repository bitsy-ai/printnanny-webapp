# Generated by Django 3.2.12 on 2022-07-11 22:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("octoprint", "0016_auto_20220620_2205"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="octoprintsettings",
            name="created_dt",
        ),
        migrations.RemoveField(
            model_name="octoprintsettings",
            name="monitoring_auto_pause",
        ),
        migrations.RemoveField(
            model_name="octoprintsettings",
            name="monitoring_auto_start",
        ),
        migrations.RemoveField(
            model_name="octoprintsettings",
            name="telemetry_enabled",
        ),
        migrations.AddField(
            model_name="octoprintsettings",
            name="octoprint_enabled",
            field=models.BooleanField(
                default=True, help_text="Start OctoPrint service"
            ),
        ),
        migrations.AlterField(
            model_name="octoprintsettings",
            name="events_enabled",
            field=models.BooleanField(
                default=True,
                help_text="Send OctoPrint events related to print job status/progress to PrintNanny Cloud https://docs.octoprint.org/en/master/events/index.html",
            ),
        ),
    ]
