import logging
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework import parsers
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from print_nanny_webapp.octoprint.api.serializers import (
    OctoPrintBackupSerializer,
    OctoPrinterProfileSerializer,
    GcodeFileSerializer,
    OctoPrintSettingsSerializer,
    OctoPrintServerSerializer,
)
from print_nanny_webapp.octoprint.models import (
    GcodeFile,
    OctoPrintBackup,
    OctoPrintSettings,
    OctoPrinterProfile,
    OctoPrintServer,
)
from print_nanny_webapp.utils.api.views import (
    generic_create_errors,
    generic_list_errors,
    generic_update_errors,
    generic_get_errors,
)


logger = logging.getLogger(__name__)

##
# OctoPrintServer (by device param)
##
@extend_schema_view(
    list=extend_schema(
        tags=["octoprint"],
        parameters=[
            OpenApiParameter(name="pi_id", type=int, location=OpenApiParameter.PATH)
        ],
        responses={
            200: OctoPrintServerSerializer(),
        }
        | generic_list_errors,
    ),
)
class OctoPrintServerByDeviceViewSet(
    GenericViewSet,
    ListModelMixin,
):
    serializer_class = OctoPrintServerSerializer
    queryset = OctoPrintServer.objects.all()
    lookup_field = "id"

    def get_queryset(self, *_args, device_id=None, **_kwargs):
        return self.queryset.filter(device=device_id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


##
# OctoPrintServer (no device filter)
##
@extend_schema_view(
    list=extend_schema(
        tags=["octoprint"],
        responses={
            200: OctoPrintServerSerializer(),
        }
        | generic_list_errors,
    ),
    create=extend_schema(
        tags=["octoprint"],
        request=OctoPrintServerSerializer,
        responses={
            201: OctoPrintServerSerializer,
        }
        | generic_create_errors,
    ),
    update=extend_schema(
        tags=["octoprint"],
        request=OctoPrintServerSerializer,
        responses={
            202: OctoPrintServerSerializer,
        }
        | generic_update_errors,
    ),
)
class OctoPrintServerViewSet(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    UpdateModelMixin,
):
    serializer_class = OctoPrintServerSerializer
    queryset = OctoPrintServer.objects.all()
    lookup_field = "id"

    @extend_schema(
        operation_id="octoprint_server_update_or_create",
        responses={
            # 400: PrinterProfileSerializer,
            200: OctoPrintServerSerializer,
            201: OctoPrintServerSerializer,
        },
        tags=["octoprint"],
    )
    @action(methods=["post"], detail=False, url_path="update-or-create")
    def update_or_create(self, request, device_id=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            device_id = request.data.get("device")
            instance, created = serializer.update_or_create(  # type: ignore[attr-defined]
                serializer.validated_data, device_id, self.request.user
            )
            response_serializer = self.get_serializer(instance)
            if not created:
                return Response(response_serializer.data, status=status.HTTP_200_OK)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


##
# OctoPrint Settings
##
@extend_schema_view(
    list=extend_schema(
        tags=["octoprint"],
        responses={
            200: OctoPrintSettingsSerializer,
        }
        | generic_list_errors,
    ),
    create=extend_schema(
        tags=["octoprint"],
        request=OctoPrintSettingsSerializer,
        responses={
            201: OctoPrintSettingsSerializer,
        }
        | generic_create_errors,
    ),
    update=extend_schema(
        tags=["octoprint"],
        request=OctoPrintSettingsSerializer,
        responses={
            202: OctoPrintSettingsSerializer,
        }
        | generic_update_errors,
    ),
)
class OctoPrintSettingsViewSet(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    UpdateModelMixin,
):
    serializer_class = OctoPrintSettingsSerializer
    queryset = OctoPrintSettings.objects.all()
    lookup_field = "id"

    @extend_schema(
        tags=["octoprint"],
        operation_id="octoprint_settings_update_or_create",
        responses={
            # 400: PrinterProfileSerializer,
            200: OctoPrintSettingsSerializer,
            201: OctoPrintSettingsSerializer,
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

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema_view(
    list=extend_schema(
        tags=["octoprint"],
        responses={200: OctoPrintBackupSerializer(many=True)} | generic_list_errors,
    ),
    create=extend_schema(
        tags=["octoprint"],
        request=OctoPrintBackupSerializer,
        responses={201: OctoPrintBackupSerializer} | generic_create_errors,
    ),
    retrieve=extend_schema(
        tags=["octoprint"],
        request=OctoPrintBackupSerializer,
        responses={200: OctoPrintBackupSerializer} | generic_get_errors,
    ),
)
class OctoPrintBackupViewset(
    GenericViewSet, ListModelMixin, RetrieveModelMixin, CreateModelMixin
):
    serializer_class = OctoPrintBackupSerializer
    queryset = OctoPrintBackup.objects.all()
    lookup_field = "id"
    parser_classes = [
        parsers.MultiPartParser,
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


##
# GcodeFile
##
@extend_schema_view(
    list=extend_schema(
        tags=["octoprint"],
        responses={
            200: GcodeFileSerializer(),
        }
        | generic_list_errors,
    ),
    create=extend_schema(
        tags=["octoprint"],
        request=GcodeFileSerializer,
        responses={
            201: GcodeFileSerializer,
        }
        | generic_create_errors,
    ),
    retrieve=extend_schema(
        tags=["octoprint"],
        request=GcodeFileSerializer,
        responses={200: GcodeFileSerializer} | generic_get_errors,
    ),
)
class GcodeFileViewSet(
    GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin
):
    serializer_class = GcodeFileSerializer
    queryset = GcodeFile.objects.all()
    lookup_field = "id"
    parser_classes = [
        parsers.MultiPartParser,
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


##
# OctoPrint Settings
##
@extend_schema_view(
    list=extend_schema(
        tags=["octoprint"],
        responses={
            200: OctoPrinterProfileSerializer(),
        }
        | generic_list_errors,
    ),
    create=extend_schema(
        tags=["octoprint"],
        request=OctoPrinterProfileSerializer,
        responses={
            201: OctoPrinterProfileSerializer,
        }
        | generic_create_errors,
    ),
    update=extend_schema(
        tags=["octoprint"],
        request=OctoPrinterProfileSerializer,
        responses={
            202: OctoPrinterProfileSerializer,
        }
        | generic_update_errors,
    ),
)
class OctoPrinterProfileViewSet(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    UpdateModelMixin,
):
    serializer_class = OctoPrinterProfileSerializer
    queryset = OctoPrinterProfile.objects.all()
    lookup_field = "id"

    @extend_schema(
        operation_id="octoprint_profile_update_or_create",
        responses={
            # 400: PrinterProfileSerializer,
            200: OctoPrinterProfileSerializer,
            201: OctoPrinterProfileSerializer,
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

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
