# Generated by Django 3.1.3 on 2021-01-17 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("alerts", "0014_auto_20210116_1551"),
    ]

    operations = [
        migrations.CreateModel(
            name="RemoteControlCommandAlertSettings",
            fields=[
                (
                    "alertsettings_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="alerts.alertsettings",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("alerts.alertsettings",),
        ),
        migrations.RemoveField(
            model_name="defectalertsettings",
            name="device",
        ),
        migrations.RemoveField(
            model_name="progressalertsettings",
            name="device",
        ),
    ]
