# Generated by Django 3.1.3 on 2021-02-06 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("remote_control", "0039_auto_20210202_0057"),
    ]

    operations = [
        migrations.AddField(
            model_name="octoprintdevice",
            name="configs",
            field=models.JSONField(default=[]),
        ),
    ]
