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
    DeviceSerializer,
    DeviceIdentitySerializer,
)
from ..models import CameraController, Device, Appliance

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
        operation_id="appliances_update_or_create",
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


# @extend_schema(tags=["devices"])
# class PrinterProfileViewSet(
#     GenericViewSet,
#     CreateModelMixin,
#     ListModelMixin,
#     RetrieveModelMixin,
#     UpdateModelMixin,
# ):

#     serializer_class = PrinterProfilePolymorphicSerializer
#     queryset = PrinterProfile.objects.all()
#     lookup_field = "id"

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# @extend_schema(tags=["devices"])
# class CameraControllerViewSet(
#     GenericViewSet,
#     CreateModelMixin,
#     ListModelMixin,
#     RetrieveModelMixin,
#     UpdateModelMixin,
# ):

#     serializer_class = CameraControllerSerializer
#     queryset = CameraController.objects.all()
#     lookup_field = "id"

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
