import os
from django.db import models


class FileLocator(models.TextChoices):
    INSTALL_PATH = "/opt/printnanny/"
    BOOT_PATH = "/boot"
    LICENSE_PATH = os.path.join(INSTALL_PATH, "license")

    DATA_PATH = os.path.join(INSTALL_PATH, "data")

    FACT_PATH = os.path.join(INSTALL_PATH, "facts.d")
    FACT_DEVICE_PATH = os.path.join(FACT_PATH, "device.fact")
    FACT_LICENSE_PATH = os.path.join(FACT_PATH, "license.fact")

    CA_CERTS = os.path.join(INSTALL_PATH, "ca-certificates")

    LICENSE_ZIP_FILENAME = "printnanny_license.zip"
    LICENSE_ZIP_PATH = os.path.join(BOOT_PATH, LICENSE_ZIP_FILENAME)

    KEY_PRIVATE_PKCS8_FILENAME = "ecdsa256_pkcs8.pem"
    KEY_PRIVATE_SEC1_FILENAME = "ecdsa256_sec1.pem"
    KEY_PUBLIC_FILENAME = "ecdsa_public.pem"

    KEY_PRIVATE_PKCS8_PATH = os.path.join(LICENSE_PATH, KEY_PRIVATE_PKCS8_FILENAME)
    KEY_PRIVATE_SEC1_PATH = os.path.join(LICENSE_PATH, KEY_PRIVATE_SEC1_FILENAME)
    KEY_PUBLIC_PATH = os.path.join(LICENSE_PATH, KEY_PUBLIC_FILENAME)

    CA_CERTS_FILENAME = "ca_certs.pem"
    CA_CERTS_PATH = os.path.join(CA_CERTS, CA_CERTS_FILENAME)


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
