# Generated by Django 3.2.12 on 2022-08-19 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0031_alter_pibootcommand_event_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pibootcommand",
            name="event_type",
            field=models.CharField(
                choices=[
                    ("Reboot", "Reboot Raspberry Pi"),
                    ("Shutdown", "Shutdown Raspberry Pi"),
                    ("SyncSettings", "Sync Raspberry Pi settings"),
                    ("SystemctlShow", "Get output from `systemctl show`"),
                ],
                db_index=True,
                max_length=32,
            ),
        ),
        migrations.AlterField(
            model_name="pibootstatus",
            name="event_type",
            field=models.CharField(
                choices=[
                    ("SystemctlShow", "Get output from `systemctl show`"),
                    ("RebootStarted", "Raspberry Pi will reboot soon"),
                    ("RebootError", "Unexpected error during reboot"),
                    ("ShutdownStarted", "Raspberry Pi will shutdown soon"),
                    ("ShutdownError", "Unexpected error during shutdown"),
                    (
                        "BootStarted",
                        "Emitted during boot process, typically after systemd network-online.target",
                    ),
                    (
                        "BootSuccess",
                        "Boot reached default.target with no errors or degraded services",
                    ),
                    (
                        "BootDegraded",
                        "At least one systemd service reports degraded state",
                    ),
                    (
                        "SyncSettingsStarted",
                        "Raspberry Pi started synchronizing settings",
                    ),
                    (
                        "SyncSettingsSuccess",
                        "Success synchronizing Raspberry Pi settings",
                    ),
                    ("SyncSettingsError", "Error synchronizing Raspberry Pi settings"),
                ],
                db_index=True,
                max_length=32,
            ),
        ),
    ]
