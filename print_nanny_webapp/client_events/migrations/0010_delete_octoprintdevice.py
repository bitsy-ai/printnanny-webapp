# Generated by Django 3.1.3 on 2020-12-30 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("remote_control", "0007_auto_20201229_2309"),
        ("client_events", "0009_auto_20201228_1434"),
    ]

    operations = [
        migrations.DeleteModel(
            name="OctoPrintDevice",
        ),
    ]
