import logging

from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    OptionsCreateModelMixin,
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSet
from rest_framework.decorators import action
from rest_framework import status

from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from drf_spectacular.types import OpenApiTypes

from rest_framework.renderers import JSONRenderer

from rest_framework.parsers import (
    MultiPartParser,
    FormParser,
)
import django_filters.rest_framework

from .serializers import (
    PrinterProfileSerializer,
    PrintSessionSerializer,
    GcodeFileSerializer,
    OctoPrintDeviceSerializer,
    OctoPrintDeviceKeySerializer,
    RemoteControlCommandSerializer,
)

from print_nanny_webapp.remote_control.models import (
    PrinterProfile,
    PrintSession,
    OctoPrintDevice,
    RemoteControlCommand,
)

from django.contrib.auth import get_user_model

User = get_user_model()


import google.api_core.exceptions


logger = logging.getLogger(__name__)


@extend_schema(tags=["remote-control"])
@extend_schema_view(
    create=extend_schema(
        responses={
            201: RemoteControlCommandSerializer,
            400: RemoteControlCommandSerializer,
        }
    )
)
class CommandViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):
    serializer_class = RemoteControlCommandSerializer
    queryset = RemoteControlCommand.objects.all()
    lookup_field = "id"
    basename = "command"

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


@extend_schema(tags=["remote-control"])
@extend_schema_view(
    create=extend_schema(
        responses={201: PrintSessionSerializer, 400: PrintSessionSerializer}
    )
)
class PrintSessionViewSet(
    UpdateModelMixin,
    OptionsCreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    GenericViewSet,
):
    serializer_class = PrintSessionSerializer
    queryset = PrintSession.objects.all()
    lookup_field = "session"
    basename = "print-session"  # users for view name generation e.g. "print-job-detail"

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id)

    @extend_schema(
        tags=["remote-control"],
        operation_id="print_session_update",
        responses={400: PrintSessionSerializer, 200: PrintSessionSerializer},
    )
    def update(self, *args, **kwargs):
        return super().update(*args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(
        tags=["remote-control"],
        operation_id="print_session_partial_update",
        responses={400: PrintSessionSerializer, 200: PrintSessionSerializer},
    )
    def partial_update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return self.update(request, *args, **kwargs)


@extend_schema(tags=["remote-control"])
class PrinterProfileViewSet(
    OptionsCreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):
    serializer_class = PrinterProfileSerializer
    queryset = PrinterProfile.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ("user", "name")
    lookup_field = "id"

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id)

    @extend_schema(
        tags=["remote-control"],
        operation_id="printer_profiles_create",
        responses={400: PrintSessionSerializer, 201: PrintSessionSerializer},
    )
    def create(self, *args, **kwargs):
        return super().create(*args, **kwargs)

    @extend_schema(
        operation_id="printer_profiles_update_or_create",
        responses={
            # 400: PrinterProfileSerializer,
            200: PrinterProfileSerializer,
            201: PrinterProfileSerializer,
        },
    )
    @action(methods=["post"], detail=False, url_path="update-or-create")
    def update_or_create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            instance, created = serializer.update_or_create(  # type: ignore[attr-defined]
                serializer.validated_data, request.user
            )
            response_serializer = self.get_serializer(instance)
            if not created:
                return Response(response_serializer.data, status=status.HTTP_200_OK)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema(tags=["remote-control"])
class GcodeFileViewSet(
    OptionsCreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = GcodeFileSerializer
    lookup_field = "id"

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id).all()  # type: ignore

    @extend_schema(
        tags=["remote-control"],
        operation_id="gcode_files_create",
        responses={400: GcodeFileSerializer, 201: GcodeFileSerializer},
    )
    def create(self, *args, **kwargs):
        return super().create(*args, **kwargs)

    @extend_schema(
        operation_id="gcode_files_update_or_create",
        responses={
            400: GcodeFileSerializer,
            200: GcodeFileSerializer,
            201: GcodeFileSerializer,
        },
    )
    @action(methods=["post"], detail=False, url_path="update-or-create")
    def update_or_create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # https://github.com/aio-libs/aiohttp/issues/3652
            # octoprint_device is accepted as a string and deserialized to an integer
            octoprint_device = OctoPrintDevice.objects.get(
                id=int(serializer.validated_data["octoprint_device"])
            )
            serializer.validated_data["octoprint_device"] = octoprint_device
            instance, created = serializer.update_or_create(  # type: ignore[attr-defined]
                serializer.validated_data, request.user
            )
            response_serializer = self.get_serializer(instance)

            if not created:
                return Response(response_serializer.data, status=status.HTTP_200_OK)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema(tags=["remote-control"])
class OctoPrintDeviceViewSet(
    OptionsCreateModelMixin,
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
):

    serializer_class = OctoPrintDeviceSerializer
    queryset = OctoPrintDevice.objects.all()
    lookup_field = "id"

    @extend_schema(
        operation_id="octoprint_devices_update_or_create",
        responses={
            400: OctoPrintDeviceSerializer,
            200: OctoPrintDeviceSerializer,
            201: OctoPrintDeviceKeySerializer,
            202: OctoPrintDeviceKeySerializer,
        },
    )
    @action(methods=["post"], detail=False, url_path="update-or-create")
    def update_or_create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data.copy()
            del validated_data["serial"]
            instance, created = serializer.update_or_create(  # type: ignore[attr-defined]
                request.user, serializer.validated_data.get("serial"), validated_data
            )

            context = {"request": self.request}
            context.update(self.get_serializer_context())

            response_serializer = OctoPrintDeviceKeySerializer(
                instance=instance, context=context
            )

            if not created:
                return Response(
                    response_serializer.data, status=status.HTTP_202_ACCEPTED
                )
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        operation_id="octoprint_devices_update",
        parameters=[],
        responses={
            # 400: OctoPrintDeviceSerializer,
            200: OctoPrintDeviceSerializer,
            202: OctoPrintDeviceSerializer,
        },
    )
    def update(self, *args, **kwargs):
        return super().update(*args, **kwargs)

    @extend_schema(
        operation_id="octoprint_devices_partial_update",
        responses={
            # 400: OctoPrintDeviceSerializer,
            200: OctoPrintDeviceSerializer,
            202: OctoPrintDeviceSerializer,
        },
    )
    def partial_update(self, *args, **kwargs):
        return super().partial_update(*args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
