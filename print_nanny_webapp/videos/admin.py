from django.contrib import admin
from print_nanny_webapp.videos.models import VideoRecording

# Register your models here.
@admin.register(VideoRecording)
class VideoRecordingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "recording_start",
        "recording_end",
        "capture_done",
        "cloud_sync_done",
        "combine_done",
        "user",
    )
    model = VideoRecording
