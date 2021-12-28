from django.db import models


class ReleaseChannel(models.TextChoices):
    STABLE = "stable", "Stable mainline release channel"
    NIGHTLY = "nightly", "Nightly developer release channel"


class ReleaseVariant(models.TextChoices):
    DESKTOP = "Desktop", "Customizable Desktop Edition"
    OCTOPRINT = "OctoPrint", "OctoPrint Edition"
    MAINSAIL = "Mainsail", "Mainsail Edition"
    REPETIER = "Rctoprint", "Repetier Edition"
