import logging
from uuid import uuid4
from typing import Optional, List

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from djstripe.models import Product as DjstripeProduct
from safedelete.models import SafeDeleteModel, SafeDeleteManager
from print_nanny_webapp.shop.enum import OrderStatusType

logger = logging.getLogger(__name__)

User = get_user_model()


class ProductManager(SafeDeleteManager):
    def create(self, **kwargs):

        stripe_product_id = kwargs.get("stripe_product_id")
        if stripe_product_id is None:
            raise ValueError("stripe_product_id is required")

        djstripe_product = DjstripeProduct.objects.get(id=stripe_product_id)
        return super().create(djstripe_product=djstripe_product, **kwargs)


class Product(SafeDeleteModel):
    """
    Product listed for sale in PrintNanny's shop. Can be a physical (shippable) good, one-time electronic service, or recurring electronic subscription
    """

    objects = ProductManager()

    class Meta:
        index_together = [
            [
                "id",
                "sku",
                "name",
                "created_dt",
            ],
            [
                "id",
                "is_active",
                "is_shippable",
                "is_preorder",
                "is_subscription",
            ],
            ["id", "stripe_price_lookup_key", "djstripe_product"],
        ]

    id = models.UUIDField(primary_key=True, default=uuid4)

    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    sku = models.CharField(max_length=255)
    slug = models.CharField(max_length=64)
    unit_label = models.CharField(max_length=255)

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    statement_descriptor = models.CharField(max_length=255)
    images = ArrayField(models.CharField(max_length=255), default=list)

    # is the product visible in shop list view?
    is_active = models.BooleanField(default=False)
    # is the product a physical good?
    is_shippable = models.BooleanField()
    # is the product a pre-order or should existing stock be used to calculate availability?
    is_preorder = models.BooleanField()
    # is the product an electronic subscription?
    is_subscription = models.BooleanField()

    stripe_price_lookup_key = models.CharField(null=True, max_length=255)

    stripe_product_id = models.CharField(unique=True, max_length=255, null=True)

    djstripe_product = models.ForeignKey("djstripe.Product", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):

        stripe_product_id = kwargs.get("stripe_product_id")
        if stripe_product_id is None:
            super().save(*args, **kwargs)
        else:
            djstripe_product = DjstripeProduct.objects.get(id=stripe_product_id)
            return super().save(djstripe_product=djstripe_product, *args, **kwargs)

    @property
    def prices(self):
        return self.djstripe_product.prices


class OrderStatus(SafeDeleteModel):
    class Meta:
        ordering = ["-created_dt"]
        index_together = [["id", "created_dt", "order", "status"]]

    created_dt = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey("shop.Order", on_delete=models.CASCADE)
    status = models.CharField(choices=OrderStatusType.choices, max_length=32)


class Order(SafeDeleteModel):
    """
    A customer order (shopping cart) for one or more pieces of inventory
    """

    class Meta:
        ordering = ["-created_dt"]

        index_together = [
            [
                "id",
                "email",
                "djstripe_customer",
                "djstripe_checkout_session",
                "djstripe_payment_intent",
            ]
        ]

    id = models.UUIDField(primary_key=True, default=uuid4)
    created_dt = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()

    # The contents of this order according to our shop Product data model
    products = models.ManyToManyField(Product)

    # Session.display_items will contain the contents of this order with ref to Stripe's data model
    djstripe_checkout_session = models.ForeignKey(
        "djstripe.Session", on_delete=models.CASCADE
    )

    # relationship created when handling checkout.session.completed
    djstripe_customer = models.ForeignKey(
        "djstripe.Customer", on_delete=models.CASCADE, null=True
    )
    # relationship created when handling checkout.session.completed
    djstripe_payment_intent = models.ForeignKey(
        "djstripe.PaymentIntent", on_delete=models.CASCADE, null=True
    )

    # relationship created when handling checkout.session.complete (if subscription)
    djstripe_subscription = models.ForeignKey(
        "djstripe.Subscription", on_delete=models.CASCADE, null=True
    )
    # will be null if order is created while not logged in, but can be reconciled
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    @property
    def last_status(self) -> Optional[OrderStatus]:
        return self.orderstatus_set.first()

    @property
    def status_history(self) -> List[OrderStatus]:
        return self.orderstatus_set

    @property
    def is_subscription(self) -> bool:
        """
        True if any product in order is a subscription
        Note: Order can contain more than 1 product
        """
        return self.products.filter(is_subscription=True).count() > 0

    @property
    def is_shippable(self) -> bool:
        """
        True if any product in order is a shippable physical good
        Note: Order can contain more than 1 product
        """
        return self.products.filter(is_shippable=True).count() > 0

    @property
    def receipt_url(self) -> Optional[str]:
        """
        For orders with a PaymentIntent (mode=payment), link to pay.stripe.com receipt
        Note: this field will be None for subscriptions, which use a portal url instead
        """
        if self.is_shippable and self.djstripe_payment_intent:
            return self.djstripe_payment_intent.charges.first().receipt_url

        return None

    @property
    def portal_url(self) -> Optional[str]:
        """
        Link to https://stripe.com/docs/customer-management Stripe Customer portal
        """
        if self.is_subscription:
            return settings.STRIPE_PORTAL_URL
        return None


class InventoryItem(SafeDeleteModel):
    """
    A piece of product inventory with a limited quantity.

    An InventoryItem will be associated with an order when Stripe's checkout.success event is received.

    If the product is shippable, the product should be marked unavailable if no unassoicated InventoryItems exist
    unless the product is a pre-order, in which case the InventoryItem will be created for later fulfillment
    """

    class Meta:
        ordering = ["-created_dt"]
        index_together = [["id", "created_dt", "updated_dt", "order", "product"]]

    id = models.UUIDField(primary_key=True, default=uuid4)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
