# Generated by Django 3.2.12 on 2023-03-27 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("djstripe", "0011_2_7"),
        ("shop", "0005_cloudlicense"),
    ]

    operations = [
        migrations.AddField(
            model_name="cloudlicense",
            name="deleted_by_cascade",
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name="inventoryitem",
            name="deleted_by_cascade",
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name="order",
            name="deleted_by_cascade",
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name="orderstatus",
            name="deleted_by_cascade",
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name="product",
            name="deleted_by_cascade",
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name="cloudlicense",
            name="deleted",
            field=models.DateTimeField(db_index=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="inventoryitem",
            name="deleted",
            field=models.DateTimeField(db_index=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="deleted",
            field=models.DateTimeField(db_index=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="djstripe_customer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="shop_order",
                to="djstripe.customer",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="djstripe_payment_intent",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="shop_order",
                to="djstripe.paymentintent",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="djstripe_subscription",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="shop_order",
                to="djstripe.subscription",
            ),
        ),
        migrations.AlterField(
            model_name="orderstatus",
            name="deleted",
            field=models.DateTimeField(db_index=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="deleted",
            field=models.DateTimeField(db_index=True, editable=False, null=True),
        ),
    ]
