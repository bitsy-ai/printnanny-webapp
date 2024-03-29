# Generated by Django 3.2.12 on 2022-02-25 06:09

from django.db import migrations, models


def dummy_default_janus_stream_port():
    return 5005


class Migration(migrations.Migration):
    dependencies = [
        ("devices", "0005_auto_20220217_2202"),
    ]

    operations = [
        migrations.AddField(
            model_name="janusstream",
            name="port",
            field=models.PositiveSmallIntegerField(
                default=dummy_default_janus_stream_port
            ),
        ),
    ]
