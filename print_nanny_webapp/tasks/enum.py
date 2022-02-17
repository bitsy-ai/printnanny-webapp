from django.db import models


class TaskStatusType(models.TextChoices):
    FAILED = "failed", "Task failed."  # TODO prompt to send crash report
    PENDING = "pending", "Waiting for device to acknowledge task."
    STARTED = "started", "Task is running."
    SUCCESS = "success", "Task succeeded."
    TIMEOUT = "timeout", "Task timed out. Please try again."

    __css__ = dict(
        FAILED="danger",
        PENDING="secondary",
        STARTED="primary",
        SUCCESS="success",
        TIMEOUT="danger",
    )

    @classmethod
    def get_css_class(cls, value):
        return cls.__css__.get(cls(value).name, "unknown")


class JanusTaskType(models.TextChoices):
    CLOUD_MONITOR_START = "cloud_monitor_start", "Start PrintNanny Monitoring (Cloud)"
    CLOUD_MONITOR_STOP = "cloud_monitor_stop", "Stop PrintNanny Monitoring (Cloud)"
    EDGE_MONITOR_START = (
        "edge_monitor_start",
        "Start PrintNanny Monitoring (Private/Edge)",
    )
    EDGE_MONITOR_STOP = "edge_monitor_stop", "Stop PrintNanny Monitoring (Private/Edge)"
