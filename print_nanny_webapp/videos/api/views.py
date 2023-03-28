import logging

from drf_spectacular.utils import extend_schema_view, extend_schema
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
)
from rest_framework import status, parsers

from print_nanny_webapp.videos.tasks import finalize_video_recording_task
from print_nanny_webapp.videos.models import VideoRecording, VideoRecordingPart
from print_nanny_webapp.videos.api.serializers import (
    VideoRecordingSerializer,
    VideoRecordingPartSerializer,
)
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

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @extend_schema(
        operation_id="video_recordings_update_or_create",
        tags=["videos"],
        request=VideoRecordingSerializer,
        responses={
            200: VideoRecordingSerializer,
            201: VideoRecordingSerializer,
        }
        | generic_create_errors
        | generic_get_errors,
    )
    @action(methods=["post"], detail=True, url_path="update-or-create")
    def update_or_create(self, request, id=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        instance, created = serializer.update_or_create(  # type: ignore[attr-defined]
            id, request.user, validated_data
        )
        response_serializer = self.get_serializer(instance)
        if created:
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(response_serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        operation_id="video_recordings_finalize",
        tags=["videos"],
        responses={
            202: VideoRecordingSerializer,
        },
    )
    @action(methods=["post"], detail=True, url_path="finalize")
    def finalize(self, request, id=None):
        video_recording = get_object_or_404(
            VideoRecording.objects.filter(id=id, user=request.user)
        )
        task = finalize_video_recording_task.delay(video_recording.id)
        video_recording.finalize_task_id = task.id
        video_recording.save()
        serializer = self.get_serializer(video_recording)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


@extend_schema_view(
    create=extend_schema(
        tags=["videos"],
        request=VideoRecordingPartSerializer,
        responses={201: VideoRecordingPartSerializer} | generic_create_errors,
    ),
    list=extend_schema(
        tags=["videos"],
        responses={
            200: VideoRecordingPartSerializer(many=True),
        }
        | generic_list_errors,
    ),
    retrieve=extend_schema(
        tags=["videos"],
        request=VideoRecordingPartSerializer,
        responses={
            200: VideoRecordingPartSerializer,
        }
        | generic_get_errors,
    ),
)
class VideoRecordingPartViewSet(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
):
    serializer_class = VideoRecordingPartSerializer
    lookup_field = "id"
    queryset = VideoRecordingPart.objects.all()
    parser_classes = [
        parsers.MultiPartParser,
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
