from rest_framework import serializers
from djstripe.models.core import Product as DjstripeProduct

from print_nanny_webapp.shop.models import Product


class DjStripeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjstripeProduct
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    djstripe_product = DjStripeProductSerializer()

    class Meta:
        model = Product
        fields = "__all__"


# class BillingCheckoutSessionSerializer(serializers.Serializer):
#     stripe_price_lookup_key = serializers.CharField()
#     email = serializers.EmailField()
#     url = serializers.URLField(read_only=True)


# class StripeCheckoutSessionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Session
#         fields = "__all__"


# class StripeCheckoutSuccessSerializer(serializers.Serializer):
#     stripe_checkout_session_id = serializers.CharField()
#     stripe_session = StripeCheckoutSessionSerializer(read_only=True)
#     stripe_customer = StripeCustomerSerializer(read_only=True)
