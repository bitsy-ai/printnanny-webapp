import logging

from typing import Any
from drf_spectacular.utils import extend_schema, extend_schema_view
from django.db.utils import IntegrityError

from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
import rest_framework.status

from .serializers import (
    AnsibleFactsSerializer,
    DeviceKeyPairSerializer,
    DevicePublicKeySerializer,
    DeviceSerializer,
    CameraSerializer,
    CloudiotDeviceSerializer,
    PrinterControllerSerializer,
)
from ..models import (
    AnsibleFacts,
    Device,
    DevicePublicKey,
    Camera,
    CloudiotDevice,
    PrinterController,
)
from ..services import KeyPair, generate_keypair_and_update_or_create_cloudiot_device
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
# Device (by id)
##
list_devices_schema = extend_schema(
    responses={
        "default": ErrorDetailSerializer,
        200: DeviceSerializer(many=True),
    },
)
modify_devices_schema = extend_schema(
    request=DeviceSerializer,
    responses={
        "default": ErrorDetailSerializer,
        201: DeviceSerializer,
        202: DeviceSerializer,
    },
)


@extend_schema_view(
    list=list_devices_schema,
    create=modify_devices_schema,
    update=modify_devices_schema,
)
class DeviceViewSet(
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

    serializer_class = DeviceSerializer
    queryset = Device.objects.all()
    lookup_field = "id"

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        hostname = request.data.get("hostname")
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            raise AlreadyExists(
                detail=f"Device with hostname={hostname} already exists for user={self.request.user.id}.",
            )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


###
# Devices (by hostname)
##
retrieve_devices_schema = extend_schema(
    operation_id="devices_retrieve_hostname",
    responses={
        "default": ErrorDetailSerializer,
        200: DeviceSerializer,
    },
)


@extend_schema_view(retrieve=retrieve_devices_schema)
class DeviceHostnameViewSet(
    GenericViewSet,
    RetrieveModelMixin,
):
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()
    lookup_field = "hostname"


##
# DevicePublicKey
##
list_device_public_keys_schema = extend_schema(
    responses={
        "default": ErrorDetailSerializer,
        200: DevicePublicKeySerializer(many=True),
    },
)
modify_device_public_keys_schema = extend_schema(
    request=DeviceKeyPairSerializer,
    responses={
        "default": ErrorDetailSerializer,
        201: DeviceKeyPairSerializer,
        202: DeviceKeyPairSerializer,
    },
)


@extend_schema_view(
    list=list_device_public_keys_schema,
    create=modify_device_public_keys_schema,
)
class DeviceKeyPairViewSet(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
):
    """
    Public key for Print Nanny Device
    Only one public key may be active at a time
    DELETE <:endpoint> will soft-delete a key
    """

    serializer_class = DevicePublicKeySerializer
    queryset = DevicePublicKey.objects.all()
    lookup_field = "id"

    def create(
        self, request: Request, device_id=None, *args: Any, **kwargs: Any
    ) -> Response:
        device = get_object_or_404(Device, pk=device_id)
        try:
            keypair, _ = generate_keypair_and_update_or_create_cloudiot_device(device)
            return Response(data=keypair, status=rest_framework.status.HTTP_201_CREATED)
        except IntegrityError:
            raise AlreadyExists(
                detail=f"DevicePublicKey already exists for device_id={device} already exists.",
            )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


##
# Cloud IoT Device
##
list_cloud_iot_devices_schema = extend_schema(
    responses={
        "default": ErrorDetailSerializer,
        200: CloudiotDeviceSerializer(many=True),
    },
)
modify_cloud_iot_devices_schema = extend_schema(
    request=CloudiotDeviceSerializer,
    responses={
        "default": ErrorDetailSerializer,
        201: CloudiotDeviceSerializer,
        202: CloudiotDeviceSerializer,
    },
)


@extend_schema_view(
    list=list_cloud_iot_devices_schema,
    create=modify_cloud_iot_devices_schema,
    update=modify_cloud_iot_devices_schema,
)
class CloudiotDeviceViewSet(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
):
    serializer_class = CloudiotDeviceSerializer
    queryset = CloudiotDevice.objects.all()
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
    request=DeviceSerializer,
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
