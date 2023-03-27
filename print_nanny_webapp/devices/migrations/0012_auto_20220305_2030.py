# Generated by Django 3.2.12 on 2022-03-05 20:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("devices", "0011_auto_20220226_2219"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="cloudiotdevice",
            name="unique_cloud_iot_device_per_device",
        ),
        migrations.AddConstraint(
            model_name="cloudiotdevice",
            constraint=models.UniqueConstraint(
                condition=models.Q(("deleted", None)),
                fields=("device",),
                name="unique_cloud_iot_device_per_device",
            ),
        ),
    ]
