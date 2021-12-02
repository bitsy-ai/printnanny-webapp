import logging

from typing import Any
from drf_spectacular.utils import extend_schema, extend_schema_view
from django.db.utils import IntegrityError

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
    DeviceInfoSerializer,
    DeviceConfigSerializer,
    LicenseSerializer,
    SystemTaskSerializer,
    DeviceSerializer,
    CameraSerializer,
    CloudiotDeviceSerializer,
    PrinterControllerSerializer,
)
from ..models import (
    DeviceInfo,
    DeviceConfig,
    License,
    SystemTask,
    Device,
    Camera,
    CloudiotDevice,
    PrinterController,
)
from ..services import generate_zipped_license_response

from print_nanny_webapp.utils.api.exceptions import AlreadyExists
from print_nanny_webapp.utils.api.serializers import ErrorDetailSerializer

logger = logging.getLogger(__name__)

##
# DeviceConfig
##
list_desired_config_schema = extend_schema(
    responses={
        "default": ErrorDetailSerializer,
        200: DeviceConfigSerializer(many=True),
    },
)


@extend_schema_view(
    list=list_desired_config_schema,
)
class DeviceConfigViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
):
    serializer_class = DeviceConfigSerializer
    queryset = DeviceConfig.objects.all()
    lookup_field = "id"

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


##
# SystemTask
##
list_system_tasks_schemaa = extend_schema(
    responses={
        "default": ErrorDetailSerializer,
        200: SystemTaskSerializer(many=True),
    },
)
create_system_tasks_schema = extend_schema(
    request=SystemTaskSerializer,
    responses={
        "default": ErrorDetailSerializer,
        201: SystemTaskSerializer,
    },
)


@extend_schema_view(
    list=list_system_tasks_schemaa,
    create=create_system_tasks_schema,
)
class SystemTaskViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
):
    serializer_class = SystemTaskSerializer
    queryset = SystemTask.objects.all()
    lookup_field = "id"


##
# License
##
list_licenses_schema = extend_schema(
    responses={
        "default": ErrorDetailSerializer,
        200: LicenseSerializer(many=True),
    },
)


@extend_schema_view(
    list=list_licenses_schema,
    tags=["devices"],
)
class LicenseViewSet(
    GenericViewSet,
    ListModelMixin,
):
    """
    All-in-one Print Nanny installation
    via print-nanny-main-<platform>-<cpu>.img
    """

    serializer_class = LicenseSerializer
    queryset = License.objects.all()
    lookup_field = "id"

    @extend_schema(
        request=LicenseSerializer,
        responses={
            "default": ErrorDetailSerializer,
            202: LicenseSerializer,
        },
        operation_id="license_activate",
    )
    @action(detail=True, methods=["POST"], url_path="activate")
    def activate(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        license = License.objects.get(pk=kwargs["id"])
        license.activated = True
        license.save()
        response_serializer = self.get_serializer(license)
        return Response(response_serializer.data, status=status.HTTP_202_ACCEPTED)


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

    @action(detail=True, methods=["GET"], url_path="generate-license")
    def generate_license(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        device = Device.objects.get(pk=kwargs["id"])
        return generate_zipped_license_response(device, request)


###
# DeviceInfo views
###
list_device_info_schema = extend_schema(
    responses={
        "default": ErrorDetailSerializer,
        200: DeviceInfoSerializer(many=True),
    },
)
modify_device_info_schema = extend_schema(
    request=DeviceInfoSerializer,
    responses={
        "default": ErrorDetailSerializer,
        201: DeviceInfoSerializer,
        202: DeviceInfoSerializer,
    },
)


@extend_schema_view(
    list=list_device_info_schema,
    create=modify_device_info_schema,
    update=modify_device_info_schema,
)
class DeviceInfoViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
):
    serializer_class = DeviceInfoSerializer
    queryset = DeviceInfo.objects.all()
    lookup_field = "id"

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @extend_schema(
        operation_id="device_info_update_or_create",
        responses={
            # 400: PrinterProfileSerializer,
            200: DeviceInfoSerializer,
            201: DeviceInfoSerializer,
        },
    )
    @action(methods=["post"], detail=False, url_path="update-or-create")
    def update_or_create(self, request, device_id=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            instance, created = serializer.update_or_create(
                serializer.validated_data, device_id
            )
            response_serializer = self.get_serializer(instance)
            if not created:
                return Response(response_serializer.data, status=status.HTTP_200_OK)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
