import logging
from uuid import uuid4
from django.db import models
from django.db.models import UniqueConstraint
from django.utils.http import urlencode
from django.urls import reverse
from django.contrib.sites.models import Site


from safedelete.models import SafeDeleteModel, SOFT_DELETE
from print_nanny_webapp.subscriptions.enum import ReferralCodeType, OrderStatusType


logger = logging.getLogger(__name__)


class MemberBadge(models.Model):
    class MemberBadgeType(models.TextChoices):

        FREE_BETA = (
            "FreeBeta",
            "Participated in free beta program",
        )
        PAID_BETA = (
            "PaidBeta",
            "Founding Members supported PrintNanny's development by pre-ordering an annual subscription",
        )

    class Meta:
        unique_together = ("type", "user")

    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
    type = models.CharField(choices=MemberBadgeType.choices, max_length=24)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="member_badges"
    )

    @property
    def label(self):
        return self.MemberBadgeType(self.type).label


class ReferralCode(SafeDeleteModel):
    """
    Generate a referral code
    """

    _safedelete_policy = SOFT_DELETE

    class Meta:
        index_together = (
            (
                "user",
                "created_dt",
                "code_type",
                "code",
            ),
        )
        constraints = [
            UniqueConstraint(
                fields=["code"],
                condition=models.Q(deleted=None),
                name="unique_referral_code",
            )
        ]

    created_dt = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="referral_codes"
    )
    code = models.CharField(max_length=255)
    code_type = models.CharField(
        max_length=32,
        default=ReferralCodeType.FOUNDING_MEMBER_TRIAL,
        choices=ReferralCodeType.choices,
    )

    def referral_url(self):
        domain = Site.objects.get_current().domain

        url_path = reverse("trial")
        q = urlencode({"code": self.code})
        return f"https://{domain}{url_path}?{q}"


class ReferralInvite(SafeDeleteModel):
    """
    Send referral code via email
    """

    class Meta:
        index_together = (
            (
                "email",
                "referrer",
            ),
        )
        constraints = [
            UniqueConstraint(
                fields=["email", "referrer"],
                condition=models.Q(deleted=None),
                name="unique_email_per_referrer",
            )
        ]

    created_dt = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    referrer = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="referral_invitations"
    )
    recipient = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        related_name="referral_invitations_recipient",
    )


class ReferralSignup(SafeDeleteModel):
    code = models.ForeignKey(
        ReferralCode,
        related_name="referral_signups",
        on_delete=models.CASCADE,
    )
    referrer = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="referral_signups_referrer"
    )
    recipient = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        related_name="referral_signups_recipient",
    )
    created_dt = models.DateTimeField(auto_now_add=True)


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
