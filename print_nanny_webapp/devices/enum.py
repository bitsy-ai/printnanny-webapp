from django.db import models


class JanusConfigType(models.TextChoices):
    CLOUD = "cloud", "Cloud WebRTC Gateway"
    EDGE = "edge", "Edge WebRTC Gateway"


class PrintNannyEnv(models.TextChoices):
    SANDBOX = "sandbox", "Sandbox Environment"
    PROD = "prod", "Prod Environment"


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


class OsEdition(models.TextChoices):
    OCTOPRINT_DESKTOP = "octoprint_desktop", "PrintNanny OS OctoPrint Desktop"
    OCTOPRINT_SLIM = "octoprint_slim", "PrintNanny OS OctoPrint Slim/Headless"
    REPETIER_DESKTOP = "repetier_desktop", "PrintNanny OS Repetier Desktop"
    REPETIER_SLIM = "repetier_slim", "PrintNanny OS Repetier Slim/Headless"
    MAINSAIL_DESKTOP = "mainsail_desktop", "PrintNanny OS Mainsail Desktop"
    MAINSAIL_SLIM = "mainsail_slim", "PrintNanny OS Mainsail Slim/Headless"
