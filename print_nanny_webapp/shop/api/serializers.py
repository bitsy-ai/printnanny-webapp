from rest_framework import serializers
from djstripe.models.core import (
    Product as DjstripeProduct,
    Customer as DjStripeCustomer,
)

from print_nanny_webapp.shop.models import Order, Product


class DjStripeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjstripeProduct
        fields = "__all__"


class DjStripeCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjStripeCustomer
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    djstripe_product = DjStripeProductSerializer()

    class Meta:
        model = Product
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    # provided by client to initialize Stripe checkout session
    stripe_price_lookup_key = serializers.CharField()
    email = serializers.EmailField()
    # created server-side
    djstripe_customer = DjStripeCustomerSerializer(read_only=True)
    # djstripe_checkout_session = DjStripeCheckoutSession(read_only=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "created_dt",
            "djstripe_customer",
            "djstripe_checkout_session",
            "djstripe_payment_intent",
            "last_status",
            "email",
            "stripe_price_lookup_key",
        )


# class BillingCheckoutSessionSerializer(serializers.Serializer):

#     url = serializers.URLField(read_only=True)


# class StripeCheckoutSessionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Session
#         fields = "__all__"


# class StripeCheckoutSuccessSerializer(serializers.Serializer):
#     stripe_checkout_session_id = serializers.CharField()
#     stripe_session = StripeCheckoutSessionSerializer(read_only=True)
#     stripe_customer = StripeCustomerSerializer(read_only=True)
