import logging
from uuid import uuid4

from django.db import models
from safedelete.models import SafeDeleteModel
from print_nanny_webapp.shop.enum import OrderStatusType

logger = logging.getLogger(__name__)


class Product(SafeDeleteModel):
    """
    Product listed for sale in PrintNanny's shop. Can be a physical (shippable) good, one-time electronic service, or recurring electronic subscription
    """

    id = models.UUIDField(primary_key=True, default=uuid4)

    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    sku = models.CharField(max_length=255)
    unit_label = models.CharField(max_length=255)

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    statement_descriptor = models.CharField(max_length=255)

    # is the product visible in shop list view?
    is_active = models.BooleanField(default=False)
    # is the product a physical good?
    is_shippable = models.BooleanField()
    # is the product a pre-order or should existing stock be used to calculate availability?
    is_preorder = models.BooleanField()
    # is the product an electronic subscription?
    is_subscription = models.BooleanField()

    stripe_price_lookup_key = models.CharField(null=True, max_length=255)
    djstripe_product = models.ForeignKey("djstripe.Product", on_delete=models.CASCADE)


class Order(SafeDeleteModel):
    """
    A customer order (shopping cart) for one or more pieces of inventory
    """

    id = models.UUIDField(primary_key=True, default=uuid4)

    djstripe_customer = models.ForeignKey("djstripe.Customer", on_delete=models.CASCADE)

    # Session.display_items will contain the contents of this order
    djstripe_checkout_session = models.ForeignKey(
        "djstripe.Session", on_delete=models.CASCADE
    )
    djstripe_payment_intent = models.ForeignKey(
        "djstripe.PaymentIntent", on_delete=models.CASCADE, null=True
    )


class OrderStatus(SafeDeleteModel):
    created_dt = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(choices=OrderStatusType.choices, max_length=32)


class InventoryItem(SafeDeleteModel):
    """
    A piece of product inventory with a limited quantity
    """

    id = models.UUIDField(primary_key=True, default=uuid4)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
