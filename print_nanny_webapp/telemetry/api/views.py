import logging
from print_nanny_webapp.telemetry.models import RemoteCommandEvent

from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSet

from drf_spectacular.utils import extend_schema, extend_schema_view
from django.apps import apps
from django.conf import settings

from .serializers import (
    OctoPrintEventSerializer,
    PrintNannyPluginEventSerializer,
    PrintStatusEventSerializer,
    TelemetryEventSerializer,
    RemoteCommandEventSerializer
)

PrintSession = apps.get_model("remote_control", "PrintSession")
TelemetryEvent = apps.get_model("telemetry", "TelemetryEvent")
PrintNannyPluginEvent = apps.get_model("telemetry", "PrintNannyPluginEvent")
OctoPrintEvent = apps.get_model("telemetry", "OctoPrintEvent")
PrintStatusEvent = apps.get_model("telemetry", "PrintStatusEvent")
RemoteCommandEvent = apps.get_model("telemetry", "RemoteCommandEvent")

logger = logging.getLogger(__name__)

@extend_schema(tags=["telemetry"])
@extend_schema_view(
    create=extend_schema(
        responses={
            201: TelemetryEventSerializer,
            400: TelemetryEventSerializer,
        }
    )
)
class TelemetryEventViewSet(
    GenericViewSet, ListModelMixin, RetrieveModelMixin
):
    serializer_class = TelemetryEventSerializer
    queryset = TelemetryEvent.objects.all()
    lookup_field = "id"

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id)


@extend_schema(tags=["telemetry"])
@extend_schema_view(
    create=extend_schema(
        responses={
            201: RemoteCommandEventSerializer,
            400: RemoteCommandEventSerializer,
        }
    )
)
class RemoteCommandqEventViewSet(
    GenericViewSet, ListModelMixin, RetrieveModelMixin
):
    serializer_class = RemoteCommandEventSerializer
    queryset = RemoteCommandEvent.objects.all()
    lookup_field = "id"

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id)



@extend_schema(tags=["telemetry"])
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


@extend_schema(tags=["telemetry"])
@extend_schema_view(
    create=extend_schema(
        responses={
            201: PrintNannyPluginEventSerializer,
            400: PrintNannyPluginEventSerializer,
        }
    )
)
class PrintNannyPluginEventViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = PrintNannyPluginEventSerializer
    queryset = PrintNannyPluginEvent.objects.all()
    lookup_field = "id"

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


@extend_schema(tags=["telemetry"])
@extend_schema_view(
    create=extend_schema(
        responses={
            201: PrintStatusEventSerializer,
            400: PrintStatusEventSerializer,
        }
    )
)
class PrintStatusEventViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = PrintStatusEventSerializer
    queryset = PrintStatusEvent.objects.all()
    lookup_field = "id"

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
