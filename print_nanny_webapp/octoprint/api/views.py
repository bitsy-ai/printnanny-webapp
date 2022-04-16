import logging
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework import parsers
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
)
from rest_framework import status
from rest_framework.response import Response

from print_nanny_webapp.octoprint.api.serializers import (
    OctoPrintBackupSerializer,
    OctoPrinterProfileSerializer,
    GcodeFileSerializer,
    OctoPrintSettingsSerializer,
    OctoPrintInstallSerializer,
)
from print_nanny_webapp.octoprint.models import (
    GcodeFile,
    OctoPrintBackup,
    OctoPrintSettings,
    OctoPrinterProfile,
    OctoPrintInstall,
)
from print_nanny_webapp.utils.api.views import (
    generic_create_errors,
    generic_list_errors,
    generic_update_errors,
    generic_get_errors,
)


logger = logging.getLogger(__name__)

##
# OctoPrintInstall (by device param)
##
@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
        ],
        responses={
            200: OctoPrintInstallSerializer(),
        }
        | generic_list_errors,
    ),
    tags=["octoprint"],
)
class OctoPrintInstallByDeviceViewSet(
    GenericViewSet,
    ListModelMixin,
):
    serializer_class = OctoPrintInstallSerializer
    queryset = OctoPrintInstall.objects.all()
    lookup_field = "id"

    def get_queryset(self, *_args, device_id=None, **_kwargs):
        return self.queryset.filter(device=device_id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


##
# OctoPrintInstall (no device filter)
##
@extend_schema_view(
    list=extend_schema(
        responses={
            200: OctoPrintInstallSerializer(),
        }
        | generic_list_errors,
    ),
    create=extend_schema(
        request=OctoPrintInstallSerializer,
        responses={
            201: OctoPrintInstallSerializer,
        }
        | generic_create_errors,
    ),
    update=extend_schema(
        request=OctoPrintInstallSerializer,
        responses={
            202: OctoPrintInstallSerializer,
        }.update(generic_update_errors),
    ),
    tags=["octoprint"],
)
class OctoPrintInstallViewSet(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    UpdateModelMixin,
):
    serializer_class = OctoPrintInstallSerializer
    queryset = OctoPrintInstall.objects.all()
    lookup_field = "id"

    @extend_schema(
        operation_id="octoprint_install_update_or_create",
        responses={
            # 400: PrinterProfileSerializer,
            200: OctoPrintInstallSerializer,
            201: OctoPrintInstallSerializer,
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
        responses={
            200: OctoPrintSettingsSerializer(),
        }
        | generic_list_errors,
    ),
    create=extend_schema(
        request=OctoPrintSettingsSerializer,
        responses={
            201: OctoPrintSettingsSerializer,
        }
        | generic_create_errors,
    ),
    update=extend_schema(
        request=OctoPrintSettingsSerializer,
        responses={
            202: OctoPrintSettingsSerializer,
        }.update(generic_update_errors),
    ),
    tags=["octoprint"],
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
        responses={200: OctoPrintBackupSerializer(many=True)} | generic_list_errors
    ),
    create=extend_schema(
        request=OctoPrintBackupSerializer,
        responses={201: OctoPrintBackupSerializer} | generic_create_errors,
    ),
    retrieve=extend_schema(
        request=OctoPrintBackupSerializer,
        responses={200: OctoPrintBackupSerializer} | generic_get_errors,
    ),
    tags=["octoprint"],
)
class OctoPrintBackupViewset(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
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
        responses={
            200: GcodeFileSerializer(),
        }
        | generic_list_errors,
    ),
    create=extend_schema(
        request=GcodeFileSerializer,
        responses={
            201: GcodeFileSerializer,
        }
        | generic_create_errors,
    ),
    retrieve=extend_schema(
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
        responses={
            200: OctoPrinterProfileSerializer(),
        }
        | generic_list_errors,
    ),
    create=extend_schema(
        request=OctoPrinterProfileSerializer,
        responses={
            201: OctoPrinterProfileSerializer,
        }
        | generic_create_errors,
    ),
    update=extend_schema(
        request=OctoPrinterProfileSerializer,
        responses={
            202: OctoPrinterProfileSerializer,
        }.update(generic_update_errors),
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
