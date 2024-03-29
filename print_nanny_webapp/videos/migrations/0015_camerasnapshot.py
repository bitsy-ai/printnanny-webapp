# Generated by Django 4.1.7 on 2023-03-30 17:34

from django.db import migrations, models
import django.db.models.deletion
import print_nanny_webapp.videos.models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("devices", "0061_alter_pinatsapp_organization_and_more"),
        ("videos", "0014_videorecording_finalize_task_id_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CameraSnapshot",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("created_dt", models.DateTimeField(auto_now_add=True)),
                (
                    "image",
                    models.FileField(
                        upload_to=print_nanny_webapp.videos.models.snapshot_filepath
                    ),
                ),
                (
                    "pi",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="camera_snapshots",
                        to="devices.pi",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_dt"],
                "index_together": {("id", "pi", "created_dt")},
            },
        ),
    ]
