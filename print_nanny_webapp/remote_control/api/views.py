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
)

from print_nanny_webapp.remote_control.models import (
    PrinterProfile,
    PrintJob,
    GcodeFile,
    OctoPrintDevice,
)

import google.api_core.exceptions

from print_nanny_webapp.utils import prometheus_metrics


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
    lookup_field = "id"

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
        responses={400: PrintJobSerializer, 201: PrintJobSerializer},
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


@extend_schema(tags=["remote_control"])
@extend_schema_view(
    create=extend_schema(
        responses={201: OctoPrintDeviceSerializer, 400: OctoPrintDeviceSerializer}
    )
)
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

    # def perform_create(self, serializer):
    #     try:
    #         serializer.save(user=self.request.user)
    #     # a device with this serial already exists
    #     except google.api_core.exceptions.AlreadyExists as e:
    #         exception = (
    #             print_nanny_webapp.client_events.api.exceptions.DeviceAlreadyExists(
    #                 user=self.request.user.id,
    #                 serial=self.request.data["serial"],
    #                 parent_exception=e,
    #             )
    #         )
    #         logger.error(f"{str(exception)} {str(exception.parent_exception)}")
    #         raise exception


    @extend_schema(
        operation_id="octoprint_devices_update_or_create",
        responses={
            400: OctoPrintDeviceSerializer,
            200: OctoPrintDeviceSerializer,
            201: OctoPrintDeviceSerializer,
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