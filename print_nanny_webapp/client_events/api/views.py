from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSet
#from drf_yasg.utils import swagger_auto_schema
#from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.parsers  import MultiPartParser, FormParser, JSONParser, FileUploadParser
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter

from .serializers import (
    OctoPrintEventSerializer, 
    PredictEventFileSerializer,
    PredictEventSerializer, 
)
from print_nanny_webapp.client_events.models import (
    OctoPrintEvent, PredictEvent, PredictEventFile
)

@extend_schema(tags=['events'])
class OctoPrintEventViewSet(CreateModelMixin, GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = OctoPrintEventSerializer
    queryset = OctoPrintEvent.objects.all()
    lookup_field = "id"

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id)
    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)

@extend_schema(tags=['events'])
class PredictEventFileViewSet(CreateModelMixin, GenericViewSet, ListModelMixin, RetrieveModelMixin):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = PredictEventFileSerializer
    queryset = PredictEventFile.objects.all()
    lookup_field = "id"

@extend_schema(tags=['events'])
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

