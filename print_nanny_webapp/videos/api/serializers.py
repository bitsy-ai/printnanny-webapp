from rest_framework import serializers

from print_nanny_webapp.videos.models import VideoRecording


class VideoRecordingSerializer(serializers.ModelSerializer):
    mjr_upload_url = serializers.SerializerMethodField()

    def get_mjr_upload_url(self, obj) -> str:
        return obj.mjr_upload_url()

    class Meta:
        model = VideoRecording
        exclude = ("deleted",)
        read_only_fields = ("id", "mjr_upload_url", "user")
