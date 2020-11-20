from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSet
#from drf_yasg.utils import swagger_auto_schema
#from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.parsers  import MultiPartParser, FormParser, JSONParser, FileUploadParser
import django_filters.rest_framework
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter

from .serializers import (
    OctoPrintEventSerializer, 
    PredictEventFileSerializer,
    PredictEventSerializer, 
    PrinterProfileSerializer, 
    PrintJobSerializer, 
    GcodeFileSerializer
)

import print_nanny_webapp.client_events.metrics
from print_nanny_webapp.client_events.models import (
    OctoPrintEvent, PredictEvent, PrinterProfile, PrintJob, GcodeFile, PredictEventFile    
)

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


           
class OctoPrintEventViewSet(CreateModelMixin, GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = OctoPrintEventSerializer
    queryset = OctoPrintEvent.objects.all()
    lookup_field = "id"

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id)
    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)


class PredictEventFileViewSet(CreateModelMixin, GenericViewSet, ListModelMixin, RetrieveModelMixin):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = PredictEventFileSerializer
    queryset = PredictEventFile.objects.all()
    lookup_field = "id"

  
@extend_schema_view(
    list=extend_schema(
        responses={
        201: PredictEventSerializer,
        202: PredictEventSerializer
        })
)
class PredictEventViewSet(CreateModelMixin, GenericViewSet, ListModelMixin, RetrieveModelMixin):
    # MultiPartParser AND FormParser
    # https://www.django-rest-framework.org/api-guide/parsers/#multipartparser
    # "You will typically want to use both FormParser and MultiPartParser
    # together in order to fully support HTML form data."
    serializer_class = PredictEventSerializer
    queryset = PredictEvent.objects.all()
    lookup_field = "id"

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

        
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