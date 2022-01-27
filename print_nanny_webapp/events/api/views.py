import logging

from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from print_nanny_webapp.events.models import Event, PrintNannyEvent
from .serializers import PolymorphicEventSerializer, PrintNannyEventSerializer


@extend_schema(tags=["events", "devices"])
@extend_schema_view(
    create=extend_schema(
        responses={
            200: PolymorphicEventSerializer,
            201: PolymorphicEventSerializer,
            400: PolymorphicEventSerializer,
        }
    )
)
class EventViewSet(
    GenericViewSet, ListModelMixin, RetrieveModelMixin, CreateModelMixin
):
    serializer_class = PolymorphicEventSerializer
    queryset = Event.objects.all()


@extend_schema(tags=["events", "devices"])
@extend_schema_view(
    create=extend_schema(
        responses={
            200: PolymorphicEventSerializer,
            201: PolymorphicEventSerializer,
            400: PolymorphicEventSerializer,
        }
    )
)
class PrintNannyEventViewSet(
    GenericViewSet, ListModelMixin, RetrieveModelMixin, CreateModelMixin
):
    serializer_class = PrintNannyEventSerializer
    queryset = PrintNannyEvent.objects.all()
