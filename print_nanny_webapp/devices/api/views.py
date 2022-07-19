import logging

from typing import Any

from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiParameter,
)
from django.db.utils import IntegrityError

from django.contrib.auth import get_user_model
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
from print_nanny_webapp.utils.api.exceptions import AlreadyExists
from print_nanny_webapp.utils.api.views import (
    generic_create_errors,
    generic_list_errors,
    generic_get_errors,
    generic_update_errors,
)
from .serializers import (
    ConfigSerializer,
    PublicKeySerializer,
    CloudiotDeviceSerializer,
    SystemInfoSerializer,
    DeviceSerializer,
    WebrtcStreamSerializer,
    DeviceSettingsSerializer,
)
from ..models import (
    CloudiotDevice,
    Device,
    WebrtcStream,
    PublicKey,
    SystemInfo,
    DeviceSettings,
)
from print_nanny_webapp.utils.api.service import get_api_config
from ..services import janus_cloud_setup, update_or_create_cloudiot_device

User = get_user_model()

logger = logging.getLogger(__name__)

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
        }
        | generic_update_errors,
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
        except IntegrityError as e:
            raise AlreadyExists(
                detail=f"Device with hostname={hostname} already exists for user={self.request.user.id}."
            ) from e

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


##
# PublicKey views
##


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
        ],
        responses={
            200: PublicKeySerializer(many=True),
        }
        | generic_list_errors,
    ),
    create=extend_schema(
        parameters=[
            OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
        ],
        request=PublicKeySerializer,
        responses={
            201: PublicKeySerializer,
        }
        | generic_create_errors,
    ),
    update=extend_schema(
        parameters=[
            OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
        ],
        request=PublicKeySerializer,
        responses={
            202: PublicKeySerializer,
        }
        | generic_create_errors,
    ),
)
class PublicKeyViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
):
    serializer_class = PublicKeySerializer
    queryset = PublicKey.objects.all()
    lookup_field = "id"

    @extend_schema(
        operation_id="public_key_update_or_create",
        responses={
            # 400: PrinterProfileSerializer,
            200: PublicKeySerializer,
            201: PublicKeySerializer,
        }
        | generic_create_errors
        | generic_update_errors,
    )
    @action(methods=["post"], detail=False, url_path="update-or-create")
    def update_or_create(self, request, device_id=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            instance, created = serializer.update_or_create(  # type: ignore[attr-defined]
                serializer.validated_data, device_id
            )
            response_serializer = self.get_serializer(instance)
            if not created:
                return Response(response_serializer.data, status=status.HTTP_200_OK)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


###
# DeviceSettings views
###
@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
        ],
        responses={
            200: DeviceSettingsSerializer(many=False),
        }
        | generic_list_errors,
    ),
    update=extend_schema(
        parameters=[
            OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
        ],
        request=DeviceSettingsSerializer,
        responses={
            202: DeviceSettingsSerializer,
        }
        | generic_create_errors,
    ),
)
class DeviceSettingsViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
):
    serializer_class = DeviceSettingsSerializer
    queryset = DeviceSettings.objects.all()
    lookup_field = "id"


###
# WebrtcStream Viewset
###
@extend_schema_view(
    list=extend_schema(
        tags=["janus", "devices"],
        parameters=[
            OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
        ],
        responses={
            200: WebrtcStreamSerializer(many=True),
        }
        | generic_list_errors,
    ),
    create=extend_schema(
        tags=["janus", "devices"],
        parameters=[
            OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
        ],
        request=WebrtcStreamSerializer,
        responses={
            201: WebrtcStreamSerializer,
        }
        | generic_create_errors,
    ),
    retrieve=extend_schema(
        tags=["janus", "devices"],
        parameters=[
            OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
        ],
        request=WebrtcStreamSerializer,
        responses={
            200: WebrtcStreamSerializer,
        }
        | generic_get_errors,
    ),
)
class WebrtcStreamViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
):
    serializer_class = WebrtcStreamSerializer
    queryset = WebrtcStream.objects.all()
    lookup_field = "id"


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
        | generic_update_errors,
    ),
    update_or_create=extend_schema(
        parameters=[
            OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
        ],
        request=SystemInfoSerializer,
        responses={
            201: SystemInfoSerializer,
            202: SystemInfoSerializer,
        }
        | generic_create_errors
        | generic_update_errors,
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

    @extend_schema(
        operation_id="system_info_update_or_create",
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
            instance, created = serializer.update_or_create(  # type: ignore[attr-defined]
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
        }
        | generic_update_errors,
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

    @extend_schema(
        operation_id="cloudiot_device_update_or_create",
        responses={
            # 400: PrinterProfileSerializer,
            200: CloudiotDeviceSerializer,
            201: CloudiotDeviceSerializer,
        },
    )
    @action(methods=["post"], detail=False, url_path="update-or-create")
    def update_or_create(self, request, device_id=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            public_key = serializer.validated_data["public_key"]
            # public_key = PublicKey.objects.get(id=public_key_id)
            instance, created = update_or_create_cloudiot_device(public_key)
            response_serializer = self.get_serializer(instance)
            if not created:
                return Response(response_serializer.data, status=status.HTTP_200_OK)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


##
# License download
##
class ConfigDownloadViewSet(
    GenericViewSet,
):
    serializer_class = ConfigSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="device_id", type=int, location=OpenApiParameter.PATH
            ),
        ],
        responses={
            200: ConfigSerializer,
        }
        | generic_get_errors,
    )
    @action(methods=["get"], detail=False, url_path="download")
    def download(self, request, device_id=None):
        device = Device.objects.get(id=device_id)
        api = get_api_config(request, device.user)
        instance = dict(device=device, api=api)
        serializer = ConfigSerializer(instance=instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
