from django.db import models


class EventModel(models.TextChoices):
    """
    Reference enum for Polymorphic Event models
    """

    WebRTCEvent = "WebRTCEvent"
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


class OctoPrintEventModel(models.TextChoices):
    OctoPrintEvent = "OctoPrintEvent"


class OctoPrintEventName(models.TextChoices):
    """
    EVENT_NAME : (OctoPrintEventString, Human-readable description)
    """

    SERVER_STARTUP = "Startup", "Server Startup"  # server
    SERVER_SHUTDOWN = "Shutdown", "Server Shutdown"  # server
    PRINT_PROGRESS = "PrintProgress", "Print Progress"  # printer comms
    PRINTER_CONNECTING = "Connecting", "Printer Connecting"  # printer comms
    PRINTER_CONNECTED = "Connected", "Printer Connecting"  # printer comms
    PRINTER_DISCONNECTING = "Disconnecting", "Printer Disconnecting"  # printer comms
    PRINTER_DISCONNECTED = (
        "Disconnected",
        "Printer Disconnected",
    )  # printer comms
    PRINTER_CONNECT_ERROR = "Error", "Printer Connection Error"  # printer comms
    PRINT_JOB_STARTED = "PrintStarted", "Print Job Started"  # print job
    PRINT_JOB_FAILED = "PrintFailed", "Print Job Failed"  # print job
    PRINT_JOB_DONE = "PrintDone", "Print Job Done"  # print job
    PRINT_JOB_CANCELLING = "PrintCancelling", "Print Job Cancelling"  # print job
    PRINT_JOB_CANCELLED = "PrintCancelled", "Print Job Cancelled"  # print job
    PRINT_JOB_PAUSED = "PrintPaused", "Print Job Paused"  # print job
    PRINT_JOB_RESUMED = "PrintResumed", "Print Job Resumed"  # print job


class TestEventName(models.TextChoices):
    MQTT_PING = "mqtt_ping", "Ping"
    MQTT_PONG = "mqtt_pong", "Pong"


class WebRTCEventName(models.TextChoices):
    STREAM_START = (
        "stream_start",
        "Initialize WebRTC mountpoint via Janus Gateway streaming plugin",
    )
    STREAM_START_SUCCESS = (
        "stream_start_success",
        "Successfully created WebRTC Mountpoint, returns Janus streaming plugin info repsponse",
    )
    STREAM_START_ERROR = "stream_start_error", "Error creating WebRTC Mountpoint"

    STREAM_STOP = (
        "stream_stop",
        "Initialize teardown of WebRTC mountpoint via Janus Gateway streaming plugin",
    )
    STREAM_STOP_SUCCESS = (
        "stream_stop_success",
        "Successfully tore down WebRTC Mountpoint, returns Janus streaming plugin destroyed response",
    )
    STREAM_STOP_ERROR = (
        "stream_stop_error",
        "Error tearing down WebRTC Mountpoint, returns Janus streaming plugin error response",
    )


class EventSource(models.TextChoices):
    OCTOPRINT = ("octoprint", "Events originating from OctoPrint")
    PRINTNANNY_OS = (
        "printnanny_os",
        "Events originating from PrintNanny OS",
    )
    PRINTNANNY_WEB = (
        "printnanny_webapp",
        "Events originating from PrintNanny Webapp",
    )
    MOONRAKER = (
        "mainsail",
        "Events originating from moonraker",
    )
