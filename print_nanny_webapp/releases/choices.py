from django.db import models


class ReleaseChannel(models.TextChoices):
    STABLE = "stable", "Stable mainline release channel"
    NIGHTLY = "nightly", "Nightly developer release channel"


class ReleaseVariant(models.TextChoices):
    BASE_DESKTOP = "base_desktop", "Customizable Desktop Edition"
    BASE_SLIM = "base_slim", "Slim Headless Edition"
    OCTOPRINT_DESKTOP = "octoprint_desktop", "OctoPrint Desktop Edition"
    OCTOPRINT_SLIM = "octoprint_slim", "OctoPrint Slim Edition"
    # @TODO repetier and mainsail
