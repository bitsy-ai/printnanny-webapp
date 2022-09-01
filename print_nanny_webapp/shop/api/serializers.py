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
