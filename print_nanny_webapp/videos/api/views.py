import logging

from drf_spectacular.utils import extend_schema_view, extend_schema

from rest_framework.response import Response
from rest_framework.decorators import action
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
from rest_framework import status


from print_nanny_webapp.videos.models import VideoRecording
from print_nanny_webapp.videos.api.serializers import VideoRecordingSerializer
from print_nanny_webapp.utils.api.views import (
    generic_get_errors,
    generic_create_errors,
    generic_list_errors,
    generic_update_errors,
)

logger = logging.getLogger(__name__)


@extend_schema_view(
    create=extend_schema(
        tags=["videos"],
        request=VideoRecordingSerializer,
        responses={201: VideoRecordingSerializer} | generic_create_errors,
    ),
    list=extend_schema(
        tags=["videos"],
        responses={
            200: VideoRecordingSerializer(many=True),
        }
        | generic_list_errors,
    ),
    update=extend_schema(
        tags=["videos"],
        request=VideoRecordingSerializer,
        responses={
            202: VideoRecordingSerializer,
        }
        | generic_update_errors,
    ),
    partial_update=extend_schema(
        tags=["videos"],
        request=VideoRecordingSerializer,
        responses={
            202: VideoRecordingSerializer,
        }
        | generic_update_errors,
    ),
    retrieve=extend_schema(
        tags=["videos"],
        request=VideoRecordingSerializer,
        responses={
            200: VideoRecordingSerializer,
        }
        | generic_get_errors,
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

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @extend_schema(
        operation_id="video_recordings_update_or_create",
        tags=["videos"],
        responses={
            200: VideoRecordingSerializer,
            202: VideoRecordingSerializer,
        }
        | generic_create_errors
        | generic_get_errors,
    )
    @action(methods=["post"], detail=False, url_path="update-or-create")
    def update_or_create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        pk = validated_data.pop("id")
        instance, created = serializer.update_or_create(  # type: ignore[attr-defined]
            pk, request.user.id, serializer.validated_data
        )
        response_serializer = self.get_serializer(instance)
        if created:
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(response_serializer.data, status=status.HTTP_200_OK)
