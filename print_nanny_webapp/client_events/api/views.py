import base64
import hashlib
import logging

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSet

from drf_spectacular.utils import extend_schema, extend_schema_view
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter
from django.apps import apps
from django.conf import settings

from .serializers import ClientEventPolymorphicSerializer
import print_nanny_webapp.client_events.api.exceptions

PrintJob = apps.get_model("remote_control", "PrintJob")
PluginEvent = apps.get_model("client_events", "PluginEvent")
OctoPrintEvent = apps.get_model("client_events", "OctoPrintEvent")
PrintJobState = apps.get_model("client_events", "PrintJobState")
logger = logging.getLogger(__name__)

@extend_schema(tags=["events"])
@extend_schema_view(
    create=extend_schema(
        responses={201:ClientEventPolymorphicSerializer, 400: ClientEventPolymorphicSerializer}
    )
)
class OctoPrintEventViewSet(
    CreateModelMixin, GenericViewSet, ListModelMixin, RetrieveModelMixin
):
    serializer_class = ClientEventPolymorphicSerializer
    queryset = OctoPrintEvent.objects.all()
    lookup_field = "id"

    @extend_schema(
        tags=["events"],
        operation_id="octoprint_core_events_enum_retrieve",
        responses={200: OpenApiTypes.STR},
    )
    @action(methods=["GET"], detail=False)
    def enum(self, *args, **kwargs):
        return Response(
            OctoPrintEvent.event_codes,
            status.HTTP_200_OK,
        )

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id)

    def perform_create(self, serializer):

        event_data = self.request.data["event_data"]

        print_job = event_data.get("print_job")
        if print_job is not None:
            print_job = PrintJob.objects.get(id=print_job)
        if self.request.user:
            user = self.request.user
        else:
            user = None
        instance = serializer.save(user=user, print_job=print_job)

@extend_schema(tags=["events"])
@extend_schema_view(
    create=extend_schema(
        responses={201:ClientEventPolymorphicSerializer, 400: ClientEventPolymorphicSerializer}
    )
)
class PluginEventViewSet(
    GenericViewSet, ListModelMixin, RetrieveModelMixin
):
    serializer_class = ClientEventPolymorphicSerializer
    queryset = PluginEvent.objects.all()
    lookup_field = "id"

    @extend_schema(
        tags=["events"],
        operation_id="plugin_events_enum_retrieve",
        responses={200: OpenApiTypes.STR},
    )
    @action(methods=["GET"], detail=False)
    def enum(self, *args, **kwargs):
        return Response(
            PluginEvent.event_codes,
            status.HTTP_200_OK,
        )

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id)

    def perform_create(self, serializer):

        event_data = self.request.data["event_data"]

        print_job = event_data.get("print_job")
        if print_job is not None:
            print_job = PrintJob.objects.get(id=print_job)
        if self.request.user:
            user = self.request.user
        else:
            user = None
        instance = serializer.save(user=user, print_job=print_job)

@extend_schema(tags=["events"])
@extend_schema_view(
    create=extend_schema(
        responses={201:ClientEventPolymorphicSerializer, 400: ClientEventPolymorphicSerializer}
    )
)
class PrintJobStateViewSet(
    GenericViewSet, ListModelMixin, RetrieveModelMixin
):
    serializer_class = ClientEventPolymorphicSerializer
    queryset = PrintJobState.objects.all()
    lookup_field = "id"

    @extend_schema(
        tags=["events"],
        operation_id="print_job_event_enum_retrieve",
        responses={200: OpenApiTypes.STR},
    )
    @action(methods=["GET"], detail=False)
    def enum(self, *args, **kwargs):
        return Response(
            PrintJobState.event_codes,
            status.HTTP_200_OK,
        )

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id)

    def perform_create(self, serializer):

        event_data = self.request.data["event_data"]

        print_job = event_data.get("print_job")
        if print_job is not None:
            print_job = PrintJob.objects.get(id=print_job)
        if self.request.user:
            user = self.request.user
        else:
            user = None
        instance = serializer.save(user=user, print_job=print_job)