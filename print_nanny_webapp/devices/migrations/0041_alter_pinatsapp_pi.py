# Generated by Django 3.2.12 on 2022-08-17 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("devices", "0040_auto_20220814_1552"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pinatsapp",
            name="pi",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="nats_apps",
                to="devices.pi",
            ),
        ),
    ]
