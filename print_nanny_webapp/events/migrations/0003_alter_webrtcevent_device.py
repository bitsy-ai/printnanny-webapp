# Generated by Django 3.2.12 on 2022-02-19 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("devices", "0005_auto_20220217_2202"),
        ("events", "0002_auto_20220218_1943"),
    ]

    operations = [
        migrations.AlterField(
            model_name="webrtcevent",
            name="device",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="events",
                to="devices.device",
            ),
        ),
    ]
