# Generated by Django 3.2.12 on 2022-04-13 18:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("octoprint", "0009_alter_octoprintsettings_octoprint_install"),
    ]

    operations = [
        migrations.AddField(
            model_name="octoprinterprofile",
            name="created_dt",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="octoprinterprofile",
            name="updated_dt",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
