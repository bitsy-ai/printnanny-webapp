import logging

from typing import Any
from drf_spectacular.types import OpenApiTypes

from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiParameter,
    OpenApiResponse,
)
from django.db.utils import Error, IntegrityError
from django.http import Http404

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
    CameraSerializer,
    CloudiotDeviceSerializer,
    DeviceConfigSerializer,
    SystemInfoSerializer,
    DeviceSerializer,
    LicenseSerializer,
    PrinterControllerSerializer,
    TaskSerializer,
    TaskStatusSerializer,
)
from ..models import (
    Camera,
    CloudiotDevice,
    Device,
    DeviceConfig,
    SystemInfo,
    License,
    PrinterController,
    Task,
    TaskStatus,
)
from ..services import generate_zipped_license_response

from print_nanny_webapp.utils.api.exceptions import AlreadyExists
from print_nanny_webapp.utils.api.serializers import ErrorDetailSerializer

logger = logging.getLogger(__name__)

##
# Task
##
list_tasks_schemaa = extend_schema(
    responses={
        "default": ErrorDetailSerializer,
        200: TaskSerializer(many=True),
    },
)
create_tasks_schema = extend_schema(
    request=TaskSerializer,
    responses={
        "default": ErrorDetailSerializer,
        200: TaskSerializer,
        201: TaskSerializer,
    },
)


@extend_schema_view(
    list=list_tasks_schemaa,
    create=create_tasks_schema,
)
class TaskViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    lookup_field = "id"


##
# TaskStatus
##

list_tasks_status_schema = extend_schema(
    parameters=[
        OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
    ],
    responses={
        "default": ErrorDetailSerializer,
        200: TaskStatusSerializer(many=True),
    },
)
retrieve_tasks_status_schema = extend_schema(
    parameters=[
        OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH),
    ],
    responses={
        "default": ErrorDetailSerializer,
        200: TaskStatusSerializer(),
    },
)
create_tasks_status_schema = extend_schema(
    parameters=[
        OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
    ],
    request=TaskStatusSerializer,
    responses={
        "default": ErrorDetailSerializer,
        201: TaskSerializer,
    },
)


@extend_schema_view(
    list=list_tasks_status_schema,
    create=create_tasks_status_schema,
    retrieve=retrieve_tasks_status_schema,
)
class TaskStatusViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
):
    serializer_class = TaskStatusSerializer
    queryset = TaskStatus.objects.all()
    lookup_field = "id"

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            logger.debug(f"Created TaskStatus={serializer.instance}")
            task_serializer = TaskSerializer(instance=serializer.instance.task)
            headers = self.get_success_headers(task_serializer.data)
            logger.debug(f"Returning response Task={serializer.instance}")
            return Response(
                task_serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )
        logger.error(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
class LicenseViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
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
        401: ErrorDetailSerializer,
        403: ErrorDetailSerializer,
        500: ErrorDetailSerializer,
        200: DeviceSerializer(many=True),
    },
)
create_devices_schema = extend_schema(
    request=DeviceSerializer,
    responses={
        # todo create a generic model response serializer to capture expected errors for create, update, get, etc
        400: ErrorDetailSerializer,
        401: ErrorDetailSerializer,
        403: ErrorDetailSerializer,
        404: ErrorDetailSerializer,
        409: ErrorDetailSerializer,
        500: ErrorDetailSerializer,
        201: DeviceSerializer,
    },
)
modify_devices_schema = extend_schema(
    request=DeviceSerializer,
    responses={
        # todo create a generic model response serializer to capture expected errors for create, update, get, etc
        400: ErrorDetailSerializer,
        401: ErrorDetailSerializer,
        403: ErrorDetailSerializer,
        404: ErrorDetailSerializer,
        409: ErrorDetailSerializer,
        500: ErrorDetailSerializer,
        202: DeviceSerializer,
    },
)


@extend_schema_view(
    list=list_devices_schema,
    create=create_devices_schema,
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
    A device (Raspberry Pi) running Print Nanny OS
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

    @extend_schema(
        request=None,
        responses={(200): OpenApiResponse(response=OpenApiTypes.BINARY)},
        operation_id="devices_generate_license",
    )
    @action(detail=True, methods=["POST"], url_path="generate-license")
    def generate_license(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        device = Device.objects.get(pk=kwargs["id"])
        return generate_zipped_license_response(device, request)

    @extend_schema(
        responses={
            "default": ErrorDetailSerializer,
            200: LicenseSerializer,
        },
    )
    @action(detail=True, methods=["GET"], url_path="active-license")
    def active_license(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        device = Device.objects.get(pk=kwargs["id"])

        if device.active_license:
            serializer = LicenseSerializer(
                device.active_license, context=dict(request=request)
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        raise Http404


###
# SystemInfo views
###
list_device_info_schema = extend_schema(
    parameters=[
        OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
    ],
    responses={
        "default": ErrorDetailSerializer,
        200: SystemInfoSerializer(many=True),
    },
)
modify_device_info_schema = extend_schema(
    parameters=[
        OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
    ],
    request=SystemInfoSerializer,
    responses={
        "default": ErrorDetailSerializer,
        201: SystemInfoSerializer,
        202: SystemInfoSerializer,
    },
)


@extend_schema_view(
    list=list_device_info_schema,
    create=modify_device_info_schema,
    update=modify_device_info_schema,
)
class SystemInfoViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
):
    serializer_class = SystemInfoSerializer
    queryset = SystemInfo.objects.all()
    lookup_field = "id"

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @extend_schema(
        operation_id="device_info_update_or_create",
        responses={
            # 400: PrinterProfileSerializer,
            200: SystemInfoSerializer,
            201: SystemInfoSerializer,
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
    parameters=[
        OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
    ],
    responses={
        "default": ErrorDetailSerializer,
        200: CloudiotDeviceSerializer(many=True),
    },
)
retrieve_cloud_iot_devices_schema = extend_schema(
    parameters=[
        OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH),
        OpenApiParameter(name="id", type=int, location=OpenApiParameter.PATH),
    ],
    responses={
        "default": ErrorDetailSerializer,
        200: CloudiotDeviceSerializer(),
    },
)
create_cloud_iot_devices_schema = extend_schema(
    parameters=[
        OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH),
    ],
    request=CloudiotDeviceSerializer,
    responses={
        "default": ErrorDetailSerializer,
        201: CloudiotDeviceSerializer,
    },
)
modify_cloud_iot_devices_schema = extend_schema(
    parameters=[
        OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH),
        OpenApiParameter(name="id", type=int, location=OpenApiParameter.PATH),
    ],
    request=CloudiotDeviceSerializer,
    responses={
        "default": ErrorDetailSerializer,
        201: CloudiotDeviceSerializer,
        202: CloudiotDeviceSerializer,
    },
)


@extend_schema_view(
    retrieve=retrieve_cloud_iot_devices_schema,
    list=list_cloud_iot_devices_schema,
    create=create_cloud_iot_devices_schema,
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
    parameters=[
        OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
    ],
    responses={
        "default": ErrorDetailSerializer,
        200: CameraSerializer(many=True),
    },
)
modify_cameras_schema = extend_schema(
    parameters=[
        OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
    ],
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
    parameters=[
        OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
    ],
    responses={
        "default": ErrorDetailSerializer,
        200: PrinterControllerSerializer(many=True),
    },
)
modify_printer_controllers_schema = extend_schema(
    parameters=[
        OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
    ],
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
