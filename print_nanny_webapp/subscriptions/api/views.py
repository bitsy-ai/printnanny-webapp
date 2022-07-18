from pyrsistent import m
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from djstripe.models.billing import Subscription
from djstripe.enums import SubscriptionStatus

from print_nanny_webapp.subscriptions.api.serializers import BillingSummarySerializer
from print_nanny_webapp.utils.api.views import generic_get_errors
from print_nanny_webapp.subscriptions.services import (
    get_stripe_subscription,
    get_stripe_charges,
    get_stripe_customer,
    get_stripe_next_invoice,
    get_stripe_subscription_events,
)


@extend_schema_view(
    tags=["billing"],
    get=extend_schema(
        responses={200: BillingSummarySerializer(many=False)} | generic_get_errors
    ),
)
class BillingSummaryView(APIView):
    def get(self, request, **kwargs):
        stripe_customer = get_stripe_customer(request.user)
        subscription = get_stripe_subscription(stripe_customer)
        charges = get_stripe_charges(stripe_customer)
        events = get_stripe_subscription_events(stripe_customer)
        if subscription.status != SubscriptionStatus.canceled:
            next_invoice = get_stripe_next_invoice(stripe_customer, subscription)
        else:
            next_invoice = None
        serializer = BillingSummarySerializer(
            instance=dict(
                subscription=subscription,
                charges=charges,
                events=events,
                next_invoice=next_invoice,
                user=request.user,
                customer=stripe_customer,
            )
        )
        return Response(serializer.data)


@extend_schema_view(
    tags=["billing"],
    post=extend_schema(
        parameters=[
            OpenApiParameter(
                name="subscription_id", type=int, location=OpenApiParameter.PATH
            )
        ],
        responses={201: BillingSummarySerializer(many=False)},
    ),
)
class BillingCancelView(APIView):
    def post(self, request, subscription_id=None):
        subscription = Subscription.objects.get(id=subscription_id)
        subscription.cancel(at_period_end=True)
        stripe_customer = get_stripe_customer(request.user)
        charges = get_stripe_charges(stripe_customer)
        events = get_stripe_subscription_events(stripe_customer)
        if subscription.status != SubscriptionStatus.canceled:
            next_invoice = get_stripe_next_invoice(stripe_customer, subscription)
        else:
            next_invoice = None
        serializer = BillingSummarySerializer(
            instance=dict(
                subscription=subscription,
                charges=charges,
                events=events,
                next_invoice=next_invoice,
                user=request.user,
                customer=stripe_customer,
            )
        )
        return Response(serializer.data)


@extend_schema_view(
    tags=["billing"],
    post=extend_schema(
        parameters=[
            OpenApiParameter(
                name="subscription_id", type=str, location=OpenApiParameter.PATH
            )
        ],
        responses={201: BillingSummarySerializer(many=False)},
    ),
)
class BillingReactivateView(APIView):
    def post(self, request, subscription_id=None):
        subscription = Subscription.objects.get(id=subscription_id)
        subscription.reactivate()
        stripe_customer = get_stripe_customer(request.user)
        charges = get_stripe_charges(stripe_customer)
        events = get_stripe_subscription_events(stripe_customer)
        if subscription.status != SubscriptionStatus.canceled:
            next_invoice = get_stripe_next_invoice(stripe_customer, subscription)
        else:
            next_invoice = None
        serializer = BillingSummarySerializer(
            instance=dict(
                subscription=subscription,
                charges=charges,
                events=events,
                next_invoice=next_invoice,
                user=request.user,
                customer=stripe_customer,
            )
        )
        return Response(serializer.data)