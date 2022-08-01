import logging

from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from drf_spectacular.utils import extend_schema, extend_schema_view
from django.apps import apps

from .serializers import (
    OctoPrintEventSerializer,
    PrintNannyPluginEventSerializer,
    PrintJobEventSerializer,
    PrinterEventSerializer,
    TelemetryEventPolymorphicSerializer,
    RemoteCommandEventSerializer,
)
from print_nanny_webapp.telemetry.models import OctoPrintEvent

TelemetryEvent = apps.get_model("telemetry", "TelemetryEvent")
PrintNannyPluginEvent = apps.get_model("telemetry", "PrintNannyPluginEvent")
PrintJobEvent = apps.get_model("telemetry", "PrintJobEvent")
PrinterEvent = apps.get_model("telemetry", "PrinterEvent")
RemoteCommandEvent = apps.get_model("telemetry", "RemoteCommandEvent")

logger = logging.getLogger(__name__)


@extend_schema(tags=["telemetry"])
@extend_schema_view(
    create=extend_schema(
        responses={
            201: TelemetryEventPolymorphicSerializer,
            400: TelemetryEventPolymorphicSerializer,
        }
    )
)
class TelemetryEventViewSet(
    GenericViewSet, ListModelMixin, RetrieveModelMixin, CreateModelMixin
):
    serializer_class = TelemetryEventPolymorphicSerializer
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
class RemoteCommandEventViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
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


@extend_schema(tags=["telemetry"])
@extend_schema_view(
    create=extend_schema(
        responses={
            201: PrintJobEventSerializer,
            400: PrintJobEventSerializer,
        }
    )
)
class PrintJobEventViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = PrintJobEventSerializer
    queryset = PrintJobEvent.objects.all()
    lookup_field = "id"

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id)


@extend_schema(tags=["telemetry"])
@extend_schema_view(
    create=extend_schema(
        responses={
            201: PrinterEventSerializer,
            400: PrinterEventSerializer,
        }
    )
)
class PrinterEventViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = PrinterEventSerializer
    queryset = PrinterEvent.objects.all()
    lookup_field = "id"

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id)
