from typing import Tuple
from rest_framework import serializers

from print_nanny_webapp.videos.models import VideoRecording


class VideoRecordingSerializer(serializers.ModelSerializer):
    mp4_upload_url = serializers.SerializerMethodField()

    def get_mp4_upload_url(self, obj) -> str:
        return obj.mp4_upload_url()

    class Meta:
        model = VideoRecording
        exclude = ("deleted",)
        read_only_fields = ("mp4_upload_url", "user")

    def update_or_create(
        self,
        pk,
        user,
        validated_data,
    ) -> Tuple[VideoRecording, bool]:
        return VideoRecording.objects.filter(id=pk, user=user).update_or_create(
            id=pk, user=user, defaults=validated_data
        )
