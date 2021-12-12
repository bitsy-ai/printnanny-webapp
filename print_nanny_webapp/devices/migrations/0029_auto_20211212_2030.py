# Generated by Django 3.2.9 on 2021-12-12 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("devices", "0028_license_updated_dt"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="camera",
            name="camera_source",
        ),
        migrations.AlterField(
            model_name="camera",
            name="camera_type",
            field=models.CharField(
                choices=[
                    ("picam", "Raspberry Pi Camera Module"),
                    ("usb", "USB Camera (coming soon)"),
                    ("ip", "Generic RTP/RTSP IP Camera (coming soon)"),
                ],
                default=[
                    ("picam", "Raspberry Pi Camera Module"),
                    ("usb", "USB Camera (coming soon)"),
                    ("ip", "Generic RTP/RTSP IP Camera (coming soon)"),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="camera",
            name="name",
            field=models.CharField(default="Raspberry Pi Cam", max_length=255),
        ),
    ]
