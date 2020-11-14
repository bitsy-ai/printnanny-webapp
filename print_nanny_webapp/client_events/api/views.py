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
from drf_spectacular.utils import extend_schema

from .serializers import OctoPrintEventSerializer, PredictEventSerializer, PrinterProfileSerializer, PrintJobSerializer, GcodeFileSerializer


from ..models import OctoPrintEvent, PredictEvent, PrinterProfile, PrintJob, GcodeFile

class PrintJobViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = PrintJobSerializer
    queryset = PrintJob.objects.all()

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id)
        
class OctoPrintEventViewSet(CreateModelMixin, GenericViewSet, ListModelMixin):
    serializer_class = OctoPrintEventSerializer
    queryset = OctoPrintEvent.objects.all()
    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PredictEventViewSet(CreateModelMixin, GenericViewSet):
    # MultiPartParser AND FormParser
    # https://www.django-rest-framework.org/api-guide/parsers/#multipartparser
    # "You will typically want to use both FormParser and MultiPartParser
    # together in order to fully support HTML form data."
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = PredictEventSerializer
    queryset = PredictEvent.objects.all()


    def preform_create(self, serializer):
        #printer = 
        serializer.save(
            user=self.request.user
        )

class PrinterProfileViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = PrinterProfileSerializer
    queryset = PrinterProfile.objects.all()

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id)
    
    @extend_schema(operation_id='printer_profiles_update_or_create')
    @action(methods=['post'], detail=False)
    def update_or_create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            instance, created = serializer.update_or_create(serializer.validated_data, request.user)
            if not created:
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GcodeFileViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = GcodeFileSerializer
    queryset = GcodeFile.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ('name', 'file_hash')

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id)

    @extend_schema(operation_id='gcode_files_update_or_create')
    @action(methods=['post'], detail=False)
    def update_or_create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            instance, created = serializer.update_or_create(serializer.validated_data, request.user)
            if not created:
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
