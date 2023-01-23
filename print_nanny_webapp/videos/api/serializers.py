from typing import Tuple, Optional
from rest_framework import serializers

from print_nanny_webapp.videos.models import VideoRecording


class VideoRecordingSerializer(serializers.ModelSerializer):
    mp4_upload_url = serializers.SerializerMethodField()

    def get_mp4_upload_url(self, obj) -> str:
        return obj.mp4_upload_url()

    mp4_size = serializers.SerializerMethodField()

    def get_mp4_size(self, obj) -> Optional[str]:
        return obj.mp4_size()

    class Meta:
        model = VideoRecording
        exclude = ("deleted",)
        read_only_fields = ("mp4_upload_url", "user", "mp4_size")

    def update_or_create(
        self,
        pk,
        user,
        validated_data,
    ) -> Tuple[VideoRecording, bool]:

        try:
            obj = VideoRecording.objects.get(id=pk, user=user)
            for key, value in validated_data:
                setattr(obj, key, value)
            obj.save()
            return obj, False
        except VideoRecording.DoesNotExist:
            obj = VideoRecording(id=pk, user=user, **validated_data)
            obj.save()
            return obj, True
