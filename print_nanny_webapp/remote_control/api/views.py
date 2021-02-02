from asgiref.sync import async_to_sync
import logging
from django.apps import apps
from django.core.files.base import ContentFile

from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSet
from rest_framework.decorators import action
from rest_framework import status

from drf_spectacular.utils import extend_schema, extend_schema_view
from drf_spectacular.types import OpenApiTypes

from rest_framework.renderers import JSONRenderer

from rest_framework.parsers import (
    MultiPartParser,
    FormParser,
    JSONParser,
    FileUploadParser,
)
import django_filters.rest_framework

from .serializers import (
    PrinterProfileSerializer,
    PrintJobSerializer,
    GcodeFileSerializer,
    OctoPrintDeviceSerializer,
    OctoPrintDeviceKeySerializer,
    RemoteControlCommandSerializer,
    RemoteControlSnapshotSerializer,
    RemoteControlSnapshotCreateResponseSerializer
)

from print_nanny_webapp.alerts.api.serializers import AlertPolymorphicSerializer
from print_nanny_webapp.remote_control.models import (
    PrinterProfile,
    PrintJob,
    GcodeFile,
    OctoPrintDevice,
    RemoteControlCommand,
    RemoteControlSnapshot,
)

from print_nanny_webapp.alerts.tasks.remote_control_command_alert import (
    create_remote_control_command_alerts,
)


import google.api_core.exceptions

from print_nanny_webapp.utils import prometheus_metrics

logger = logging.getLogger(__name__)

RemoteControlCommandAlert = apps.get_model("alerts", "RemoteControlCommandAlert")


@extend_schema(tags=["remote-control"])
@extend_schema_view(
    create=extend_schema(responses={201: PrintJobSerializer, 400: PrintJobSerializer})
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

    @extend_schema(
        tags=["remote_control"],
        operation_id="valid_commands_retrieve",
        responses={200: OpenApiTypes.STR},
    )
    @action(methods=["GET"], detail=False)
    def valid(self, *args, **kwargs):
        return Response(
            RemoteControlCommand.COMMAND_CODES,
            status.HTTP_200_OK,
        )

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

        alert_subtype = RemoteControlCommandAlert.get_alert_subtype(request.data)
        if alert_subtype is not None:

            task = create_remote_control_command_alerts.delay(
                request.user.id, instance.id, alert_subtype.value
            )
            logger.info(f"Created create_remote_control_command_alerts task {task}")

        return Response(serializer.data)


@extend_schema(tags=["remote-control"])
@extend_schema_view(
    create=extend_schema(responses={201: PrintJobSerializer, 400: PrintJobSerializer})
)
class PrintJobViewSet(
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):
    serializer_class = PrintJobSerializer
    queryset = PrintJob.objects.all()
    lookup_field = "id"
    basename = "print-job"  # users for view name generation e.g. "print-job-detail"

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id)

    @extend_schema(
        tags=["remote-control"],
        operation_id="print_jobs_create",
        responses={400: PrintJobSerializer, 201: PrintJobSerializer},
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    @extend_schema(
        tags=["remote-control"],
        operation_id="print_jobs_update",
        responses={400: PrintJobSerializer, 200: PrintJobSerializer},
    )
    def update(self, *args, **kwargs):
        return super().update(*args, **kwargs)

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)
        prometheus_metrics.print_job_status.state(instance.last_status)

    def perform_update(self, serializer):

        instance = serializer.save()
        if (
            instance.progress > 0
            and instance % user.user_settings.alert_on_progress_percent == 0
        ):
            create_progress_video_task.delay(instance.id, instance.progress)
        prometheus_metrics.print_job_status.state(instance.last_status)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        tags=["remote-control"],
        operation_id="print_jobs_partial_update",
        responses={400: PrintJobSerializer, 200: PrintJobSerializer},
    )
    def partial_update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return self.update(request, *args, **kwargs)


@extend_schema(tags=["remote-control"])
class PrinterProfileViewSet(
    CreateModelMixin,
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
        responses={400: PrintJobSerializer, 201: PrintJobSerializer},
    )
    def create(self, *args, **kwargs):
        return super().create(*args, **kwargs)

    @extend_schema(
        operation_id="printer_profiles_update_or_create",
        responses={
            400: PrinterProfileSerializer,
            200: PrinterProfileSerializer,
            201: PrinterProfileSerializer,
        },
    )
    @action(methods=["post"], detail=False)
    def update_or_create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            instance, created = serializer.update_or_create(
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
class RemoteControlSnapshotViewSet(
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = RemoteControlSnapshotSerializer
    queryset = RemoteControlSnapshot.objects.all()
    lookup_field = "id"

    @extend_schema(
        tags=["remote-control"],
        operation_id="snapshots_create",
        responses={
            400: RemoteControlSnapshotSerializer,
            201: RemoteControlSnapshotCreateResponseSerializer,
        },
    )
    def create(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # https://github.com/aio-libs/aiohttp/issues/3652
            # octoprint_device is accepted as a string and deserialized to an integer
            instance = serializer.create(serializer.validated_data)
            response_serializer = RemoteControlSnapshotCreateResponseSerializer(instance=instance, context={'request': self.request})
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=["remote-control"])
class GcodeFileViewSet(
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = GcodeFileSerializer
    queryset = GcodeFile.objects.all()
    lookup_field = "id"

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id)

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
    @action(methods=["post"], detail=False)
    def update_or_create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # https://github.com/aio-libs/aiohttp/issues/3652
            # octoprint_device is accepted as a string and deserialized to an integer
            octoprint_device = OctoPrintDevice.objects.get(
                id=int(serializer.validated_data["octoprint_device"])
            )
            serializer.validated_data["octoprint_device"] = octoprint_device
            instance, created = serializer.update_or_create(
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
    CreateModelMixin,
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
    @action(methods=["post"], detail=False)
    def update_or_create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data.copy()
            del validated_data["serial"]
            instance, created = serializer.update_or_create(
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
        responses={
            400: OctoPrintDeviceSerializer,
            200: OctoPrintDeviceSerializer,
            202: OctoPrintDeviceSerializer,
        },
    )
    def update(self, *args, **kwargs):
        return super().update(*args, **kwargs)

    @extend_schema(
        operation_id="octoprint_devices_partial_update",
        responses={
            400: OctoPrintDeviceSerializer,
            200: OctoPrintDeviceSerializer,
            202: OctoPrintDeviceSerializer,
        },
    )
    def partial_update(self, *args, **kwargs):
        return super().partial_update(*args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
