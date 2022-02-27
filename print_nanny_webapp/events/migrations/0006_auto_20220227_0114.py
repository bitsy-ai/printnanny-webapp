# Generated by Django 3.2.12 on 2022-02-27 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0005_auto_20220224_0325"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="send_ws",
            field=models.BooleanField(
                default=True, help_text="Broadcast to events websocket: /ws/events"
            ),
        ),
        migrations.AddField(
            model_name="testevent",
            name="send_mqtt",
            field=models.BooleanField(
                default=True,
                help_text="Broadcast to mqtt topic: /devices/{device-id}/commands/",
            ),
        ),
        migrations.AddField(
            model_name="webrtcevent",
            name="mqtt",
            field=models.BooleanField(
                default=True,
                help_text="Broadcast to mqtt topic: /devices/{device-id}/commands/",
            ),
        ),
    ]
