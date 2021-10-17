import logging

from typing import Any
from drf_spectacular.utils import extend_schema, extend_schema_view
from django.db.utils import IntegrityError

import rest_framework.status
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
    AnsibleFactsSerializer,
    AppliancePublicKeySerializer,
    ApplianceSerializer,
    CameraSerializer,
    CloudIoTDeviceSerializer,
    PrinterControllerSerializer,
)
from ..models import (
    AnsibleFacts,
    Appliance,
    AppliancePublicKey,
    Camera,
    CloudIoTDevice,
    PrinterController,
)
from print_nanny_webapp.utils.api.exceptions import AlreadyExists
from print_nanny_webapp.utils.api.serializers import ErrorDetailSerializer

logger = logging.getLogger(__name__)

##
# AnsibleFacts
##
list_ansible_facts_schema = extend_schema(
    responses={
        "default": ErrorDetailSerializer,
        200: AnsibleFactsSerializer(many=True),
    },
)
modify_ansible_facts_schema = extend_schema(
    request=AnsibleFactsSerializer,
    responses={
        "default": ErrorDetailSerializer,
        201: AnsibleFactsSerializer,
        202: AnsibleFactsSerializer,
    },
)


@extend_schema_view(
    list=list_ansible_facts_schema,
    create=modify_ansible_facts_schema,
    update=modify_ansible_facts_schema,
)
class AnsibleFactsViewSet(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
):
    serializer_class = AnsibleFactsSerializer
    queryset = AnsibleFacts.objects.all()
    lookup_field = "id"

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


##
# Appliance
##
list_appliances_schema = extend_schema(
    responses={
        "default": ErrorDetailSerializer,
        200: ApplianceSerializer(many=True),
    },
)
modify_appliances_schema = extend_schema(
    request=ApplianceSerializer,
    responses={
        "default": ErrorDetailSerializer,
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
            raise AlreadyExists(
                detail=f"Appliance with hostname={hostname} already exists for user={self.request.user.id}.",
            )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


##
# AppliancePublicKey
##
list_appliance_public_keys_schema = extend_schema(
    responses={
        "default": ErrorDetailSerializer,
        200: AppliancePublicKeySerializer(many=True),
    },
)
modify_appliance_public_keys_schema = extend_schema(
    request=AppliancePublicKeySerializer,
    responses={
        "default": ErrorDetailSerializer,
        201: AppliancePublicKeySerializer,
        202: AppliancePublicKeySerializer,
    },
)


@extend_schema_view(
    list=list_appliance_public_keys_schema,
    create=modify_appliance_public_keys_schema,
    update=modify_appliance_public_keys_schema,
)
class AppliancePublicKeyViewSet(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
):
    """
    Public key for Print Nanny Appliance
    Only one public key may be active at a time
    DELETE <:endpoint> will soft-delete a key
    """

    serializer_class = AppliancePublicKeySerializer
    queryset = AppliancePublicKey.objects.all()
    lookup_field = "id"

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        appliance = request.data.get("appliance_id")
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            raise AlreadyExists(
                detail=f"AppliancePublicKey already exists for appliance_id={appliance} already exists.",
            )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


##
# Cloud IoT Device
##
list_cloud_iot_devices_schema = extend_schema(
    responses={
        "default": ErrorDetailSerializer,
        200: CloudIoTDeviceSerializer(many=True),
    },
)
modify_cloud_iot_devices_schema = extend_schema(
    request=CloudIoTDeviceSerializer,
    responses={
        "default": ErrorDetailSerializer,
        201: CloudIoTDeviceSerializer,
        202: CloudIoTDeviceSerializer,
    },
)


@extend_schema_view(
    list=list_cloud_iot_devices_schema,
    create=modify_cloud_iot_devices_schema,
    update=modify_cloud_iot_devices_schema,
)
class CloudIoTDeviceViewSet(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
):
    serializer_class = CloudIoTDeviceSerializer
    queryset = CloudIoTDevice.objects.all()
    lookup_field = "id"

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


##
# Camera
##
list_cameras_schema = extend_schema(
    responses={
        "default": ErrorDetailSerializer,
        200: CameraSerializer(many=True),
    },
)
modify_cameras_schema = extend_schema(
    request=CameraSerializer,
    responses={
        "default": ErrorDetailSerializer,
        201: CameraSerializer,
        202: CameraSerializer,
    },
)


@extend_schema_view(
    list=list_cameras_schema,
    create=modify_cameras_schema,
    update=modify_cameras_schema,
)
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


##
# PrinterController
##
list_printer_controllers_schema = extend_schema(
    responses={
        "default": ErrorDetailSerializer,
        200: PrinterControllerSerializer(many=True),
    },
)
modify_printer_controllers_schema = extend_schema(
    request=ApplianceSerializer,
    responses={
        "default": ErrorDetailSerializer,
        201: PrinterControllerSerializer,
        202: PrinterControllerSerializer,
    },
)


@extend_schema_view(
    list=list_printer_controllers_schema,
    create=modify_printer_controllers_schema,
    update=modify_printer_controllers_schema,
)
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
