from rest_framework import serializers
from djstripe.models.billing import (
    Subscription,
    Plan,
    SubscriptionSchedule,
)
from djstripe.models.core import Product, Price, Event, Customer, Charge
from djstripe.models.payment_methods import PaymentMethod
from djstripe import settings as djstripe_settings
from djstripe.utils import convert_tstamp
import stripe

from print_nanny_webapp.users.api.serializers import UserSerializer


class StripeSubscriptionSchedule(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionSchedule
        fields = "__all__"


class StripePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        # exclude a few enums we don't use, which have problematic presentations in strongly-typed languages like rust
        exclude = (
            "aggregate_usage",
            "billing_scheme",
            "tiers_mode",
        )


class StripePaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = "__all__"


class StripeSubscriptionSerializer(serializers.ModelSerializer):
    plan = StripePlanSerializer()
    default_payment_method = StripePaymentMethodSerializer()
    schedule = StripeSubscriptionSchedule()

    is_period_current = serializers.BooleanField()
    is_status_current = serializers.BooleanField()
    is_status_temporarily_current = serializers.BooleanField()
    is_valid = serializers.BooleanField()  # type: ignore

    class Meta:
        model = Subscription
        fields = "__all__"


class StripeChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charge
        fields = "__all__"


class StripeEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class StripeDateTimeFieldSerializer(serializers.DateTimeField):
    def to_native(self, value):
        if value is not None:
            return convert_tstamp(value)

    def to_representation(self, value):
        if type(value) is int:
            value = self.to_native(value)
        return super().to_representation(value)


class StripeCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Customer


class BillingSummarySerializer(serializers.Serializer):
    subscription = StripeSubscriptionSerializer(required=False)
    customer = StripeCustomerSerializer()
    user = UserSerializer(allow_null=True, required=False)

    billing_portal_url = serializers.SerializerMethodField()

    def get_billing_portal_url(self, obj) -> str:
        stripe.api_key = djstripe_settings.djstripe_settings.STRIPE_SECRET_KEY
        session = stripe.billing_portal.Session.create(
            customer=obj["customer"].id,
            return_url="https://printnanny.ai/billing",
        )
        return session.url


class BillingPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = "__all__"


class BillingProductSerializer(serializers.ModelSerializer):

    prices = BillingPriceSerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"
