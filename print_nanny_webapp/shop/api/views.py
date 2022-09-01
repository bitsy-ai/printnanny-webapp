from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
)

from print_nanny_webapp.shop.api.serializers import ProductSerializer
from print_nanny_webapp.shop.models import Product
from print_nanny_webapp.utils.api.views import generic_get_errors


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


# @extend_schema_view(
#     post=extend_schema(
#         tags=["billing"],
#         request=BillingCheckoutSessionSerializer,
#         responses={200: BillingCheckoutSessionSerializer(many=False)}
#         | generic_update_errors,
#     ),
# )
# class BillingCheckoutView(APIView):
#     # omit OwnerOrUserFilterBackend, which is a DEFAULT_FILTER_BACKENDS
#     filter_backends = [DjangoFilterBackend]
#     permission_classes = (AllowAny,)

#     def post(self, request):
#         serializer = BillingCheckoutSessionSerializer(data=request.data)
#         if serializer.is_valid():
#             stripe_lookup_key = serializer.validated_data["stripe_price_lookup_key"]
#             django_session = request.session._get_or_create_session_key()
#             checkout_session = create_stripe_checkout_session(
#                 request, stripe_lookup_key, django_session
#             )
#             return Response(
#                 {"url": checkout_session.url}, status=status.HTTP_201_CREATED
#             )

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @extend_schema_view(
#     get=extend_schema(
#         tags=["billing"],
#         responses={200: StripeCheckoutSuccessSerializer(many=False)}
#         | generic_get_errors,
#     ),
# )
# class BillingCheckoutSuccessView(APIView):
#     filter_backends = [DjangoFilterBackend]
#     permission_classes = (AllowAny,)

#     def get(self, request, stripe_checkout_session_id=None):

#         if stripe_checkout_session_id is not None:
#             session = get_stripe_checkout_session(stripe_checkout_session_id)
#             customer = get_stripe_customer_by_id(session.customer.id)

#             response_serializer = StripeCheckoutSuccessSerializer(
#                 instance=dict(
#                     stripe_checkout_session_id=stripe_checkout_session_id,
#                     stripe_session=session,
#                     stripe_customer=customer,
#                 )
#             )
#             return Response(response_serializer.data, status=status.HTTP_200_OK)
#         return Response(
#             "stripe_checkout_session_id is required", status=status.HTTP_400_BAD_REQUEST
#         )
