# Generated by Django 3.2.12 on 2023-03-15 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("videos", "0008_auto_20230302_1004"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="videorecordingpart",
            name="buffer_duration",
        ),
        migrations.RemoveField(
            model_name="videorecordingpart",
            name="buffer_offset",
        ),
        migrations.RemoveField(
            model_name="videorecordingpart",
            name="buffer_offset_end",
        ),
        migrations.RemoveField(
            model_name="videorecordingpart",
            name="buffer_streamtime",
        ),
        migrations.RemoveField(
            model_name="videorecordingpart",
            name="buffer_ts",
        ),
    ]
