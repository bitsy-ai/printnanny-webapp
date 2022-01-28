from django.db import models


class EventModel(models.TextChoices):
    TestEvent = "TestEvent"


class EventSource(models.TextChoices):
    OCTOPRINT = ("octoprint", "Events originating from OctoPrint")
    PRINT_NANNY = (
        "printnanny",
        "Events originating from Print Nanny",
    )
    MOONRAKER = (
        "mainsail",
        "Events originating from moonraker",
    )


class EventStatus(models.TextChoices):
    SENT = "sent", "Sent"
    ACK = "ack", "Acknowledged"
    SUCCESS = "success", "Success"
    FAILED = "failed", "Failed"
    TIMEOUT = "timeout", "Timeout"


class TestEventType(models.TextChoices):
    MQTT_PING = "mqtt_ping", "MQTT Ping Event"
    MQTT_PONG = "mqtt_pong", "MQTT Pong Event"
