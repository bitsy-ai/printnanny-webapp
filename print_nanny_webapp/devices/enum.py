from django.db import models


class CameraType(models.TextChoices):
    PICAM = "picam", "Raspberry Pi Camera Module"
    USB = (
        "usb",
        "USB Camera (coming soon)",
    )
    IP = "ip", "Generic RTP/RTSP IP Camera (coming soon)"


class DeviceReleaseChannel(models.TextChoices):
    STABLE = "stable", "Stable mainline release channel"
    NIGHTLY = "nightly", "Nightly developer release channel"


class PrinterSoftwareType(models.TextChoices):
    OCTOPRINT = "OctoPrint", "OctoPrint printer controller"
    # TODO re-enable as setup teaser + add 400 response if submitted
    # REPETIER = "Repetier", "Repetier printer controller"
    # MAINSAL = "Mainsail", "Mainsail printer controller"


class TaskStatusType(models.TextChoices):
    FAILED = "failed", "Task failed."  # TODO prompt to send crash report
    PENDING = "pending", "Waiting for device to acknowledge task."
    STARTED = "started", "Task is running."
    SUCCESS = "success", "Task succeeded."
    TIMEOUT = "timeout", "Task timed out. Please try again."

    __css__ = dict(
        FAILED="danger",
        PENDING="secondary",
        STARTED="warning",
        SUCCESS="success",
        TIMEOUT="timeout",
    )

    @classmethod
    def get_css_class(cls, value):
        return cls.__css__[cls(value).name]


class TaskType(models.TextChoices):
    ACTIVATE_LICENSE = "activate_license", "License Activation"
    SOFTWARE_UPDATE = (
        "software_update",
        "Software Updating",
    )
