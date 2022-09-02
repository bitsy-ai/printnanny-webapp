from rest_framework.views import APIView
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema_view, extend_schema
from djstripe.enums import SubscriptionStatus

from print_nanny_webapp.subscriptions.api.serializers import (
    BillingSummarySerializer,
)
from print_nanny_webapp.utils.api.views import generic_get_errors
from print_nanny_webapp.subscriptions.services import (
    get_stripe_subscription,
    get_stripe_charges,
    get_stripe_customer,
    get_stripe_next_invoice,
    get_stripe_subscription_events,
)


@extend_schema_view(
    get=extend_schema(
        tags=["billing"],
        responses={200: BillingSummarySerializer(many=False)} | generic_get_errors,
    ),
)
class BillingSummaryView(APIView):
    def get(self, request, **kwargs):
        stripe_customer = get_stripe_customer(request.user)
        subscription = get_stripe_subscription(stripe_customer)
        charges = get_stripe_charges(stripe_customer)
        events = get_stripe_subscription_events(stripe_customer)
        if (
            subscription is not None
            and subscription.status != SubscriptionStatus.canceled
        ):
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
