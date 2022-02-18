import logging
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiParameter,
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from django.apps import apps
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
)
from print_nanny_webapp.utils.api.views import (
    generic_create_errors,
    generic_list_errors,
    generic_get_errors,
)
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

    serializer_class = PolymorphicEventSerializer
    queryset = Event.objects.all()
    lookup_field = "id"
    device = None
    stream = None

    def get_queryset(self, *args, **kwargs):
        device_id = self.kwargs.get("device_id")
        self.device = get_object_or_404(Device, pk=device_id)
        return self.queryset.filter(user_id=self.request.user.id, device=self.device)

    def create(self, request, *args, **kwargs):
        device_id = kwargs.get("device_id")
        if device_id is None:
            raise ValueError("Failed to parse :device_id from url path")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        logger.info("EventViewSet.create serializer.is_valid=%s", serializer.data)

        self.device = get_object_or_404(Device, pk=device_id)
        self.stream = janus_stream_get_or_create(self.device)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        logger.info("EventViewSet.perform_create request=%s", self.request.POST)
        serializer.save(device=self.device, stream=self.stream)


@extend_schema_view(
    list=extend_schema(
        tags=["events", "devices"],
        parameters=[
            OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
        ],
        responses={
            200: PolymorphicEventSerializer(many=True),
        }
        | generic_list_errors,
    ),
    create=extend_schema(
        tags=["events", "devices"],
        parameters=[
            OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
        ],
        request=PolymorphicEventSerializer,
        responses={
            201: PolymorphicEventSerializer,
        }
        | generic_create_errors,
    ),
    retrieve=extend_schema(
        tags=["events", "devices"],
        parameters=[
            OpenApiParameter(
                name="device_id", type=int, location=OpenApiParameter.PATH
            ),
        ],
        request=PolymorphicEventSerializer,
        responses={
            200: PolymorphicEventSerializer,
        }
        | generic_get_errors,
    ),
)
class DeviceEventViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
):
    """
    Generic events viewset
    """

    serializer_class = PolymorphicDeviceEventSerializer
    queryset = Event.objects.all()
    lookup_field = "id"
    device = None
    stream = None

    def get_queryset(self, *args, **kwargs):
        device_id = self.kwargs.get("device_id")
        self.device = get_object_or_404(Device, pk=device_id)
        return self.queryset.filter(user_id=self.request.user.id, device=self.device)

    def create(self, request, *args, **kwargs):
        device_id = kwargs.get("device_id")
        if device_id is None:
            raise ValueError("Failed to parse :device_id from url path")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        logger.info("EventViewSet.create serializer.is_valid=%s", serializer.data)

        self.device = get_object_or_404(Device, pk=device_id)
        self.stream = janus_stream_get_or_create(self.device)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        logger.info("EventViewSet.perform_create request=%s", self.request.POST)
        serializer.save(device=self.device, stream=self.stream)
