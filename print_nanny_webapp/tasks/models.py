import logging

from django.contrib.auth import get_user_model
from django.db import models
from polymorphic.models import PolymorphicModel
from safedelete.models import SafeDeleteModel, SOFT_DELETE
from .enum import TaskStatusType, JanusTaskType

User = get_user_model()
logger = logging.getLogger(__name__)


class Task(PolymorphicModel, SafeDeleteModel):
    """
    Append-only log published to /devices/:id/state FROM device
    Indicates current state of device

    See: desired state design pattern for details
    """

    _safedelete_policy = SOFT_DELETE
    active = models.BooleanField(default=True)

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


class JanusTask(Task):
    task_type = models.CharField(max_length=32, choices=JanusTaskType.choices)
    stream = models.ForeignKey("devices.JanusStream", on_delete=models.CASCADE)


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
