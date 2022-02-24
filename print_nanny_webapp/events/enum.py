from django.db import models


class EventType(models.TextChoices):
    WebRTCEvent = "WebRTCEvent"
    TestEvent = "TestEvent"


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
