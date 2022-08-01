import logging
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from django.apps import apps

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from print_nanny_webapp.events.models import BasePiEvent
from print_nanny_webapp.utils.api.views import (
    generic_create_errors,
    generic_list_errors,
    generic_get_errors,
)
from print_nanny_webapp.utils.permissions import IsObjectOwner
from .serializers import (
    PolymorphicPiEventSerializer,
)

Pi = apps.get_model("devices", "Pi")

logger = logging.getLogger(__name__)


@extend_schema_view(
    list=extend_schema(
        tags=["pis", "events"],
        responses={
            200: PolymorphicPiEventSerializer(many=True),
        }
        | generic_list_errors,
    ),
    create=extend_schema(
        tags=["pis", "events"],
        request=PolymorphicPiEventSerializer,
        responses={
            201: PolymorphicPiEventSerializer,
        }
        | generic_create_errors,
    ),
    retrieve=extend_schema(
        tags=["pis", "events"],
        request=PolymorphicPiEventSerializer,
        responses={
            200: PolymorphicPiEventSerializer,
        }
        | generic_get_errors,
    ),
)
class AllPiEventsViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
):
    """
    Interact with all events inheriting from BasePiEvent
    """

    permission_classes = [IsObjectOwner, IsAuthenticated]
    serializer_class = PolymorphicPiEventSerializer
    queryset = BasePiEvent.objects.all()
    lookup_field = "id"

    # get events related to all pis owned by authenticated user
    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id)


@extend_schema_view(
    list=extend_schema(
        tags=["pis", "events"],
        parameters=[
            OpenApiParameter(name="pi_id", type=int, location=OpenApiParameter.PATH)
        ],
        responses={
            200: PolymorphicPiEventSerializer(many=True),
        }
        | generic_list_errors,
    ),
)
class SinglePiEventsViewSet(
    GenericViewSet,
    ListModelMixin,
):
    """
    Interact with all events inheriting from BasePiEvent
    """

    permission_classes = [IsObjectOwner, IsAuthenticated]
    serializer_class = PolymorphicPiEventSerializer
    queryset = BasePiEvent.objects.all()
    lookup_field = "id"

    # get events related to path parameter: pi_id
    def get_queryset(self, pi_id=None, *args, **kwargs):
        if pi_id is None:
            raise ValueError("pi_id is required")
        return self.queryset.filter(user_id=self.request.user.id, pi_id=pi_id)

    # def create(self, request, *args, **kwargs):
    #     logger.info("EventViewSet.create handling request.data %s", request.data)
    #     serializer = PolymorphicEventCreateSerializer(data=request.data)
    #     logger.info("EventViewSet.create got serializer %s", serializer)
    #     serializer.is_valid(raise_exception=True)
    #     logger.info("EventViewSet.create serializer is_valid=True")

    #     # assert user owns device
    #     if serializer.validated_data.get("device"):
    #         device = serializer.validated_data.get("device")
    #         if device.user != request.user:
    #             raise PermissionDenied(
    #                 {
    #                     "message": "You don't have permission to access",
    #                     "object_id": device.id,
    #                     "user_id": request.user.id,
    #                     "serializer_data": serializer.validated_data,
    #                 }
    #             )

    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.validated_data)
    #     return Response(
    #         serializer.data, status=status.HTTP_201_CREATED, headers=headers
    #     )

    # def perform_create(self, serializer):
    #     return serializer.save(user=self.request.user)


# @extend_schema_view(
#     list=extend_schema(
#         tags=["events", "commands"],
#         responses={
#             200: PolymorphicCommandSerializer(many=True),
#         }
#         | generic_list_errors,
#     ),
#     create=extend_schema(
#         tags=["events", "commands"],
#         request=PolymorphicCommandCreateSerializer,
#         responses={
#             201: PolymorphicCommandSerializer,
#         }
#         | generic_create_errors,
#     ),
#     retrieve=extend_schema(
#         tags=["events", "commands"],
#         request=PolymorphicCommandSerializer,
#         responses={
#             200: PolymorphicCommandSerializer,
#         }
#         | generic_get_errors,
#     ),
# )
# class CommandViewSet(
#     GenericViewSet,
#     ListModelMixin,
#     RetrieveModelMixin,
#     CreateModelMixin,
# ):
#     """
#     Generic events viewset
#     """

#     permission_classes = [IsObjectOwner, IsAuthenticated]
#     serializer_class = PolymorphicCommandSerializer
#     queryset = Event.objects.all()
#     lookup_field = "id"

#     def get_queryset(self, *args, **kwargs):
#         return self.queryset.filter(user_id=self.request.user.id)

#     def create(self, request, *args, **kwargs):
#         logger.info("EventViewSet.create handling request.data %s", request.data)
#         serializer = PolymorphicCommandCreateSerializer(data=request.data)
#         logger.info("EventViewSet.create got serializer %s", serializer)
#         serializer.is_valid(raise_exception=True)
#         logger.info("EventViewSet.create serializer is_valid=True")

#         # assert user owns device
#         if serializer.validated_data.get("device"):
#             device = serializer.validated_data.get("device")
#             if device.user != request.user:
#                 raise PermissionDenied(
#                     {
#                         "message": "You don't have permission to access",
#                         "object_id": device.id,
#                         "user_id": request.user.id,
#                         "serializer_data": serializer.validated_data,
#                     }
#                 )

#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.validated_data)
#         return Response(
#             serializer.data, status=status.HTTP_201_CREATED, headers=headers
#         )

#     def perform_create(self, serializer):
#         return serializer.save(user=self.request.user)
