# Generated by Django 3.2.12 on 2022-07-30 20:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("devices", "0034_auto_20220730_2020"),
    ]

    operations = [
        migrations.AddField(
            model_name="pi",
            name="sbc",
            field=models.CharField(
                choices=[("rpi_4", "Raspberry Pi 4")], default="rpi_4", max_length=32
            ),
        ),
    ]
