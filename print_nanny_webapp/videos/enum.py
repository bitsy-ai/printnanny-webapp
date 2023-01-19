from django.db import models


class VideoRecordingStatus(models.TextChoices):
    PENDING = "pending", "Video recording is starting"
    INPROGRESS = "inprogress", "Video recording in-progress"
    DONE = "done", "Video recording finished"
