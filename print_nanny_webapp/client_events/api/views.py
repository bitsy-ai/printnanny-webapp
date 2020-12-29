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
from django.apps import apps
from django.conf import settings

from .serializers import OctoPrintEventSerializer, OctoPrintDeviceSerializer
import print_nanny_webapp.client_events.api.exceptions
from print_nanny_webapp.client_events.models import OctoPrintEvent, OctoPrintDevice

import google.api_core.exceptions

PrintJob = apps.get_model("remote_control", "PrintJob")
logger = logging.getLogger(__name__)


@extend_schema(tags=["events"])
@extend_schema_view(
    create=extend_schema(
        responses={201: OctoPrintEventSerializer, 400: OctoPrintEventSerializer}
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
        operation_id="octoprint_events_tracking_retrieve",
        responses={200: OpenApiTypes.STR},
    )
    @action(methods=["GET"], detail=False)
    def tracking(self, *args, **kwargs):
        return Response(
            [x.value for x in OctoPrintEvent.EventTypeChoices.__members__.values()],
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


@extend_schema(tags=["devices"])
@extend_schema_view(
    create=extend_schema(
        responses={201: OctoPrintDeviceSerializer, 400: OctoPrintDeviceSerializer}
    )
)
class OctoPrintDeviceViewSet(
    CreateModelMixin,
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
):

    serializer_class = OctoPrintDeviceSerializer
    queryset = OctoPrintDevice.objects.all()
    lookup_field = "id"

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        # a device with this serial already exists
        except google.api_core.exceptions.AlreadyExists as e:
            exception = (
                print_nanny_webapp.client_events.api.exceptions.DeviceAlreadyExists(
                    user=self.request.user.id,
                    serial=self.request.data["serial"],
                    parent_exception=e,
                )
            )
            logger.error(f"{str(exception)} {str(exception.parent_exception)}")
            raise exception
