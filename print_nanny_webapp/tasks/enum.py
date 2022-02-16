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


class TaskType(models.TextChoices):
    MONITOR_START = "monitor_start", "Start Monitor"
    MONITOR_STOP = "monitor_stop", "Stop Monitor"

    SYSTEM_CHECK = "system_check", "System Check"
    SOFTWARE_UPDATE = (
        "software_update",
        "Software Updating",
    )
