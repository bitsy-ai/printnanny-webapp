from django.db import models


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


class TaskStatusType(models.TextChoices):
    FAILED = "failed", "Task failed."  # TODO prompt to send crash report
    PENDING = "pending", "Waiting for device to acknowledge task."
    STARTED = "started", "Task is running."
    SUCCESS = "success", "Task succeeded."
    TIMEOUT = "timeout", "Task timed out. Please try again."

    __css__ = dict(
        FAILED="danger",
        PENDING="secondary",
        STARTED="primary",
        SUCCESS="success",
        TIMEOUT="danger",
    )

    @classmethod
    def get_css_class(cls, value):
        return cls.__css__.get(cls(value).name, "unknown")


class TaskType(models.TextChoices):
    MONITOR_START = "monitor_start", "Start Monitor"
    MONITOR_STOP = "monitor_stop", "Stop Monitor"

    SYSTEM_CHECK = "system_check", "System Check"
    SOFTWARE_UPDATE = (
        "software_update",
        "Software Updating",
    )


class OnboardingTaskType(models.TextChoices):
    LINK = "link", "Link device to your account"
    TEST_VIDEO = "test_video", "Test live video stream"
    TEST_MQTT = "test_mqtt", "Send a ping/pong over MQTT"
    RESTORE_OCTOPRINT = "restore_octoprint", "Restore OctoPrint from backup"
    TEST_OCTOPRINT = "test_octoprint", "Log into OctoPrint"
