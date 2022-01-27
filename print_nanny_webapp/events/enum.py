from django.db import models


class EventSource(models.TextChoices):
    OCTOPRINT = ("octoprint", "Events originating from OctoPrint")
    PRINT_NANNY = (
        "print_nanny",
        "Events originating from Print Nanny",
    )
    MOONRAKER = (
        "mainsail",
        "Events originating from moonraker",
    )


class PrintNannyEventStatus(models.TextChoices):
    SENT = "sent", "Sent"
    ACK = "ack", "Acknowledged"
    SUCCESS = "success", "Success"
    FAILED = "failed", "Failed"
    TIMEOUT = "timeout", "Timeout"


class PrintNannyEventType(models.TextChoices):
    MQTT_PING = "mqtt_ping", "MQTT Ping Event"
    MQTT_PONG = "mqtt_pong", "MQTT Pong Event"
