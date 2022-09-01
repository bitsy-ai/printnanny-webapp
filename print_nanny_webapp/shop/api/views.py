from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
)
from rest_framework import status


from print_nanny_webapp.shop.api.serializers import (
    ProductSerializer,
    OrderSerializer,
    OrderCheckoutSerializer,
)
from print_nanny_webapp.shop.models import Product
from print_nanny_webapp.shop.services import create_stripe_checkout_session
from print_nanny_webapp.utils.api.views import generic_get_errors, generic_create_errors


@extend_schema_view(
    get=extend_schema(
        tags=["shop"],
        responses={200: ProductSerializer(many=True)} | generic_get_errors,
    ),
)
class ProductsViewSet(GenericViewSet, ListModelMixin):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = "id"
    # omit OwnerOrUserFilterBackend, which is a DEFAULT_FILTER_BACKENDS
    filter_backends = [DjangoFilterBackend]
    permission_classes = (AllowAny,)


@extend_schema_view(
    post=extend_schema(
        tags=["shop"],
        request=OrderCheckoutSerializer,
        responses={200: OrderCheckoutSerializer(many=False)} | generic_create_errors,
    ),
)
class OrderCheckoutView(APIView):
    # allows order to be created from anonymous session
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = OrderSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            stripe_lookup_key = serializer.validated_data["stripe_price_lookup_key"]
            django_session = request.session._get_or_create_session_key()
            checkout_session = create_stripe_checkout_session(
                request, stripe_lookup_key, django_session
            )
            return Response(
                {"url": checkout_session.url}, status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(
    get=extend_schema(
        tags=["orders"],
        request=OrderSerializer,
        responses={200: OrderSerializer(many=False)} | generic_get_errors,
    ),
)
class OrderByStripeCheckoutSessionIdView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, stripe_checkout_session_id=None):
        pass
        # if stripe_checkout_session_id is not None:
        #     session = sync_stripe_checkout_session(stripe_checkout_session_id)
        #     customer = get_stripe_customer_by_id(session.customer.id)

        #     response_serializer = StripeCheckoutSuccessSerializer(
        #         instance=dict(
        #             stripe_checkout_session_id=stripe_checkout_session_id,
        #             stripe_session=session,
        #             stripe_customer=customer,
        #         )
        #     )
        #     return Response(response_serializer.data, status=status.HTTP_200_OK)
        # return Response(
        #     "stripe_checkout_session_id is required", status=status.HTTP_400_BAD_REQUEST
        # )
