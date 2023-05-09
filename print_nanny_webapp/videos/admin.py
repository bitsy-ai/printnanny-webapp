from django.contrib import admin
from print_nanny_webapp.videos.models import (
    VideoRecording,
    VideoRecordingPart,
    CameraSnapshot,
    DemoSubmission,
)


# Register your models here.


@admin.register(DemoSubmission)
class DemoSubmissionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "created_dt",
        "result",
    )
    model = DemoSubmission


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


@admin.register(CameraSnapshot)
class CameraSnapshotAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "pi",
        "created_dt",
        "image",
    )
    model = CameraSnapshot
