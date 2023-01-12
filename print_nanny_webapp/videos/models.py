from django.db import models
from django.contrib.auth import get_user_model
from safedelete.models import SafeDeleteModel, SafeDeleteManager

# Create your models here.

User = get_user_model()


def mjr_recording_filepath(instance, filename):
    path = instance.created_dt.strftime("uploads/mjr_recording/%Y/%m/%d")
    return f"{path}/{instance.id}/{filename}"


class VideoRecording(SafeDeleteModel):
    """
    A video recording
    """

    start_dt = models.DateTimeField()
    end_dt = models.DateTimeField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    # mjr is a Janus recording format, which is basically a stream of RTP packets: https://janus.conf.meetecho.com/docs/recordplay.html
    mjr_recording = models.FileField(upload_to=mjr_recording_filepath, null=True)
