# Generated by Django 3.1.3 on 2020-12-28 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("client_events", "0005_octoprintdevice_print_nanny_client_version"),
    ]

    operations = [
        migrations.AddField(
            model_name="octoprintdevice",
            name="name",
            field=models.CharField(default="octoprint", max_length=255),
            preserve_default=False,
        ),
    ]
