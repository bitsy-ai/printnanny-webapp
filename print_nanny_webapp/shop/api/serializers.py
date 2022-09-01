from rest_framework import serializers
from djstripe.models.core import (
    Product as DjstripeProduct,
    Customer as DjStripeCustomer,
    PaymentIntent as DjStripePaymentIntent,
    Price as DjStripePrice,
)
from djstripe.models.checkout import Session as DjStripeCheckoutSession

from print_nanny_webapp.shop.models import Order, Product
from print_nanny_webapp.shop.services import create_stripe_checkout_session


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


class DjStripePaymentIntentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjStripePaymentIntent
        fields = "__all__"


class DjStripePriceSerializer(serializers.ModelSerializer):
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
    stripe_checkout_session_url = serializers.CharField(read_only=True)

    class Meta:
        model = Order
        fields = ("products", "email", "stripe_checkout_session_url")

    def create(self, validated_data):
        request = self.context["request"]
        email = validated_data["email"]
        product_ids = validated_data["products"]
        django_session = request.session._get_or_create_session_key()
        products = Product.objects.get(id__in=product_ids)
        checkout_session = create_stripe_checkout_session(
            request, django_session, products
        )


class OrderSerializer(serializers.ModelSerializer):
    djstripe_customer = DjStripeCustomerSerializer(read_only=True)
    djstripe_checkout_session = DjStripeCheckoutSessionSerializer(read_only=True)
    djstripe_payment_intent = DjStripePaymentIntentSerializer(read_only=True)
    products = ProductSerializer(read_only=True, many=True)
    id = serializers.UUIDField(read_only=True)

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
