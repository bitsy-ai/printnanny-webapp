from django.db import models
from django.contrib.auth import get_user_model
from safedelete.models import SafeDeleteModel
from uuid import uuid4

from .enum import VideoRecordingStatus

# Create your models here.

User = get_user_model()


def mp4_filepath(instance, filename):
    path = instance.created_dt.strftime("uploads/video_recordings/mp4/%Y/%m/%d")
    return f"{path}/{instance.id}.mp4"


class VideoRecording(SafeDeleteModel):
    """
    A video recording
    """

    id = models.UUIDField(primary_key=True, default=uuid4)
    created_dt = models.DateTimeField(auto_now_add=True)

    recording_start = models.DateTimeField(null=True)
    recording_end = models.DateTimeField(null=True)
    recording_status = models.CharField(
        max_length=32,
        choices=VideoRecordingStatus.choices,
        default=VideoRecordingStatus.PENDING,
    )

    cloud_sync_start = models.DateTimeField(null=True)
    cloud_sync_end = models.DateTimeField(null=True)
    cloud_sync_status = models.CharField(
        max_length=32,
        choices=VideoRecordingStatus.choices,
        default=VideoRecordingStatus.PENDING,
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    gcode_file_name = models.CharField(max_length=255, null=True)
    mp4_file = models.FileField(upload_to=mp4_filepath, null=True)

    def mp4_upload_url(self):
        name = mp4_filepath(self, None)
        return self.mp4_file.storage.upload_url(name)
