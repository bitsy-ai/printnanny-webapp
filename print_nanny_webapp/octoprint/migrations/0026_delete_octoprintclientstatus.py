# Generated by Django 3.2.12 on 2022-11-15 07:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("octoprint", "0025_octoprintgcodeevent"),
    ]

    operations = [
        migrations.DeleteModel(
            name="OctoPrintClientStatus",
        ),
    ]
