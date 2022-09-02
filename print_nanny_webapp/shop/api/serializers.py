from typing import Any, Dict
from rest_framework import serializers
from djstripe.models.core import (
    Product as DjstripeProduct,
    Customer as DjStripeCustomer,
    PaymentIntent as DjStripePaymentIntent,
    Price as DjStripePrice,
    Charge as DjStripeCharge,
)
from djstripe.models.checkout import Session as DjStripeCheckoutSession
from djstripe.settings import djstripe_settings
import stripe

from print_nanny_webapp.shop.models import Order, Product
from print_nanny_webapp.shop.services import create_order


class DjStripeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjstripeProduct
        fields = "__all__"


class DjStripeCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjStripeCustomer
        fields = "__all__"


class DjStripeCheckoutSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjStripeCheckoutSession
        fields = "__all__"


class DjStripeChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjStripeCharge
        fields = "__all__"


class DjStripePaymentIntentSerializer(serializers.ModelSerializer):
    charges = DjStripeChargeSerializer(many=True, read_only=True)

    class Meta:
        model = DjStripePaymentIntent
        fields = "__all__"


class DjStripePriceSerializer(serializers.ModelSerializer):
    human_readable_price = serializers.CharField()

    class Meta:
        model = DjStripePrice
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    djstripe_product = DjStripeProductSerializer()
    prices = DjStripePriceSerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"


class OrderCheckoutSerializer(serializers.ModelSerializer):
    # provided by client to initialize Stripe checkout session
    email = serializers.EmailField()
    products = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Product.objects.all()
    )
    stripe_checkout_redirect_url = serializers.CharField(read_only=True)

    class Meta:
        model = Order
        fields = ("products", "email", "stripe_checkout_redirect_url")

    def create(self, validated_data):
        request = self.context["request"]
        email = validated_data["email"]
        products = validated_data["products"]
        if len(products) == 0:
            raise ValueError("Expected at least 1 product")
        if len(products) > 1:
            raise NotImplementedError(
                f"Checkout for more than 1 product is not implemented (received {len(product_ids)})"
            )

        product = products[0]
        return create_order(request, product, email)


class OrderSerializer(serializers.ModelSerializer):
    """
    Djstripe's representation of Stripe Checkout model is missing a number of fields, like subtotal amount and shipping/tax charges

    stripe_checkout_session_data is the raw JSON returned by stripe.checkout.Session.retrieve
    """

    djstripe_customer = DjStripeCustomerSerializer(read_only=True)
    djstripe_checkout_session = DjStripeCheckoutSessionSerializer(read_only=True)
    djstripe_payment_intent = DjStripePaymentIntentSerializer(read_only=True)
    products = ProductSerializer(read_only=True, many=True)
    id = serializers.UUIDField(read_only=True)

    stripe_checkout_redirect_url = serializers.CharField(read_only=True, required=False)

    stripe_checkout_session_data = serializers.SerializerMethodField()

    def get_stripe_checkout_session_data(self, obj) -> Dict[Any, Any]:
        stripe.api_key = djstripe_settings.STRIPE_SECRET_KEY
        return stripe.checkout.Session.retrieve(
            obj.djstripe_checkout_session.id,
            expand=["customer", "payment_intent", "line_items"],
        )

    class Meta:
        model = Order
        fields = (
            "id",
            "created_dt",
            "products",
            "djstripe_customer",
            "djstripe_checkout_session",
            "djstripe_payment_intent",
            "last_status",
            "email",
            "stripe_checkout_redirect_url",
            "stripe_checkout_session_data",
        )
