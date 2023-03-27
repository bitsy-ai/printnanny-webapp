# Generated by Django 3.2.12 on 2022-07-11 22:03

from django.db import migrations, models
import print_nanny_webapp.devices.models


class Migration(migrations.Migration):
    dependencies = [
        ("devices", "0027_alter_devicesettings_octoprint_enabled"),
    ]

    operations = [
        migrations.AlterField(
            model_name="janusstream",
            name="admin_secret",
            field=models.CharField(
                default=print_nanny_webapp.devices.models.get_random_string_32,
                help_text="Janus Gateway Admin API secret. Will be null if config_type=CLOUD",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="janusstream",
            name="api_token",
            field=models.CharField(
                default=print_nanny_webapp.devices.models.get_random_string_32,
                max_length=255,
            ),
        ),
    ]
