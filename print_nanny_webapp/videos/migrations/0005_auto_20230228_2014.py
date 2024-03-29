# Generated by Django 3.2.12 on 2023-02-28 20:14

from django.db import migrations, models
import django.db.models.deletion
import print_nanny_webapp.videos.models


class Migration(migrations.Migration):
    dependencies = [
        ("videos", "0004_rename_uuid_videorecording_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="videorecording",
            name="cloud_sync_end",
        ),
        migrations.RemoveField(
            model_name="videorecording",
            name="cloud_sync_start",
        ),
        migrations.RemoveField(
            model_name="videorecording",
            name="cloud_sync_status",
        ),
        migrations.RemoveField(
            model_name="videorecording",
            name="recording_status",
        ),
        migrations.AddField(
            model_name="videorecording",
            name="capture_done",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="videorecording",
            name="cloud_sync_done",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="videorecording",
            name="combine_done",
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name="VideoRecordingPart",
            fields=[
                ("deleted", models.DateTimeField(editable=False, null=True)),
                (
                    "id",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("part", models.IntegerField()),
                ("size", models.BigIntegerField()),
                (
                    "mp4_file",
                    models.FileField(
                        null=True,
                        upload_to=print_nanny_webapp.videos.models.part_mp4_filepath,
                    ),
                ),
                (
                    "video_recording",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="videos.videorecording",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
