from rest_framework import serializers

from print_nanny_webapp.videos.models import VideoRecording


class VideoRecordingSerializer(serializers.ModelSerializer):
    mp4_upload_url = serializers.SerializerMethodField()

    def get_mp4_upload_url(self, obj) -> str:
        return obj.mp4_upload_url()

    class Meta:
        model = VideoRecording
        exclude = ("deleted",)
        read_only_fields = ("id", "mp4_upload_url", "user")
