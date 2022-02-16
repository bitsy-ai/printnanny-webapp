import logging

from django.contrib.auth import get_user_model
from django.db import models
from polymorphic.models import PolymorphicModel
from safedelete.models import SafeDeleteModel, SOFT_DELETE
from .enum import TaskStatusType, TaskType

User = get_user_model()
logger = logging.getLogger(__name__)


class Task(PolymorphicModel, SafeDeleteModel):
    """
    Append-only log published to /devices/:id/state FROM device
    Indicates current state of device

    See: desired state design pattern for details
    https://cloud.google.com/iot/docs/concepts/devices#changing_device_behavior_or_state_using_configuration_data
    """

    _safedelete_policy = SOFT_DELETE

    class Meta:
        ordering = ["-created_dt"]
        index_together = [["device", "created_dt"]]

    device = models.ForeignKey(
        "devices.Device", on_delete=models.CASCADE, db_index=True, related_name="tasks"
    )
    created_dt = models.DateTimeField(db_index=True, auto_now_add=True)

    @property
    def last_status(self):
        return self.status_set.first()


class MonitoringStartTask(Task):
    janus_auth = models.ForeignKey("devices.JanusCloudAuth", on_delete=models.CASCADE)
    janus_media_stream = models.ForeignKey(
        "devices.JanusCloudMediaStream", on_delete=models.CASCADE
    )

    @property
    def name(self):
        return TaskType.MONITOR_START


class MonitoringStopTask(Task):
    janus_media_stream = models.ForeignKey(
        "devices.JanusCloudMediaStream", on_delete=models.CASCADE
    )

    @property
    def name(self):
        return TaskType.MONITOR_STOP


class TaskStatus(SafeDeleteModel):
    class Meta:
        ordering = ["-created_dt"]
        index_together = [["task", "status"]]

    created_dt = models.DateTimeField(db_index=True, auto_now_add=True)

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="status_set")

    status = models.CharField(
        max_length=16,
        choices=TaskStatusType.choices,
        default=TaskStatusType.PENDING,
    )

    @property
    def css_class(self):
        return TaskStatusType.get_css_class(self.status)
