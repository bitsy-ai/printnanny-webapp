# Generated by Django 3.2.12 on 2023-01-09 00:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("devices", "0052_auto_20221105_1957"),
    ]

    operations = [
        migrations.DeleteModel(
            name="PiSettings",
        ),
    ]
