import logging
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiParameter,
)
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
    OctoPrintSettingsSerializer,
)
from print_nanny_webapp.octoprint.models import OctoPrintBackup, OctoPrintSettings
from print_nanny_webapp.utils.api.views import (
    generic_create_errors,
    generic_list_errors,
    generic_update_errors,
    generic_get_errors,
)


logger = logging.getLogger(__name__)

##
# OctoPrint Settings
##
@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
        ],
        responses={
            200: OctoPrintSettingsSerializer(),
        }
        | generic_list_errors,
    ),
    create=extend_schema(
        parameters=[
            OpenApiParameter(
                name="device_id", type=int, location=OpenApiParameter.PATH
            ),
        ],
        request=OctoPrintSettingsSerializer,
        responses={
            201: OctoPrintSettingsSerializer,
        }
        | generic_create_errors,
    ),
    update=extend_schema(
        parameters=[
            OpenApiParameter(
                name="device_id", type=int, location=OpenApiParameter.PATH
            ),
        ],
        request=OctoPrintSettingsSerializer,
        responses={
            202: OctoPrintSettingsSerializer,
        }.update(generic_update_errors),
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
        operation_id="octoprint_settings_device_update_or_create",
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
