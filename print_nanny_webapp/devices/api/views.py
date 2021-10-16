import logging

from typing import Any
from drf_spectacular.utils import extend_schema, extend_schema_view
from django.db.utils import IntegrityError

import rest_framework.status
from rest_framework.serializers import ValidationError
from rest_framework.decorators import action
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .serializers import (
    ApplianceSerializer,
    CameraSerializer,
    PrinterControllerSerializer,
)
from ..models import Camera, Appliance, PrinterController

logger = logging.getLogger(__name__)


##
# v1 Appliance Identity Provisioning (distributed via rpi-imager)
##
list_appliances_schema = extend_schema(
    responses={
        403: {"type": "object", "properties": {"detail": {"type": "string"}}},
        500: {"type": "object", "properties": {"detail": {"type": "string"}}},
        200: ApplianceSerializer(many=True),
    },
)
modify_appliances_schema = extend_schema(
    request=ApplianceSerializer,
    responses={
        403: {"type": "object", "properties": {"detail": {"type": "string"}}},
        409: {"type": "object", "properties": {"detail": {"type": "string"}}},
        500: {"type": "object", "properties": {"detail": {"type": "string"}}},
        200: ApplianceSerializer,
        201: ApplianceSerializer,
        202: ApplianceSerializer,
    },
)


@extend_schema_view(
    list=list_appliances_schema,
    create=modify_appliances_schema,
    update=modify_appliances_schema,
)
class ApplianceViewSet(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
):
    """
    All-in-one Print Nanny installation
    via print-nanny-main-<platform>-<cpu>.img
    """

    serializer_class = ApplianceSerializer
    queryset = Appliance.objects.all()
    lookup_field = "id"

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        hostname = request.data.get("hostname")
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            raise ValidationError(
                code=rest_framework.status.HTTP_409_CONFLICT,
                detail=f"HTTP_409_CONFLICT: Appliance with hostname={hostname} already exists for user={self.request.user.id}",
            )
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CameraViewSet(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
):
    serializer_class = CameraSerializer
    queryset = Camera.objects.all()
    lookup_field = "id"

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PrinterControllerViewSet(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
):
    serializer_class = PrinterControllerSerializer
    queryset = PrinterController.objects.all()
    lookup_field = "id"

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
