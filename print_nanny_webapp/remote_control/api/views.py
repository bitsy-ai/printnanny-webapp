from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSet
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema
from rest_framework.parsers  import MultiPartParser, FormParser, JSONParser, FileUploadParser
import django_filters.rest_framework

from .serializers import (
    PrinterProfileSerializer, 
    PrintJobSerializer, 
    GcodeFileSerializer
)

from ..models import (
    PrinterProfile, PrintJob, GcodeFile
)

import print_nanny_webapp.utils.prometheus_metrics

class PrintJobViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = PrintJobSerializer
    queryset = PrintJob.objects.all()
    lookup_field = "id"
    basename = "print-job" # users for view name generation e.g. "print-job-detail"
    lookup_field = "id"

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id)

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)
        print_nanny_webapp.client_events.metrics.print_job_status.state(instance.last_status.value)

    def perform_update(self, serializer):
        instance = serializer.save()
        print_nanny_webapp.client_events.metrics.print_job_status.state(instance.last_status)

class PrinterProfileViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = PrinterProfileSerializer
    queryset = PrinterProfile.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ('user', 'name')
    lookup_field = "id"

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id)
    
    @extend_schema(
        operation_id='printer_profiles_update_or_create',
        responses={
            400: PrinterProfileSerializer,
            202: PrinterProfileSerializer,
            201: PrinterProfileSerializer
        }
    )
    @action(methods=['post'], detail=False)
    def update_or_create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            instance, created = serializer.update_or_create(serializer.validated_data, request.user)
            response_serializer = self.get_serializer(instance)
            if not created:
                return Response(response_serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
      
class GcodeFileViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = GcodeFileSerializer
    queryset = GcodeFile.objects.all()
    lookup_field = "id"

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id)

    @extend_schema(
        operation_id='gcode_files_update_or_create',
        responses={
            400: GcodeFileSerializer,
            202: GcodeFileSerializer,
            201: GcodeFileSerializer
        }
    )
    @action(methods=['post'], detail=False)
    def update_or_create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            instance, created = serializer.update_or_create(serializer.validated_data, request.user)
            response_serializer = self.get_serializer(instance)

            if not created:
                return Response(response_serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)