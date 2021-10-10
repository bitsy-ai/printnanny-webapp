from django.db import models


class ApplianceReleaseChannel(models.TextChoices):
    MAIN = "main", "Stable mainline release channel"
    DEVEL = "devel", "Unstable developer release channel"


class PrinterSoftwareType(models.TextChoices):
    OCTOPRINT = "OctoPrint", "OctoPrint printer controller"
    # TODO re-enable as setup teaser + add 400 response if submitted
    # REPETIER = "Repetier", "Repetier printer controller"
    # MAINSAL = "Mainsail", "Mainsail printer controller"
