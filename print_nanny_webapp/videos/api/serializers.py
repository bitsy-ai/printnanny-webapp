from rest_framework import serializers

from print_nanny_webapp.videos.models import VideoRecording


class VideoRecordingSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, obj) -> str:
        return f"/crash-reports/{obj.id}/"

    class Meta:
        model = VideoRecording
        exclude = ("deleted",)
        read_only_fields = ("id", "url")
