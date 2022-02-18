import logging
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiParameter,
)
from django.apps import apps

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
)
from rest_framework.permissions import IsAuthenticated
from print_nanny_webapp.utils.api.views import (
    generic_create_errors,
    generic_list_errors,
    generic_get_errors,
)
from print_nanny_webapp.utils.permissions import IsObjectOwner
from print_nanny_webapp.events.models import Event
from .serializers import PolymorphicEventSerializer, PolymorphicDeviceEventSerializer

Device = apps.get_model("devices", "Device")

logger = logging.getLogger(__name__)


@extend_schema_view(
    list=extend_schema(
        tags=["events"],
        responses={
            200: PolymorphicEventSerializer(many=True),
        }
        | generic_list_errors,
    ),
    create=extend_schema(
        tags=["events"],
        request=PolymorphicEventSerializer,
        responses={
            201: PolymorphicEventSerializer,
        }
        | generic_create_errors,
    ),
    retrieve=extend_schema(
        tags=["events"],
        request=PolymorphicEventSerializer,
        responses={
            200: PolymorphicEventSerializer,
        }
        | generic_get_errors,
    ),
)
class EventViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
):
    """
    Generic events viewset
    """

    permission_classes = [IsObjectOwner, IsAuthenticated]
    serializer_class = PolymorphicEventSerializer
    queryset = Event.objects.all()
    lookup_field = "id"
    device = None
    stream = None

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id)

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        logger.info("EventViewSet.create serializer.is_valid=%s", serializer.data)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        logger.info("EventViewSet.perform_create request=%s", self.request.POST)
        serializer.save(user=self.request.user)
