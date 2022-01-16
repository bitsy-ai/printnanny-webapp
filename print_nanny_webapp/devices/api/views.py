import logging

from typing import Any

from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiParameter,
)
from django.db.utils import IntegrityError
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
    SystemInfoSerializer,
    DeviceSerializer,
    PrinterControllerSerializer,
    TaskSerializer,
    TaskStatusSerializer,
)
from ..models import (
    Camera,
    CloudiotDevice,
    Device,
    SystemInfo,
    PrinterController,
    Task,
    TaskStatus,
)
from ..services import generate_zipped_license_response

from print_nanny_webapp.utils.api.exceptions import AlreadyExists
from print_nanny_webapp.utils.api.serializers import ErrorDetailSerializer

from print_nanny_webapp.utils.api.views import (
    generic_create_errors,
    generic_list_errors,
    generic_get_errors,
    generic_update_errors,
)

logger = logging.getLogger(__name__)

##
# Task
##
@extend_schema_view(
    # GET many tasks
    list=extend_schema(
        responses={
            200: TaskSerializer(many=True),
        }
        | generic_list_errors
    ),
    # POST tasks
    create=extend_schema(
        request=TaskSerializer,
        responses={
            201: TaskSerializer,
        }
        | generic_create_errors,
    ),
    # GET one task
    retreive=extend_schema(
        request=TaskSerializer,
        responses={
            200: TaskSerializer,
        }
        | generic_get_errors,
    ),
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
@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
        ],
        responses={
            200: TaskStatusSerializer(many=True),
        }
        | generic_list_errors,
    ),
    create=extend_schema(
        parameters=[
            OpenApiParameter(
                name="device_id", type=int, location=OpenApiParameter.PATH
            ),
        ],
        responses={
            200: TaskStatusSerializer,
        }
        | generic_create_errors,
    ),
    retrieve=extend_schema(
        parameters=[
            OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
        ],
        request=TaskStatusSerializer,
        responses={
            201: TaskSerializer,
        }
        | generic_get_errors,
    ),
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
# Device (by id)
##

# override device_create_operation to set required = true on requestBody
# for some reason (yet unknown) DRF AutoSchema is omitting required on the POST method for this endpoint
# copied from /api/schema/
device_create_operation = {
    "operationId": "devices_create",
    "description": "A device (Raspberry Pi) running Print Nanny OS",
    "tags": ["devices"],
    "requestBody": {
        "content": {
            "application/json": {
                "schema": {"$ref": "#/components/schemas/DeviceRequest"}
            },
            "application/x-www-form-urlencoded": {
                "schema": {"$ref": "#/components/schemas/DeviceRequest"}
            },
            "multipart/form-data": {
                "schema": {"$ref": "#/components/schemas/DeviceRequest"}
            },
        },
        # this is the only line added to AutoSchema generated @ /api/schema/
        "required": True,
    },
    "security": [{"cookieAuth": []}, {"tokenAuth": []}],
    "responses": {
        "400": {
            "content": {
                "application/json": {
                    "schema": {"$ref": "#/components/schemas/ErrorDetail"}
                }
            },
            "description": "",
        },
        "401": {
            "content": {
                "application/json": {
                    "schema": {"$ref": "#/components/schemas/ErrorDetail"}
                }
            },
            "description": "",
        },
        "403": {
            "content": {
                "application/json": {
                    "schema": {"$ref": "#/components/schemas/ErrorDetail"}
                }
            },
            "description": "",
        },
        "404": {
            "content": {
                "application/json": {
                    "schema": {"$ref": "#/components/schemas/ErrorDetail"}
                }
            },
            "description": "",
        },
        "409": {
            "content": {
                "application/json": {
                    "schema": {"$ref": "#/components/schemas/ErrorDetail"}
                }
            },
            "description": "",
        },
        "500": {
            "content": {
                "application/json": {
                    "schema": {"$ref": "#/components/schemas/ErrorDetail"}
                }
            },
            "description": "",
        },
        "201": {
            "content": {
                "application/json": {"schema": {"$ref": "#/components/schemas/Device"}}
            },
            "description": "",
        },
    },
}


@extend_schema_view(
    list=extend_schema(
        responses={
            200: DeviceSerializer(many=True),
        }
        | generic_list_errors
    ),
    update=extend_schema(
        request=DeviceSerializer,
        responses={
            202: DeviceSerializer,
        }.update(generic_update_errors),
    ),
    create=extend_schema(
        operation=device_create_operation,
    ),
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

    @action(detail=True, methods=["GET"], url_path="generate-license")
    def generate_license(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        device = Device.objects.get(pk=kwargs["id"])
        return generate_zipped_license_response(device, request)

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


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
        ],
        responses={
            200: SystemInfoSerializer(many=True),
        }
        | generic_list_errors,
    ),
    create=extend_schema(
        parameters=[
            OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
        ],
        request=SystemInfoSerializer,
        responses={
            201: SystemInfoSerializer,
        }
        | generic_create_errors,
    ),
    update=extend_schema(
        parameters=[
            OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
        ],
        request=SystemInfoSerializer,
        responses={
            202: SystemInfoSerializer,
        }
        | generic_create_errors,
    ),
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


@extend_schema_view(
    retrieve=extend_schema(
        operation_id="devices_retrieve_hostname",
        responses={
            200: DeviceSerializer,
        }
        | generic_get_errors,
    )
)
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


@extend_schema_view(
    retrieve=extend_schema(
        parameters=[
            OpenApiParameter(
                name="device_id", type=int, location=OpenApiParameter.PATH
            ),
            OpenApiParameter(name="id", type=int, location=OpenApiParameter.PATH),
        ],
        responses={
            200: CloudiotDeviceSerializer(),
        }
        | generic_get_errors,
    ),
    list=extend_schema(
        parameters=[
            OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
        ],
        responses={
            200: CloudiotDeviceSerializer(many=True),
        }
        | generic_list_errors,
    ),
    create=extend_schema(
        parameters=[
            OpenApiParameter(
                name="device_id", type=int, location=OpenApiParameter.PATH
            ),
        ],
        request=CloudiotDeviceSerializer,
        responses={
            201: CloudiotDeviceSerializer,
        }
        | generic_create_errors,
    ),
    update=extend_schema(
        parameters=[
            OpenApiParameter(
                name="device_id", type=int, location=OpenApiParameter.PATH
            ),
        ],
        request=CloudiotDeviceSerializer,
        responses={
            202: CloudiotDeviceSerializer,
        }.update(generic_update_errors),
    ),
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
@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
        ],
        responses={
            200: CameraSerializer(many=True),
        }
        | generic_list_errors,
    ),
    create=extend_schema(
        parameters=[
            OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
        ],
        request=CameraSerializer,
        responses={
            201: CameraSerializer,
        }
        | generic_create_errors,
    ),
    update=extend_schema(
        parameters=[
            OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
        ],
        request=CameraSerializer,
        responses={
            202: CameraSerializer,
        }.update(generic_update_errors),
    ),
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


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
        ],
        responses={
            200: PrinterControllerSerializer(many=True),
        }
        | generic_list_errors,
    ),
    create=extend_schema(
        parameters=[
            OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
        ],
        request=DeviceSerializer,
        responses={
            201: PrinterControllerSerializer,
        }
        | generic_create_errors,
    ),
    update=extend_schema(
        parameters=[
            OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
        ],
        request=DeviceSerializer,
        responses={
            202: PrinterControllerSerializer,
        }.update(generic_update_errors),
    ),
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
