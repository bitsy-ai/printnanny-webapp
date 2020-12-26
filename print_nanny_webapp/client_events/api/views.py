from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSet

# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.parsers import (
    MultiPartParser,
    FormParser,
    JSONParser,
    FileUploadParser,
)
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from django.apps import apps

from .serializers import (
    OctoPrintEventSerializer,
    PredictEventFileSerializer,
    PredictEventSerializer,
)
from print_nanny_webapp.client_events.models import (
    OctoPrintEvent,
    PredictEvent,
    PredictEventFile,
)

PrintJob = apps.get_model("remote_control", "PrintJob")

# def get_queryset(self, *args, **kwargs):
#     return [x.value for x in OctoPrintEvent.EventTypeChoices.__members__.values()]


@extend_schema(tags=["events"])
@extend_schema_view(
    create=extend_schema(
        responses={201: OctoPrintEventSerializer, 400: OctoPrintEventSerializer}
    )
)
class OctoPrintEventViewSet(
    CreateModelMixin, GenericViewSet, ListModelMixin, RetrieveModelMixin
):
    serializer_class = OctoPrintEventSerializer
    queryset = OctoPrintEvent.objects.all()
    lookup_field = "id"

    @extend_schema(
        tags=["events"],
        operation_id="octoprint_events_tracking_retrieve",
        responses={200: OpenApiTypes.STR},
    )
    @action(methods=["GET"], detail=False)
    def tracking(self, *args, **kwargs):
        return Response(
            [x.value for x in OctoPrintEvent.EventTypeChoices.__members__.values()],
            status.HTTP_200_OK,
        )

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id)

    def perform_create(self, serializer):

        event_data = self.request.data["event_data"]

        print_job = event_data.get("print_job")
        if print_job is not None:
            print_job = PrintJob.objects.get(id=print_job)
        if self.request.user:
            user = self.request.user
        else:
            user = None
        instance = serializer.save(user=user, print_job=print_job)


@extend_schema(tags=["events"])
@extend_schema_view(
    create=extend_schema(
        responses={201: PredictEventFileSerializer, 400: PredictEventFileSerializer}
    )
)
class PredictEventFileViewSet(
    CreateModelMixin, GenericViewSet, ListModelMixin, RetrieveModelMixin
):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = PredictEventFileSerializer
    queryset = PredictEventFile.objects.all()
    lookup_field = "id"


@extend_schema(tags=["events"])
@extend_schema_view(
    create=extend_schema(responses={201: OpenApiTypes.INT, 400: PredictEventSerializer})
)
class PredictEventViewSet(
    CreateModelMixin, GenericViewSet, ListModelMixin, RetrieveModelMixin
):
    # MultiPartParser AND FormParser
    # https://www.django-rest-framework.org/api-guide/parsers/#multipartparser
    # "You will typically want to use both FormParser and MultiPartParser
    # together in order to fully support HTML form data."
    serializer_class = PredictEventSerializer
    queryset = PredictEvent.objects.all()
    lookup_field = "id"

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data["id"], status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
