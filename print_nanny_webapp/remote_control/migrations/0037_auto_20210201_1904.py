# Generated by Django 3.1.3 on 2021-02-02 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("remote_control", "0036_printerprofile_volume_custom_box"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="octoprintdevice",
            name="private_key",
        ),
        migrations.AlterField(
            model_name="octoprintdevice",
            name="public_key",
            field=models.TextField(),
        ),
    ]
