# Generated by Django 3.2.12 on 2022-04-18 01:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("octoprint", "0012_gcodefile_created_dt"),
    ]

    operations = [
        migrations.AlterField(
            model_name="octoprintinstall",
            name="printnanny_plugin_version",
            field=models.CharField(max_length=64),
        ),
    ]
