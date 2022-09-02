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
from print_nanny_webapp.shop.enum import OrderStatusType
from print_nanny_webapp.shop.models import Product, OrderStatus
from print_nanny_webapp.utils.api.views import generic_get_errors, generic_create_errors
from print_nanny_webapp.shop.services import sync_stripe_order


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
        serializer = OrderCheckoutSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            instance = serializer.create(serializer.validated_data)
            res_serializer = OrderSerializer(instance=instance)
            return Response(res_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(
    get=extend_schema(
        tags=["shop"],
        request=OrderSerializer,
        responses={200: OrderSerializer(many=False)} | generic_get_errors,
    ),
)
class OrderByStripeCheckoutSessionIdView(APIView):
    permission_classes = (AllowAny,)

    def get(self, _request, stripe_checkout_session_id=None):
        if stripe_checkout_session_id is not None:

            order = sync_stripe_order(stripe_checkout_session_id)

            # create order status
            OrderStatus.objects.create(
                order=order, status=OrderStatusType.CHECKOUT_SESSION_COMPLETED
            )

            response_serializer = OrderSerializer(instance=order)
            return Response(response_serializer.data, status=status.HTTP_200_OK)
        return Response(
            "stripe_checkout_session_id is required", status=status.HTTP_400_BAD_REQUEST
        )
