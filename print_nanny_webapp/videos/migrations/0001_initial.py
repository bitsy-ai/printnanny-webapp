# Generated by Django 3.2.12 on 2023-01-12 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import print_nanny_webapp.videos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="VideoRecording",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("deleted", models.DateTimeField(editable=False, null=True)),
                ("start_dt", models.DateTimeField()),
                ("end_dt", models.DateTimeField()),
                ("name", models.CharField(max_length=255)),
                (
                    "mjr_recording",
                    models.FileField(
                        null=True,
                        upload_to=print_nanny_webapp.videos.models.mjr_recording_filepath,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]