# Generated by Django 3.2.12 on 2022-07-11 19:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("devices", "0026_auto_20220711_1917"),
    ]

    operations = [
        migrations.AlterField(
            model_name="devicesettings",
            name="octoprint_enabled",
            field=models.BooleanField(
                default=True, help_text="Start OctoPrint service"
            ),
        ),
    ]
