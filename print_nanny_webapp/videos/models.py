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
    path = timezone.now().strftime("uploads/video_recordings/mp4/%Y/%m/%d")
    return f"{path}/{instance.id}/final.mp4"


def part_mp4_filepath(instance, filename):
    path = timezone.now().strftime("uploads/video_recordings/mp4/%Y/%m/%d")
    return f"{path}/{instance.id}/part_{instance.part}.mp4"


class VideoRecording(SafeDeleteModel):
    """
    A video recording
    """

    id = models.UUIDField(primary_key=True, default=uuid4)
    cloud_sync_done = models.BooleanField(default=False)
    combine_done = models.BooleanField(default=False)

    recording_start = models.DateTimeField(null=True)
    recording_end = models.DateTimeField(null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    gcode_file_name = models.CharField(max_length=255, null=True)
    mp4_file = models.FileField(upload_to=final_mp4_filepath, null=True)

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
    buffer_ts = models.BigIntegerField()
    buffer_streamtime = models.BigIntegerField()
    buffer_runningtime = models.BigIntegerField()
    buffer_duration = models.BigIntegerField()
    buffer_offset = models.BigIntegerField()
    buffer_offset_end = models.BigIntegerField()

    file_name = models.CharField(max_length=255)

    mp4_file = models.FileField(upload_to=part_mp4_filepath, null=True)
    sync_start = models.DateTimeField(null=True)
    sync_end = models.DateTimeField(null=True)

    video_recording = models.ForeignKey(VideoRecording, on_delete=models.CASCADE)

    def mp4_upload_url(self):
        name = part_mp4_filepath(self, None)
        return self.mp4_file.storage.upload_url(name)

    def mp4_size(self) -> int:
        if self.mp4_file is not None:
            name = part_mp4_filepath(self, None)
            try:
                return self.mp4_file.storage.size(name)
            except google.api_core.exceptions.NotFound:
                return 0
        return 0
