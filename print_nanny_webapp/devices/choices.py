from django.db import models


class DeviceReleaseChannel(models.TextChoices):
    STABLE = "stable", "Stable mainline release channel"
    NIGHTLY = "nightly", "Nightly developer release channel"


class PrinterSoftwareType(models.TextChoices):
    OCTOPRINT = "OctoPrint", "OctoPrint printer controller"
    # TODO re-enable as setup teaser + add 400 response if submitted
    # REPETIER = "Repetier", "Repetier printer controller"
    # MAINSAL = "Mainsail", "Mainsail printer controller"


class DeviceStatus(models.TextChoices):
    INITIAL = "initial", "Waiting for initial Raspberry Pi boot"
    UPDATE_RUNNING = (
        "update_running",
        "Software update in-progress. Please do not power down or reboot.",
    )
    UPDATE_FAILED = "update_failed", "Software update failed"  # TODO send crash report
    UPDATE_SUCCESS = "update_success", "Software is up-to-date"


class DeviceCommand(models.TextChoices):
    SOFTWARE_UPDATE = (
        "printnanny update",
        "Run software updates. Please do not reboot or power down until update is finished.",
    )
