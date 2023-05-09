from typing import Tuple, Optional
from rest_framework import serializers

from print_nanny_webapp.videos.models import (
    CameraSnapshot,
    VideoRecording,
    VideoRecordingPart,
    DemoSubmission,
)


class DemoSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemoSubmission
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_dt",
            "result",
            "feedback_nozzle",
            "feedback_spaghetti",
            "feedback_adhesion",
            "feedback_print",
            "feedback_raft",
        )


class DemoSubmissionFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemoSubmission
        fields = "__all__"
        read_only_fields = ("id", "created_dt", "result", "submission", "email")


class VideoRecordingFinalizeSerializer(serializers.Serializer):
    recording_end = serializers.DateTimeField()


class VideoRecordingSerializer(serializers.ModelSerializer):
    mp4_size = serializers.SerializerMethodField()

    def get_mp4_size(self, obj) -> Optional[int]:
        return obj.mp4_size()

    class Meta:
        model = VideoRecording
        exclude = ("deleted", "deleted_by_cascade")
        read_only_fields = (
            "user",
            "mp4_size",
            "mp4_file",
            "finalize_task_id",
        )

    def update_or_create(
        self,
        pk,
        user,
        validated_data,
    ) -> Tuple[VideoRecording, bool]:
        try:
            obj = VideoRecording.objects.get(id=pk, user=user)
            for key, value in validated_data.items():
                setattr(obj, key, value)
            obj.save()
            return (obj, False)
        except VideoRecording.DoesNotExist:
            obj = VideoRecording(id=pk, user=user, **validated_data)
            obj.save()
            return (obj, True)


class VideoRecordingPartSerializer(serializers.ModelSerializer):
    def get_mp4_size(self, obj) -> Optional[int]:
        return obj.mp4_size()

    class Meta:
        model = VideoRecordingPart
        exclude = ("deleted",)
        read_only_fields = ("mp4_size", "user", "sync_end")


class CameraSnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = CameraSnapshot
        fields = "__all__"
        read_only_fields = ("id", "created_dt")
