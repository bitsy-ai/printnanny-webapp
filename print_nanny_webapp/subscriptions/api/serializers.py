from rest_framework import serializers
from djstripe.models.billing import Subscription, Invoice
from djstripe.models.core import Event, Customer, Charge

from print_nanny_webapp.users.api.serializers import UserSerializer


class StripeSubscriptionSerializer(serializers.ModelSerializer):
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


class StripeInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = "__all__"


class StripeCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Customer


class BillingSummarySerializer(serializers.Serializer):
    subscriptions = StripeSubscriptionSerializer(many=True)
    charge_history = StripeChargeSerializer(many=True)
    events = StripeEventSerializer(many=True)
    next_invoice = StripeInvoiceSerializer(allow_null=True, required=False)
    customer = StripeCustomerSerializer()
    user = UserSerializer(allow_null=True, required=False)
