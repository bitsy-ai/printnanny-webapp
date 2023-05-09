from django.db import models


class VideoRecordingStatus(models.TextChoices):
    PENDING = "pending", "Video recording is starting"
    INPROGRESS = "inprogress", "Video recording in-progress"
    DONE = "done", "Video recording finished"


class DemoSubmissionFeedbackEnum(models.TextChoices):
    PASS = "pass", "Submission received positive (thumbs up) feedback"
    FAIL = "fail", "Submission received negative (thumbs down) feedback"
    NOT_APPLICABLE = "na", "Submission received N/A (not applicable)"
