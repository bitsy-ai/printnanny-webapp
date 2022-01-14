# Generated by Django 3.2.7 on 2021-11-14 05:15

from django.db import migrations, models
import django.db.models.deletion
import print_nanny_webapp.devices.models


class Migration(migrations.Migration):

    dependencies = [
        # ("releases", "0002_auto_20211031_1735"),
        ("devices", "0005_auto_20211113_2227"),
    ]

    operations = [
        migrations.AddField(
            model_name="deviceinfo",
            name="machine_id",
            field=models.CharField(default="123abc", max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="device",
            name="bootstrap_release",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="releases.release",
            ),
        ),
        migrations.AddConstraint(
            model_name="deviceinfo",
            constraint=models.UniqueConstraint(
                condition=models.Q(("deleted", None)),
                fields=("device",),
                name="unique_device_info_per_device",
            ),
        ),
    ]
