# Generated by Django 3.2.12 on 2022-02-25 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("devices", "0007_janusstream_unique_port"),
    ]

    operations = [
        migrations.RenameField(
            model_name="janusstream",
            old_name="port",
            new_name="rtp_port",
        ),
    ]
