# Generated by Django 3.1.7 on 2021-04-27 03:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("remote_control", "0061_auto_20210425_2253"),
    ]

    operations = [
        migrations.CreateModel(
            name="GeeksToken",
            fields=[
                ("key", models.UUIDField(primary_key=True, serialize=False)),
                (
                    "octoprint_device",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="remote_control.octoprintdevice",
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
                "verbose_name": "GeeksToken",
                "verbose_name_plural": "GeeksTokens",
                "abstract": False,
            },
        ),
    ]
