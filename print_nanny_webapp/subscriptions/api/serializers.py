from django.db import models
from rest_framework import serializers
from djstripe.models.billing import (
    Subscription,
    UpcomingInvoice,
    Plan,
    SubscriptionSchedule,
)
from djstripe.models.core import Event, Customer, Charge
from djstripe.models.payment_methods import PaymentMethod
from djstripe.fields import StripeDateTimeField
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
        fields = "__all__"


class StripePaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = "__all__"


class StripeSubscriptionSerializer(serializers.ModelSerializer):
    plan = StripePlanSerializer()
    default_payment_method = StripePaymentMethodSerializer()
    schedule = StripeSubscriptionSchedule()

    is_period_current = serializers.BooleanField
    is_status_current = serializers.BooleanField
    is_status_temporarily_current = serializers.BooleanField
    is_valid = serializers.BooleanField  # type: ignore

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


from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import is_protected_type, smart_str


class InvoiceSlugRelatedField(serializers.RelatedField):
    """
    UpcomingInvoice has no database rows to reverse on
    """

    default_error_messages = {
        "does_not_exist": "Object with {slug_name}={value} does not exist.",
        "invalid": "Invalid value.",
    }

    def __init__(self, slug_field=None, **kwargs):
        assert slug_field is not None, "The `slug_field` argument is required."
        self.slug_field = slug_field
        super().__init__(**kwargs)

    def to_internal_value(self, data):
        queryset = self.get_queryset()
        try:
            return queryset.get(**{self.slug_field: data})
        except ObjectDoesNotExist:
            self.fail(
                "does_not_exist", slug_name=self.slug_field, value=smart_str(data)
            )
        except (TypeError, ValueError):
            self.fail("invalid")

    def to_representation(self, obj):
        return obj


class StripeNextInvoiceSerializer(serializers.ModelSerializer):
    serializer_field_mapping = serializers.ModelSerializer.serializer_field_mapping
    serializer_field_mapping[StripeDateTimeField] = StripeDateTimeFieldSerializer  # type: ignore
    serializer_field_mapping[stripe.stripe_object.StripeObject] = serializers.JSONField  # type: ignore
    serializer_field_mapping[
        stripe.api_resources.list_object.ListObject
    ] = serializers.JSONField  # type: ignore
    serializer_related_to_field = InvoiceSlugRelatedField  # type: ignore

    class Meta:
        model = UpcomingInvoice
        fields = "__all__"


class StripeCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Customer


class BillingSummarySerializer(serializers.Serializer):
    subscription = StripeSubscriptionSerializer()
    charges = StripeChargeSerializer(many=True)
    events = StripeEventSerializer(many=True)
    next_invoice = StripeNextInvoiceSerializer(allow_null=True, required=False)
    customer = StripeCustomerSerializer()
    user = UserSerializer(allow_null=True, required=False)

    billing_portal_url = serializers.SerializerMethodField()

    def get_billing_portal_url(self, obj) -> str:
        session = stripe.billing_portal.Session.create(
            customer=obj["customer"].id,
            return_url="https://printnanny.ai/billing",
        )
        return session.url
