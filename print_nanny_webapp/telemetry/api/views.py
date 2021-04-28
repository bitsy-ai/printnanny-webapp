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

from .serializers import (
    OctoPrintEventSerializer,
    PluginEventSerializer,
    PrintSessionStateSerializer,
)
import print_nanny_webapp.telemetry.api.exceptions

PrintSession = apps.get_model("remote_control", "PrintSession")
PluginEvent = apps.get_model("telemetry", "PluginEvent")
OctoPrintEvent = apps.get_model("telemetry", "OctoPrintEvent")
PrintSessionState = apps.get_model("telemetry", "PrintSessionState")

logger = logging.getLogger(__name__)


@extend_schema(tags=["events"])
@extend_schema_view(
    create=extend_schema(
        responses={
            201: OctoPrintEventSerializer,
            400: OctoPrintEventSerializer,
        }
    )
)
class OctoPrintEventViewSet(
    CreateModelMixin, GenericViewSet, ListModelMixin, RetrieveModelMixin
):
    serializer_class = OctoPrintEventSerializer
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

        print_session = event_data.get("print_session")
        if print_session is not None:
            print_session = PrintSession.objects.get(id=print_session)
        if self.request.user:
            user = self.request.user
        else:
            user = None
        instance = serializer.save(user=user, print_session=print_session)


@extend_schema(tags=["events"])
@extend_schema_view(
    create=extend_schema(
        responses={201: PluginEventSerializer, 400: PluginEventSerializer}
    )
)
class PluginEventViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = PluginEventSerializer
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

        print_session = event_data.get("print_session")
        if print_session is not None:
            print_session = PrintSession.objects.get(id=print_session)
        if self.request.user:
            user = self.request.user
        else:
            user = None
        instance = serializer.save(user=user, print_session=print_session)


@extend_schema(tags=["events"])
@extend_schema_view(
    create=extend_schema(
        responses={
            201: PrintSessionStateSerializer,
            400: PrintSessionStateSerializer,
        }
    )
)
class PrintSessionStateViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = PrintSessionStateSerializer
    queryset = PrintSessionState.objects.all()
    lookup_field = "id"

    @extend_schema(
        tags=["events"],
        operation_id="print_session_event_enum_retrieve",
        responses={200: OpenApiTypes.STR},
    )
    @action(methods=["GET"], detail=False)
    def enum(self, *args, **kwargs):
        return Response(
            PrintSessionState.event_codes,
            status.HTTP_200_OK,
        )

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id)

    def perform_create(self, serializer):

        event_data = self.request.data["event_data"]

        print_session = event_data.get("print_session")
        if print_session is not None:
            print_session = PrintSession.objects.get(id=print_session)
        if self.request.user:
            user = self.request.user
        else:
            user = None
        instance = serializer.save(user=user, print_session=print_session)
