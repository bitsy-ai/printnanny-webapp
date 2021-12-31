from django.db import models


class ReleaseChannel(models.TextChoices):
    STABLE = "stable", "Stable mainline release channel"
    NIGHTLY = "nightly", "Nightly developer release channel"


class ReleaseVariant(models.TextChoices):
    DESKTOP = "desktop", "Customizable Desktop Edition"
    OCTOPRINT = "cctoPrint", "OctoPrint Edition"
    MAINSAIL = "mainsail", "Mainsail Edition"
    REPETIER = "repetier", "Repetier Edition"
