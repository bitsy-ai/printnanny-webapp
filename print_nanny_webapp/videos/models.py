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


def snapshot_filepath(instance, filename):
    path = timezone.now().strftime("uploads/camera_snapshots/%Y/%m/%d")
    return f"{path}/{instance.id}.jpg"


def challenge_campaign_submission_filepath(instance, filename):
    path = timezone.now().strftime("uploads/challenge_campaign_submission/%Y/%m/%d")
    return f"{path}/{filename}.jpg"


def challenge_campaign_result_filepath(instance, filename):
    path = timezone.now().strftime("uploads/challenge_campaign_result/%Y/%m/%d")
    return f"{path}/{filename}.jpg"


class ChallengeCampaignLead(models.Model):
    """
    Uploaded an image to "PrintNanny challenge" marketing campaign
    """

    class Meta:
        ordering = ["-created_dt"]
        index_together = [["id", "created_dt", "email"]]

    created_dt = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    submission = models.FileField(upload_to=challenge_campaign_submission_filepath)
    result = models.FileField(upload_to=challenge_campaign_result_filepath)


class CameraSnapshot(models.Model):
    class Meta:
        ordering = ["-created_dt"]
        index_together = [["id", "pi", "created_dt"]]

    id = models.UUIDField(primary_key=True, default=uuid4)
    pi = models.ForeignKey(
        "devices.Pi", on_delete=models.CASCADE, related_name="camera_snapshots"
    )
    created_dt = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to=snapshot_filepath)


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
