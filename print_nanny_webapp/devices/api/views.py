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
    PrinterControllerSerializer,
)
from ..models import Camera, Appliance, PrinterController

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
    """
    All-in-one Print Nanny installation
    via print-nanny-main-<platform>-<cpu>.img
    """

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
    @action(methods=["post"], detail=False, url_path="update-or-create")
    def update_or_create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = CreateApplianceSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data.copy()
            del validated_data["hostname"]
            instance, created = serializer.update_or_create(
                request.user, serializer.validated_data.get("hostname"), validated_data
            )

            context = {"request": self.request}
            context.update(self.get_serializer_context())

            response_serializer = ApplianceSerializer(
                instance=instance, context=context
            )

            if not created:
                return Response(
                    response_serializer.data, status=status.HTTP_202_ACCEPTED
                )
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

    @extend_schema(
        request=PrinterControllerSerializer,
        responses={
            400: PrinterControllerSerializer,
            200: PrinterControllerSerializer,
            201: PrinterControllerSerializer,
            202: PrinterControllerSerializer,
        },
    )
    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return super().create(request, *args, **kwargs)
