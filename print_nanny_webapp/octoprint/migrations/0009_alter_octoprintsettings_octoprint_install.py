# Generated by Django 3.2.12 on 2022-04-13 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("octoprint", "0008_auto_20220413_1818"),
    ]

    operations = [
        migrations.AlterField(
            model_name="octoprintsettings",
            name="octoprint_install",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="settings",
                to="octoprint.octoprintinstall",
            ),
        ),
    ]
