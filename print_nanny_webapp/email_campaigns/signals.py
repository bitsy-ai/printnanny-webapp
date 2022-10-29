import logging
from anymail.signals import post_send, tracking
from anymail.message import UNSET
from django.dispatch import receiver

from print_nanny_webapp.email_campaigns.models import EmailMessage, EmailTrackingEvent

logger = logging.getLogger(__name__)

# log sent emails
@receiver(post_send)
def log_sent_message(sender, message, status, esp_name, **_kwargs):

    merge_global_data = getattr(message, "merge_global_data", None)

    if merge_global_data is not None and merge_global_data != UNSET:
        campaign_id = message.merge_global_data.get("campaign_id")
        if campaign_id is None:
            raise ValueError(
                "metadata->campaign_id is required to log sent EmailMessage"
            )
        for email, recipient_status in status.recipients.items():
            metadata = message.merge_metadata[email]
            user_id = metadata.get("user_id")
            obj = EmailMessage.objects.create(
                message_id=recipient_status.message_id,  # might be None if send failed
                send_status=recipient_status.status,
                campaign_id=campaign_id,
                user_id=user_id,
                email=email,
            )
            logger.info(
                "Logged EmailMessage id=%s message_id=%s", obj.id, obj.message_id
            )

    else:
        logger.warning(
            "log_sent_message merge_global_data is UNSET, failed to log EmailMessage"
        )


# record webhook tracking events
@receiver(tracking)
def log_tracking_event(sender, event, esp_name, **_kwargs):
    message_id = event.message_id
    if message_id is None:
        logger.error("Received Mailgun tracking event without message_id: %s", event)
        raise ValueError("message_id is required")

    try:
        email_message = EmailMessage.objects.get(message_id=message_id)
        obj = EmailTrackingEvent.objects.create(
            email_message=email_message,
            campaign=email_message.campaign,
            user=email_message.user,
            event_type=event.event_type,
            message_id=message_id,
            ts=event.timestamp,
            recipient=event.recipient,
            metadata=event.metadata,
            tags=event.tags,
            reject_reason=event.reject_reason,
            description=event.description,
            mta_response=event.mta_response,
            user_agent=event.user_agent,
            click_url=event.click_url,
            esp_event=event.esp_event,
        )
    except EmailMessage.DoesNotExist:
        logger.warning(
            "Received mailgun webhook with message_id=%s, but no EmailMessage log exists with message_id",
            message_id,
        )
        obj = EmailTrackingEvent.objects.create(
            email_message=None,
            campaign=None,
            user=None,
            event_type=event.event_type,
            message_id=message_id,
            ts=event.timestamp,
            recipient=event.recipient,
            metadata=event.metadata,
            tags=event.tags,
            reject_reason=event.reject_reason,
            description=event.description,
            mta_response=event.mta_response,
            user_agent=event.user_agent,
            click_url=event.click_url,
            esp_event=event.esp_event,
        )
    logger.info(
        "Created EmailTrackingEvent id=%s event_type=%s",
        obj.id,
        obj.event_type,
    )
