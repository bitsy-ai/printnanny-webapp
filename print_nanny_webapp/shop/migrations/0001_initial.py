# Generated by Django 3.2.12 on 2022-09-01 07:24

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("djstripe", "0010_alter_customer_balance"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("sku", models.CharField(max_length=255)),
                ("slug", models.CharField(max_length=64)),
                ("unit_label", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("description", models.CharField(max_length=255)),
                ("statement_descriptor", models.CharField(max_length=255)),
                (
                    "images",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=255),
                        default=list,
                        size=None,
                    ),
                ),
                ("is_active", models.BooleanField(default=False)),
                ("is_shippable", models.BooleanField()),
                ("is_preorder", models.BooleanField()),
                ("is_subscription", models.BooleanField()),
                (
                    "stripe_price_lookup_key",
                    models.CharField(max_length=255, null=True),
                ),
                (
                    "djstripe_product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="djstripe.product",
                    ),
                ),
            ],
            options={
                "index_together": {
                    ("id", "stripe_price_lookup_key", "djstripe_product"),
                    ("id", "sku", "name", "created_dt"),
                    (
                        "id",
                        "is_active",
                        "is_shippable",
                        "is_preorder",
                        "is_subscription",
                    ),
                },
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                ("deleted", models.DateTimeField(editable=False, null=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("created_dt", models.DateTimeField(auto_now_add=True)),
                ("email", models.EmailField(max_length=254)),
                (
                    "djstripe_checkout_session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="djstripe.session",
                    ),
                ),
                (
                    "djstripe_customer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="djstripe.customer",
                    ),
                ),
                (
                    "djstripe_payment_intent",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="djstripe.paymentintent",
                    ),
                ),
                ("products", models.ManyToManyField(to="shop.Product")),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_dt"],
                "index_together": {
                    (
                        "id",
                        "email",
                        "djstripe_customer",
                        "djstripe_checkout_session",
                        "djstripe_payment_intent",
                    )
                },
            },
        ),
        migrations.CreateModel(
            name="OrderStatus",
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
                ("created_dt", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("checkout_session_created", "Checkout session created"),
                            (
                                "checkout_session_completed",
                                "Checkout session completed",
                            ),
                            ("checkout_session_expired", "Checkout session expired"),
                            (
                                "checkout_session_success",
                                "Added PaymentIntent to checkout session",
                            ),
                            ("processing", "Order is being proccessed"),
                            ("ready_to_ship", "Order is ready to ship"),
                            ("shipped", "Order has been passed shipping service"),
                            ("goods_fulfilled", "Physical goods order fulfilled"),
                            (
                                "service_fulfilled",
                                "Electronic service or subscription fulfilled",
                            ),
                            ("refund_requested", "Refund requested"),
                            ("refund_granted", "Refund granted"),
                        ],
                        max_length=32,
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="shop.order"
                    ),
                ),
            ],
            options={
                "ordering": ["-created_dt"],
                "index_together": {("id", "created_dt", "order", "status")},
            },
        ),
        migrations.CreateModel(
            name="InventoryItem",
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
                    "order",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shop.order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="shop.product"
                    ),
                ),
            ],
            options={
                "ordering": ["-created_dt"],
                "index_together": {
                    ("id", "created_dt", "updated_dt", "order", "product")
                },
            },
        ),
    ]
