import logging

from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
)
from rest_framework.permissions import AllowAny
from rest_framework import status, parsers

from print_nanny_webapp.videos.tasks import finalize_video_recording_task, demo_task
from print_nanny_webapp.videos.models import (
    CameraSnapshot,
    VideoRecording,
    VideoRecordingPart,
    DemoSubmission,
)
from print_nanny_webapp.videos.api.serializers import (
    CameraSnapshotSerializer,
    VideoRecordingSerializer,
    VideoRecordingPartSerializer,
    VideoRecordingFinalizeSerializer,
    DemoSubmissionSerializer,
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
        request=VideoRecordingFinalizeSerializer,
        responses={
            202: VideoRecordingSerializer,
        },
    )
    @action(methods=["post"], detail=True, url_path="finalize")
    def finalize(self, request, id=None):
        request_serializer = VideoRecordingFinalizeSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)
        recording_end = request_serializer.validated_data["recording_end"]
        video_recording = get_object_or_404(
            VideoRecording.objects.filter(id=id, user=request.user)
        )
        video_recording.recording_end = recording_end
        video_recording.cloud_sync_done = True

        task = finalize_video_recording_task.delay(video_recording.id)
        video_recording.finalize_task_id = task.id
        video_recording.save()
        response_serializer = self.get_serializer(video_recording)
        return Response(response_serializer.data, status=status.HTTP_202_ACCEPTED)


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


@extend_schema_view(
    retrieve=extend_schema(
        tags=["videos"],
        parameters=[
            OpenApiParameter(name="pi_id", type=int, location=OpenApiParameter.PATH)
        ],
        responses={200: CameraSnapshotSerializer(many=False)} | generic_get_errors,
    ),
    list=extend_schema(
        tags=["videos"],
        parameters=[
            OpenApiParameter(name="pi_id", type=int, location=OpenApiParameter.PATH)
        ],
        responses={
            200: CameraSnapshotSerializer(many=True),
        }
        | generic_list_errors,
    ),
    create=extend_schema(
        tags=["videos"],
        parameters=[
            OpenApiParameter(name="pi_id", type=int, location=OpenApiParameter.PATH)
        ],
        request=CameraSnapshotSerializer,
        responses={201: CameraSnapshotSerializer} | generic_create_errors,
    ),
)
class CameraSnapshotViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
):
    serializer_class = CameraSnapshotSerializer
    queryset = CameraSnapshot.objects.all()
    lookup_field = "id"

    parser_classes = [parsers.MultiPartParser]

    def get_queryset(self, *args, **kwargs):
        result = self.queryset.filter(pi__user_id=self.request.user.id)
        return result


@extend_schema_view(
    create=extend_schema(
        tags=["videos"],
        request=DemoSubmissionSerializer,
        responses={201: DemoSubmissionSerializer} | generic_create_errors,
    ),
)
class DemoSubmissionViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin):
    serializer_class = DemoSubmissionSerializer
    queryset = DemoSubmission.objects.all()
    parser_classes = [parsers.MultiPartParser]
    permission_classes = (AllowAny,)
    # omit OwnerOrUserFilterBackend, which is a DEFAULT_FILTER_BACKENDS
    filter_backends = [DjangoFilterBackend]

    def perform_create(self, serializer):
        obj = serializer.save()
        task = demo_task.delay(obj.id)
        logger.info("DemoSubmissionViewSet created demo_task %s", task)
