import logging

from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from print_nanny_webapp.events.models import Event, TestEvent
from .serializers import PolymorphicEventSerializer, TestEventSerializer
from print_nanny_webapp.utils.api.views import (
    generic_create_errors,
    generic_list_errors,
    generic_get_errors,
    generic_update_errors,
)


@extend_schema(tags=["events", "devices"])
@extend_schema_view(
    create=extend_schema(
        responses={
            201: PolymorphicEventSerializer,
        }
    )
)
class EventViewSet(
    GenericViewSet, ListModelMixin, RetrieveModelMixin, CreateModelMixin
):
    serializer_class = PolymorphicEventSerializer
    queryset = Event.objects.all()
    lookup_field = "id"

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id)


@extend_schema(tags=["events", "devices"])
@extend_schema_view(
    create=extend_schema(
        request=TestEventSerializer,
        responses={
            201: TestEventSerializer,
        }
        | generic_create_errors,
    ),
    list=extend_schema(
        request=TestEventSerializer,
        responses={
            200: TestEventSerializer(many=True),
        }
        | generic_list_errors,
    ),
    retrieve=extend_schema(
        request=TestEventSerializer,
        responses={
            200: TestEventSerializer,
        }
        | generic_create_errors,
    ),
)
class TestEventViewSet(
    GenericViewSet, ListModelMixin, RetrieveModelMixin, CreateModelMixin
):
    serializer_class = TestEventSerializer
    queryset = TestEvent.objects.all()
