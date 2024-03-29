# Generated by Django 3.1.7 on 2021-05-11 04:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("telemetry", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="octoprintpluginevent",
            name="event_type",
            field=models.CharField(
                choices=[
                    ("device_register_start", "Device registration started"),
                    ("device_register_done", "Device registration succeeded"),
                    ("device_register_failed", "Device registration failed"),
                    ("printer_profile_sync_start", "Printer profile sync started"),
                    ("printer_profile_sync_done", "Printer profile sync succeeded"),
                    ("printer_profile_sync_failed", "Printer profile sync failed"),
                    ("connect_test_rest_api", "Test connection to REST API"),
                    (
                        "connect_test_rest_api_failed",
                        "Test connection to REST API failed",
                    ),
                    (
                        "connect_test_rest_api_success",
                        "Test connection to REST API success",
                    ),
                    ("connect_test_mqtt_ping", "Test connection to REST API"),
                    (
                        "connect_test_mqtt_ping_failed",
                        "Test connection to REST API failed",
                    ),
                    (
                        "connect_test_mqtt_ping_success",
                        "Test connection to REST API success",
                    ),
                ],
                db_index=True,
                max_length=255,
            ),
        ),
    ]
