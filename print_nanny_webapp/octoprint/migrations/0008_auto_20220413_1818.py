# Generated by Django 3.2.12 on 2022-04-13 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("octoprint", "0007_auto_20220412_0221"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="octoprintsettings",
            name="user",
        ),
        migrations.AddField(
            model_name="octoprintsettings",
            name="auto_backup",
            field=models.CharField(default="0 0 * * 2", max_length=64),
        ),
        migrations.AddField(
            model_name="octoprintsettings",
            name="events_enabled",
            field=models.BooleanField(
                default=False,
                help_text="Send OctoPrint events to PrintNanny Cloud https://docs.octoprint.org/en/master/events/index.html",
            ),
        ),
        migrations.AddField(
            model_name="octoprintsettings",
            name="octoprint_install",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="settings",
                to="octoprint.octoprintinstall",
            ),
        ),
        migrations.AddField(
            model_name="octoprintsettings",
            name="telemetry_enabled",
            field=models.BooleanField(
                default=False,
                help_text="Send telemetry data to PrintNanny Cloud for debugging/analytics purposes",
            ),
        ),
        migrations.AlterField(
            model_name="octoprintsettings",
            name="sync_gcode",
            field=models.BooleanField(
                default=True, help_text="Sync Gcode files to/from PrintNanny Cloud"
            ),
        ),
        migrations.AlterField(
            model_name="octoprintsettings",
            name="sync_printer_profiles",
            field=models.BooleanField(
                default=True, help_text="Sync Printer Profiles to/from PrintNanny Cloud"
            ),
        ),
    ]