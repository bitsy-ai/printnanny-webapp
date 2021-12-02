from django.db import models


class DeviceReleaseChannel(models.TextChoices):
    STABLE = "stable", "Stable mainline release channel"
    NIGHTLY = "nightly", "Nightly developer release channel"


class PrinterSoftwareType(models.TextChoices):
    OCTOPRINT = "OctoPrint", "OctoPrint printer controller"
    # TODO re-enable as setup teaser + add 400 response if submitted
    # REPETIER = "Repetier", "Repetier printer controller"
    # MAINSAL = "Mainsail", "Mainsail printer controller"


class SystemTaskStatus(models.TextChoices):
    WAITING = "waiting", "Waiting for Pi to accept task"
    STARTED = "started", "Running"
    FAILED = "failed", "Failed"  # TODO prompt to send crash report
    SUCCESS = "success", "Success"

    __css__ = dict(
        WAITING="secondary",
        STARTED="warning",
        FAILED="danger",
        SUCCESS="success",
    )

    @classmethod
    def get_css_class(cls, value):
        return cls.__css__[cls(value).name]


class SystemTaskType(models.TextChoices):
    ACTIVATE_LICENSE = "activate_license", "License Activation"
    SOFTWARE_UPDATE = (
        "software_update",
        "Software Updating",
    )
