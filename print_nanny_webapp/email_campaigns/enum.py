from django.db import models

# based on anymail.signals.EventType and anymail.signals.RejectReason, which are not exported in Django choices format


class EventType(models.TextChoices):
    """Constants for normalized Anymail event types"""

    # Delivery (and non-delivery) event types:
    # (these match message.ANYMAIL_STATUSES where appropriate)
    QUEUED = (
        "queued",
        "the ESP has accepted the message and will try to send it (possibly later)",
    )
    SENT = (
        "sent",
        "the ESP has sent the message (though it may or may not get delivered)",
    )
    REJECTED = (
        "rejected",
        "the ESP refused to send the messsage (e.g., suppression list, policy, invalid email)",
    )
    FAILED = (
        "failed",
        "the ESP was unable to send the message (e.g., template rendering error)",
    )

    BOUNCED = "bounced", "rejected or blocked by receiving MTA"
    DEFERRED = (
        "deferred",
        "delayed by receiving MTA; should be followed by a later BOUNCED or DELIVERED",
    )
    DELIVERED = "delivered", "accepted by receiving MTA"
    AUTORESPONDED = "autoresponded", "a bot replied"

    # Tracking event types:
    OPENED = "opened", "open tracking"
    CLICKED = "clicked", "click tracking"
    COMPLAINED = (
        "complained",
        "recipient reported as spam (e.g., through feedback loop)",
    )
    UNSUBSCRIBED = "unsubscribed", "recipient attempted to unsubscribe"
    SUBSCRIBED = "subscribed", "signed up for mailing list through ESP-hosted form"

    # Inbound event types:
    INBOUND = "inbound", "received message"
    INBOUND_FAILED = "inbound_failed", "inbound message delivery failed"

    # Other:
    UNKNOWN = "unknown", "Unknown"


class RejectReason(models.TextChoices):
    """Constants for normalized Anymail reject/drop reasons"""

    INVALID = "invalid", "bad address format"
    BOUNCED = "bounced", "(previous) bounce from recipient"
    TIMED_OUT = "timed_out", "(previous) repeated failed delivery attempts"
    BLOCKED = "blocked", "ESP policy suppression"
    SPAM = "spam", "(previous) spam complaint from recipient"
    UNSUBSCRIBED = "unsubscribed", "(previous) unsubscribe request from recipient"
    OTHER = "other", "Other"
