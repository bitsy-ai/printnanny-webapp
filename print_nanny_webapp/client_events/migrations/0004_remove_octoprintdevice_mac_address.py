# Generated by Django 3.1.3 on 2020-12-28 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("client_events", "0003_auto_20201227_1417"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="octoprintdevice",
            name="mac_address",
        ),
    ]
