# Generated by Django 3.2.12 on 2022-04-13 04:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("devices", "0014_auto_20220401_1652"),
    ]

    operations = [
        migrations.AddField(
            model_name="device",
            name="edition",
            field=models.CharField(
                choices=[
                    ("octoprint_desktop", "PrintNanny OS OctoPrint Desktop"),
                    ("octoprint_lite", "PrintNanny OS OctoPrint Lite/Headless"),
                    ("repetier_desktop", "PrintNanny OS Repetier Desktop"),
                    ("repetier_lite", "PrintNanny OS Repetier Lite/Headless"),
                    ("mainsail_desktop", "PrintNanny OS Mainsail Desktop"),
                    ("mainsail_lite", "PrintNanny OS Mainsail Lite/Headless"),
                ],
                default="octoprint_desktop",
                max_length=32,
            ),
            preserve_default=False,
        ),
    ]
