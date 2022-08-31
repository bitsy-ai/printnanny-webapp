from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.mixins import (
    ListModelMixin,
)
from rest_framework.viewsets import GenericViewSet
from rest_framework import status

from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from djstripe.models import Product
from djstripe.enums import SubscriptionStatus

from print_nanny_webapp.subscriptions.api.serializers import (
    BillingSummarySerializer,
    BillingCheckoutSessionSerializer,
    BillingProductSerializer,
)
from print_nanny_webapp.utils.api.views import generic_get_errors, generic_update_errors
from print_nanny_webapp.subscriptions.services import (
    get_stripe_subscription,
    get_stripe_charges,
    get_stripe_customer,
    get_stripe_next_invoice,
    get_stripe_subscription_events,
    create_stripe_checkout_session,
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


@extend_schema_view(
    get=extend_schema(
        tags=["billing"],
        responses={200: BillingProductSerializer(many=True)} | generic_get_errors,
    ),
)
class BillingProductsViewSet(GenericViewSet, ListModelMixin):
    serializer_class = BillingProductSerializer
    queryset = Product.objects.all()
    lookup_field = "id"
    # omit OwnerOrUserFilterBackend, which is a DEFAULT_FILTER_BACKENDS
    filter_backends = [DjangoFilterBackend]
    permission_classes = (AllowAny,)


@extend_schema_view(
    post=extend_schema(
        tags=["billing"],
        request=BillingCheckoutSessionSerializer,
        responses={200: BillingCheckoutSessionSerializer(many=False)}
        | generic_update_errors,
    ),
)
class BillingCheckoutView(APIView):
    lookup_field = "id"
    # omit OwnerOrUserFilterBackend, which is a DEFAULT_FILTER_BACKENDS
    filter_backends = [DjangoFilterBackend]
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = BillingCheckoutSessionSerializer(data=request.data)
        if serializer.is_valid():
            stripe_lookup_key = serializer.validated_data["stripe_price_lookup_key"]
            django_session = request.session._get_or_create_session_key()
            if request.user.is_authenticated:
                checkout_session = create_stripe_checkout_session(
                    stripe_lookup_key, django_session, user=request.user
                )
            else:
                checkout_session = create_stripe_checkout_session(
                    stripe_lookup_key, django_session, user=None
                )
            # response_serializer = BillingCheckoutSessionSerializer(
            #     instance=dict(url=checkout_session.url)
            # )
            return Response(
                {"url": checkout_session.url}, status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
