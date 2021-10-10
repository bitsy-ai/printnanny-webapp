import logging

from typing import Any
from drf_spectacular.utils import extend_schema
from rest_framework import status
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
    CreateApplianceSerializer,
    CameraSerializer,
)
from ..models import Camera, Appliance

logger = logging.getLogger(__name__)


##
# v1 Appliance Identity Provisioning (distributed via rpi-imager)
##
class ApplianceViewSet(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
):
    serializer_class = ApplianceSerializer
    queryset = Appliance.objects.all()
    lookup_field = "id"

    @extend_schema(
        request=CreateApplianceSerializer,
        responses={
            400: ApplianceSerializer,
            200: ApplianceSerializer,
            201: ApplianceSerializer,
            202: ApplianceSerializer,
        },
    )
    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return super().create(request, *args, **kwargs)


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

    @extend_schema(
        request=CameraSerializer,
        responses={
            400: CameraSerializer,
            200: CameraSerializer,
            201: CameraSerializer,
            202: CameraSerializer,
        },
    )
    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return super().create(request, *args, **kwargs)
