from django.db import models


class DeviceReleaseChannel(models.TextChoices):
    STABLE = "stable", "Stable mainline release channel"
    NIGHTLY = "nightly", "Nightly developer release channel"


class PrinterSoftwareType(models.TextChoices):
    OCTOPRINT = "OctoPrint", "OctoPrint printer controller"
    # TODO re-enable as setup teaser + add 400 response if submitted
    # REPETIER = "Repetier", "Repetier printer controller"
    # MAINSAL = "Mainsail", "Mainsail printer controller"


class AnsibleStateChoices(models.TextChoices):
    RUNNING = "running" "Software update is running"
    SUCCESS = "success" "Software is up-to-date"
    FAILED = "failed" "Software update failed"
