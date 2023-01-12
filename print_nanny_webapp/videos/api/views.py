import logging

from drf_spectacular.utils import extend_schema_view, extend_schema

from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
)
from rest_framework import parsers


from print_nanny_webapp.videos.models import VideoRecording
from print_nanny_webapp.videos.api.serializers import VideoRecordingSerializer
from print_nanny_webapp.utils.api.views import (
    generic_create_errors,
    generic_list_errors,
    generic_update_errors,
)

logger = logging.getLogger(__name__)


@extend_schema_view(
    create=extend_schema(
        tags=["crash-reports"],
        request=VideoRecordingSerializer,
        responses={201: VideoRecordingSerializer} | generic_create_errors,
    ),
    list=extend_schema(
        tags=["crash-reports"],
        responses={
            200: VideoRecordingSerializer(many=True),
        }
        | generic_list_errors,
    ),
    update=extend_schema(
        tags=["crash-reports"],
        request=VideoRecordingSerializer,
        responses={
            202: VideoRecordingSerializer,
        }
        | generic_update_errors,
    ),
    partial_update=extend_schema(
        tags=["crash-reports"],
        request=VideoRecordingSerializer,
        responses={
            202: VideoRecordingSerializer,
        }
        | generic_update_errors,
    ),
)
class VideoRecordingViewSet(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
):
    serializer_class = VideoRecordingSerializer
    lookup_field = "id"
    queryset = VideoRecording.objects.all()

    parser_classes = [
        parsers.MultiPartParser,
    ]
