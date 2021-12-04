from django.db import models


class DeviceReleaseChannel(models.TextChoices):
    STABLE = "stable", "Stable mainline release channel"
    NIGHTLY = "nightly", "Nightly developer release channel"


class PrinterSoftwareType(models.TextChoices):
    OCTOPRINT = "OctoPrint", "OctoPrint printer controller"
    # TODO re-enable as setup teaser + add 400 response if submitted
    # REPETIER = "Repetier", "Repetier printer controller"
    # MAINSAL = "Mainsail", "Mainsail printer controller"


class TaskStatusType(models.TextChoices):
    FAILED = "failed", "Failed"  # TODO prompt to send crash report
    REQUESTED = "requested", "Requested"
    STARTED = "started", "Running"
    SUCCESS = "success", "Success"
    TIMEOUT = "timeout", "Timeout"

    __css__ = dict(
        FAILED="danger",
        REQUESTED="secondary",
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
