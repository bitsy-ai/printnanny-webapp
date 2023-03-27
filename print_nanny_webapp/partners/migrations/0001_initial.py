# Generated by Django 3.1.7 on 2021-05-04 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import print_nanny_webapp.partners.models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("remote_control", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="GeeksToken",
            fields=[
                ("deleted", models.DateTimeField(editable=False, null=True)),
                (
                    "key",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("verified", models.BooleanField(default=False)),
                (
                    "qrcode",
                    models.ImageField(
                        upload_to=print_nanny_webapp.partners.models._upload_to
                    ),
                ),
                (
                    "octoprint_device",
                    models.ForeignKey(
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
        ),
        migrations.AddConstraint(
            model_name="geekstoken",
            constraint=models.UniqueConstraint(
                condition=models.Q(deleted=None),
                fields=("octoprint_device_id",),
                name="unique_geeks_token_per_octoprint_device",
            ),
        ),
    ]
