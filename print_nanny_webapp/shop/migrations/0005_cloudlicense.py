# Generated by Django 3.2.12 on 2023-02-03 23:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("djstripe", "0010_alter_customer_balance"),
        ("devices", "0059_webrtcstream_mountpoint"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("shop", "0004_product_stripe_product_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="CloudLicense",
            fields=[
                ("deleted", models.DateTimeField(editable=False, null=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("created_dt", models.DateTimeField(auto_now_add=True)),
                ("updated_dt", models.DateTimeField(auto_now=True)),
                (
                    "pi",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="devices.pi",
                    ),
                ),
                (
                    "stripe_customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="djstripe.customer",
                    ),
                ),
                (
                    "stripe_subscription",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="djstripe.subscription",
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