from django.contrib import admin
from print_nanny_webapp.videos.models import VideoRecording, VideoRecordingPart

# Register your models here.
@admin.register(VideoRecording)
class VideoRecordingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "recording_start",
        "recording_end",
        "cloud_sync_done",
    )
    model = VideoRecording


@admin.register(VideoRecordingPart)
class VideoRecordingPartAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "buffer_index",
        "video_recording",
        "sync_start",
        "sync_end",
    )
    model = VideoRecordingPart
