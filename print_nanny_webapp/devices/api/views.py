import logging

from typing import Any

from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiParameter,
)
from django.http import HttpResponse
from django.db.utils import IntegrityError
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.renderers import BaseRenderer

from print_nanny_webapp.utils.api.exceptions import AlreadyExists
from print_nanny_webapp.utils.api.views import (
    generic_create_errors,
    generic_list_errors,
    generic_get_errors,
    generic_update_errors,
)

from .serializers import (
    PublicKeySerializer,
    CloudiotDeviceSerializer,
    SystemInfoSerializer,
    PiSerializer,
    WebrtcStreamSerializer,
    PiSettingsSerializer,
)
from ..models import (
    CloudiotDevice,
    Pi,
    WebrtcStream,
    PublicKey,
    SystemInfo,
    PiSettings,
)
from print_nanny_webapp.utils.api.service import get_api_config
from ..services import (
    build_license_zip,
    janus_cloud_setup,
    update_or_create_cloudiot_device,
)

User = get_user_model()

logger = logging.getLogger(__name__)


@extend_schema_view(
    retrieve=extend_schema(
        tags=["devices"],
    ),
    destroy=extend_schema(
        tags=["devices"],
    ),
    list=extend_schema(
        tags=["devices"],
        responses={
            200: PiSerializer(many=True),
        }
        | generic_list_errors,
    ),
    update=extend_schema(
        tags=["devices"],
        request=PiSerializer,
        responses={
            202: PiSerializer,
        }
        | generic_update_errors,
    ),
    partial_update=extend_schema(
        tags=["devices"],
        request=PiSerializer,
        responses={
            202: PiSerializer,
        }
        | generic_update_errors,
    ),
    create=extend_schema(
        tags=["devices"],
        request=PiSerializer,
        responses={201: PiSerializer} | generic_create_errors,
    ),
)
class PiViewSet(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
):
    """
    A device (Raspberry Pi) running Print Nanny OS
    """

    serializer_class = PiSerializer
    queryset = Pi.objects.all()
    lookup_field = "id"

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        hostname = request.data.get("hostname")
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            raise AlreadyExists(
                detail=f"Pi with hostname={hostname} already exists for user={self.request.user.id}."
            ) from e

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


##
# PublicKey views
##
@extend_schema_view(
    retrieve=extend_schema(tags=["devices"]),
    list=extend_schema(
        tags=["devices"],
        parameters=[
            OpenApiParameter(name="pi_id", type=int, location=OpenApiParameter.PATH)
        ],
        responses={
            200: PublicKeySerializer(many=True),
        }
        | generic_list_errors,
    ),
    create=extend_schema(
        tags=["devices"],
        parameters=[
            OpenApiParameter(name="pi_id", type=int, location=OpenApiParameter.PATH)
        ],
        request=PublicKeySerializer,
        responses={
            201: PublicKeySerializer,
        }
        | generic_create_errors,
    ),
    update=extend_schema(
        tags=["devices"],
        parameters=[
            OpenApiParameter(name="pi_id", type=int, location=OpenApiParameter.PATH)
        ],
        request=PublicKeySerializer,
        responses={
            202: PublicKeySerializer,
        }
        | generic_create_errors,
    ),
    partial_update=extend_schema(
        tags=["devices"],
        parameters=[
            OpenApiParameter(name="pi_id", type=int, location=OpenApiParameter.PATH)
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
        tags=["devices"],
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
# PiSettings views
###
@extend_schema_view(
    retrieve=extend_schema(tags=["devices"]),
    list=extend_schema(
        tags=["devices"],
        parameters=[
            OpenApiParameter(name="pi_id", type=int, location=OpenApiParameter.PATH)
        ],
        responses={
            200: PiSettingsSerializer(many=False),
        }
        | generic_list_errors,
    ),
    create=extend_schema(
        tags=["devices"],
        parameters=[
            OpenApiParameter(name="pi_id", type=int, location=OpenApiParameter.PATH)
        ],
        request=PiSettingsSerializer,
        responses={
            201: PiSettingsSerializer,
        }
        | generic_create_errors,
    ),
    update=extend_schema(
        tags=["devices"],
        parameters=[
            OpenApiParameter(name="pi_id", type=int, location=OpenApiParameter.PATH)
        ],
        request=PiSettingsSerializer,
        responses={
            202: PiSettingsSerializer,
        }
        | generic_update_errors,
    ),
    partial_update=extend_schema(
        tags=["devices"],
        parameters=[
            OpenApiParameter(name="pi_id", type=int, location=OpenApiParameter.PATH)
        ],
        request=PiSettingsSerializer,
        responses={
            202: PiSettingsSerializer,
        }
        | generic_update_errors,
    ),
)
class PiSettingsViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
):
    serializer_class = PiSettingsSerializer
    queryset = PiSettings.objects.all()
    lookup_field = "id"


###
# WebrtcStream Viewset
###
@extend_schema_view(
    list=extend_schema(
        tags=["janus", "devices"],
        parameters=[
            OpenApiParameter(name="pi_id", type=int, location=OpenApiParameter.PATH)
        ],
        responses={
            200: WebrtcStreamSerializer(many=True),
        }
        | generic_list_errors,
    ),
    create=extend_schema(
        tags=["janus", "devices"],
        parameters=[
            OpenApiParameter(name="pi_id", type=int, location=OpenApiParameter.PATH)
        ],
        request=WebrtcStreamSerializer,
        responses={
            201: WebrtcStreamSerializer,
        }
        | generic_create_errors,
    ),
    update=extend_schema(
        tags=["janus", "devices"],
        parameters=[
            OpenApiParameter(name="pi_id", type=int, location=OpenApiParameter.PATH)
        ],
        request=WebrtcStreamSerializer,
        responses={
            202: WebrtcStreamSerializer,
        }
        | generic_update_errors,
    ),
    partial_update=extend_schema(
        tags=["janus", "devices"],
        parameters=[
            OpenApiParameter(name="pi_id", type=int, location=OpenApiParameter.PATH)
        ],
        request=WebrtcStreamSerializer,
        responses={
            202: WebrtcStreamSerializer,
        }
        | generic_update_errors,
    ),
    retrieve=extend_schema(
        tags=["janus", "devices"],
        parameters=[
            OpenApiParameter(name="pi_id", type=int, location=OpenApiParameter.PATH)
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
    retrieve=extend_schema(tags=["devices"]),
    list=extend_schema(
        tags=["devices"],
        parameters=[
            OpenApiParameter(name="pi_id", type=int, location=OpenApiParameter.PATH)
        ],
        responses={
            200: SystemInfoSerializer(many=True),
        }
        | generic_list_errors,
    ),
    create=extend_schema(
        tags=["devices"],
        parameters=[
            OpenApiParameter(name="pi_id", type=int, location=OpenApiParameter.PATH)
        ],
        request=SystemInfoSerializer,
        responses={
            201: SystemInfoSerializer,
        }
        | generic_create_errors,
    ),
    update=extend_schema(
        tags=["devices"],
        parameters=[
            OpenApiParameter(name="pi_id", type=int, location=OpenApiParameter.PATH)
        ],
        request=SystemInfoSerializer,
        responses={
            202: SystemInfoSerializer,
        }
        | generic_update_errors,
    ),
    partial_update=extend_schema(
        tags=["devices"],
        parameters=[
            OpenApiParameter(name="pi_id", type=int, location=OpenApiParameter.PATH)
        ],
        request=SystemInfoSerializer,
        responses={
            202: SystemInfoSerializer,
        }
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
        parameters=[
            OpenApiParameter(name="pi_id", type=int, location=OpenApiParameter.PATH)
        ],
        tags=["devices"],
        operation_id="system_info_update_or_create",
        responses={
            # 400: PrinterProfileSerializer,
            200: SystemInfoSerializer,
            201: SystemInfoSerializer,
            202: SystemInfoSerializer,
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


##
# Cloud IoT Pi
##
@extend_schema_view(
    retrieve=extend_schema(
        tags=["devices"],
        parameters=[
            OpenApiParameter(name="pi_id", type=int, location=OpenApiParameter.PATH),
            OpenApiParameter(name="id", type=int, location=OpenApiParameter.PATH),
        ],
        responses={
            200: CloudiotDeviceSerializer(),
        }
        | generic_get_errors,
    ),
    list=extend_schema(
        tags=["devices"],
        parameters=[
            OpenApiParameter(name="pi_id", type=int, location=OpenApiParameter.PATH)
        ],
        responses={
            200: CloudiotDeviceSerializer(many=True),
        }
        | generic_list_errors,
    ),
    create=extend_schema(
        tags=["devices"],
        parameters=[
            OpenApiParameter(name="pi_id", type=int, location=OpenApiParameter.PATH),
        ],
        request=CloudiotDeviceSerializer,
        responses={
            201: CloudiotDeviceSerializer,
        }
        | generic_create_errors,
    ),
    update=extend_schema(
        tags=["devices"],
        parameters=[
            OpenApiParameter(name="pi_id", type=int, location=OpenApiParameter.PATH),
        ],
        request=CloudiotDeviceSerializer,
        responses={
            202: CloudiotDeviceSerializer,
        }
        | generic_update_errors,
    ),
    partial_update=extend_schema(
        tags=["devices"],
        parameters=[
            OpenApiParameter(name="pi_id", type=int, location=OpenApiParameter.PATH),
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
        tags=["devices"],
        operation_id="cloudiot_device_update_or_create",
        responses={
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


class ZipRenderer(BaseRenderer):
    media_type = "application/zip"
    format = "bin"


class PiLicenseViewset(
    GenericViewSet,
):
    # serializer_class = ConfigSerializer

    renderer_classes = [ZipRenderer]
    # @extend_schema(
    #     tags=["devices"],
    #     parameters=[
    #         OpenApiParameter(name="pi_id", type=int, location=OpenApiParameter.PATH),
    #     ],
    #     responses={
    #         200: ConfigSerializer,
    #     }
    #     | generic_get_errors,
    # )
    # @action(methods=["get"], detail=False, url_path="download")
    # def download(self, request, device_id=None):
    #     device = Pi.objects.get(id=device_id)
    #     api = get_api_config(request, device.user)
    #     instance = dict(device=device, api=api)
    #     serializer = ConfigSerializer(instance=instance)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        tags=["devices"],
        parameters=[
            OpenApiParameter(name="pi_id", type=int, location=OpenApiParameter.PATH),
        ],
        responses=bytes,
    )
    @action(detail=False, methods=["get"], url_path="zip")
    def download_zip(
        self, request: Request, pi_id=None, *args: Any, **kwargs: Any
    ) -> HttpResponse:
        pi = get_object_or_404(Pi.objects.filter(id=pi_id, user=request.user))

        zip_content = build_license_zip(pi, request)

        response = HttpResponse(zip_content, content_type=ZipRenderer.media_type)
        filename = f"printnanny-{pi.hostname}.zip"
        response["Content-Disposition"] = f"attachment; filename={filename}"
        return response
