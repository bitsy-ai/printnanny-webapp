# Generated by Django 3.2.12 on 2022-08-20 18:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("devices", "0041_alter_pinatsapp_pi"),
    ]

    operations = [
        migrations.AddField(
            model_name="webrtcstream",
            name="info",
            field=models.JSONField(default=dict),
        ),
    ]
