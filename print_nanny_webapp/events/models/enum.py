from django.db import models


class AlertEventType(models.TextChoices):
    PRINT_QUALITY = "PrintQuality", "Quality control alerts"
    PRINT_STARTED = "PrintStarted", "Triggered on print job start"
    PRINT_DONE = "PrintDone", "Triggered when print job is finished"
    PRINT_PROGRESS = (
        "PrintProgress",
        "Triggered when print job progress reaches %percent",
    )
    PRINT_PAUSED = "PrintPaused", "Triggered when print job is paused"
    PRINT_CANCELLED = "PrintCancelled", "Triggered when print job is cancelled"


class PiCamCommandType(models.TextChoices):
    CamStart = ("CamStart", "Start gstreamer pipelines")
    CamStop = ("CamStop", "Stop gstreamer pipelines")


class PiCamStatusType(models.TextChoices):
    CamStarted = ("CamStarted", "gstreamer pipeline started")
    CamStartSuccess = ("CamStartSuccess", "gstreamer pipeline started successfully")
    CamError = ("CamError", "gstreamer pipeline error")
    CamStopped = ("CamStopped", "gstreamer pipeline stopped")


class PiSoftwareUpdateCommandType(models.TextChoices):
    SwupdateUpdate = ("Swupdate", "Update PrintNanny OS to target version")
    SwupdateRollback = ("SwupdateRollback", "Rollback PrintNanny OS to target version")


class PiSoftwareUpdateStatusType(models.TextChoices):
    SwupdateStarted = ("SwupdateStarted", "Started PrintNanny OS update")
    SwupdateSuccess = ("SwupdateSuccess", "PrintNanny OS update succeeded")
    SwupdateError = ("SwupdateError", "Error updating Raspberry Pi")


class PiBootCommandType(models.TextChoices):
    Reboot = ("Reboot", "Reboot Raspberry Pi")
    Shutdown = ("Shutdown", "Shutdown Raspberry Pi")
    SyncSettings = ("SyncSettings", "Sync Raspberry Pi settings")
    SystemctlShow = ("SystemctlShow", "Get output from `systemctl show`")


class PiBootStatusType(models.TextChoices):
    SystemctlShow = ("SystemctlShow", "Get output from `systemctl show`")
    RebootStarted = ("RebootStarted", "Raspberry Pi will reboot soon")
    RebootError = ("RebootError", "Unexpected error during reboot")
    ShutdownStarted = ("ShutdownStarted", "Raspberry Pi will shutdown soon")
    ShutdownError = ("ShutdownError", "Unexpected error during shutdown")
    BootStarted = (
        "BootStarted",
        "Emitted during boot process, typically after systemd network-online.target",
    )
    BootSuccess = (
        "BootSuccess",
        "Boot reached default.target with no errors or degraded services",
    )
    BootDegraded = (
        "BootDegraded",
        "At least one systemd service reports degraded state",
    )
    SyncSettingsStarted = (
        "SyncSettingsStarted",
        "Raspberry Pi started synchronizing settings",
    )
    SyncSettingsSuccess = (
        "SyncSettingsSuccess",
        "Success synchronizing Raspberry Pi settings",
    )
    SyncSettingsError = (
        "SyncSettingsError",
        "Error synchronizing Raspberry Pi settings",
    )


class PiEventSubjectPattern(models.TextChoices):
    PiBootStatus = "pi.{pi_id}.status.boot"
    PiBootCommand = "pi.{pi_id}.command.boot"
    PiCamStatus = "pi.{pi_id}.status.cam"
    PiCamCommand = "pi.{pi_id}.command.cam"
    PiSoftwareUpdateStatus = "pi.{pi_id}.status.swupdate"
    PiSoftwareUpdateCommand = "pi.{pi_id}.command.swupdate"


class EventModel(models.TextChoices):
    """
    Reference enum for Polymorphic Event models
    """

    WebRTCEvent = "WebRTCEvent"
    WebRTCCommand = "WebRTCCommand"
    TestEvent = "TestEvent"


class TestEventModel(models.TextChoices):
    """
    Enum with 1 possible value is the easiest way to specify a "constant" value in an OpenAPI schema
    """

    TestEvent = "TestEvent"


class WebRTCEventModel(models.TextChoices):
    """
    Enum with 1 possible value is the easiest way to specify a "constant" value in an OpenAPI schema
    """

    WebRTCEvent = "WebRTCEvent"


class WebRTCCommandModel(models.TextChoices):
    """
    Enum with 1 possible value is the easiest way to specify a "constant" value in an OpenAPI schema
    """

    WebRTCCommand = "WebRTCCommand"


class EventSource(models.TextChoices):
    OCTOPRINT = ("octoprint", "Events originating from OctoPrint")
    PRINTNANNY_OS = (
        "printnanny_os",
        "Event originating from PrintNanny OS",
    )
    PRINTNANNY_CLOUD = (
        "printnanny_cloud",
        "Events originating from PrintNanny Cloud services",
    )
    MOONRAKER = (
        "mainsail",
        "Events originating from moonraker",
    )
