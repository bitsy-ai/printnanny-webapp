# Generated by Django 3.2.12 on 2022-09-02 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderstatus",
            name="status",
            field=models.CharField(
                choices=[
                    ("checkout_session_created", "Checkout session created"),
                    ("checkout_session_completed", "Checkout session completed"),
                    ("checkout_session_expired", "Checkout session expired"),
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
    ]