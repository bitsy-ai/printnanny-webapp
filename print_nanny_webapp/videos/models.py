from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

import google.api_core.exceptions

from safedelete.models import SafeDeleteModel
from uuid import uuid4
from .enum import VideoRecordingStatus

# Create your models here.

User = get_user_model()


def final_mp4_filepath(instance, filename):
    return f"uploads/video_recordings/{instance.id}/final.mp4"


def part_mp4_filepath(instance, filename):
    return f"{instance.mp4_parts_path()}{instance.buffer_index}.mp4"


class VideoRecording(SafeDeleteModel):
    """
    A video recording
    """

    id = models.UUIDField(primary_key=True, default=uuid4)
    cloud_sync_done = models.BooleanField(default=False)

    finalize_start = models.DateTimeField(null=True)
    finalize_end = models.DateTimeField(null=True)
    finalize_task_id = models.CharField(max_length=255, null=True)

    recording_start = models.DateTimeField(null=True)
    recording_end = models.DateTimeField(null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    gcode_file_name = models.CharField(max_length=255, null=True)
    mp4_file = models.FileField(upload_to=final_mp4_filepath, null=True)

    def mp4_parts_path(self) -> str:
        return f"uploads/video_recordings/{self.id}/parts/"

    def gsutil_pattern(self) -> str:
        return f"uploads/video_recordings/{self.id}/parts/*.mp4"

    def mp4_upload_url(self):
        name = final_mp4_filepath(self, None)
        return self.mp4_file.storage.upload_url(name)

    def mp4_size(self) -> int:
        if self.mp4_file is not None:
            name = final_mp4_filepath(self, None)
            try:
                return self.mp4_file.storage.size(name)
            except google.api_core.exceptions.NotFound:
                return 0
        return 0


class VideoRecordingPart(SafeDeleteModel):
    id = models.CharField(primary_key=True, max_length=255)
    size = models.BigIntegerField()

    buffer_index = models.BigIntegerField()
    buffer_runningtime = models.BigIntegerField()

    file_name = models.CharField(max_length=255)

    mp4_file = models.FileField(upload_to=part_mp4_filepath)
    sync_start = models.DateTimeField()
    sync_end = models.DateTimeField(auto_now_add=True)

    video_recording = models.ForeignKey(
        VideoRecording, on_delete=models.CASCADE, related_name="video_recording_parts"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def mp4_size(self) -> int:
        if self.mp4_file is not None:
            name = part_mp4_filepath(self, None)
            try:
                return self.mp4_file.storage.size(name)
            except google.api_core.exceptions.NotFound:
                return 0
        return 0

    def mp4_parts_path(self) -> str:
        return self.video_recording.mp4_parts_path()
