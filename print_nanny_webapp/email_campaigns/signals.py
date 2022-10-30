import logging
from typing import Optional
from anymail.signals import post_send, tracking
from anymail.message import UNSET
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.conf import settings
import posthog

from print_nanny_webapp.email_campaigns.models import EmailMessage, EmailTrackingEvent

logger = logging.getLogger(__name__)

UserModel = get_user_model()

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


def get_email_message_log(event) -> Optional[EmailMessage]:
    """
    Try to find EmailMessage associated with anymail tracking event
    """
    email_messages = EmailMessage.objects.filter(
        message_id=event.message_id, email=event.recipient
    ).all()

    if email_messages.count() > 1:
        logger.error(
            "Found %s EmailMessage rows for message_id=%s recipient=%s - associating with first found",
            email_messages.count(),
            event.message_id,
            event.recipient,
        )
        email_message = email_messages.first()
    elif email_messages.count() == 1:
        email_message = email_messages.first()
    else:
        logger.warning(
            "Received mailgun webhook with message_id=%s, but no EmailMessage log exists with message_id",
            event.message_id,
        )
        email_message = None
    return email_message


# record webhook tracking events
@receiver(tracking)
def log_tracking_event(sender, event, esp_name, **_kwargs):
    try:
        message_id = event.message_id

        # do not log admin error emails
        recipient = event.recipient

        admin_emails = [email for name, email in settings.ADMINS]

        if (
            recipient in admin_emails or recipient == "leigh+alerts@printnanny.ail"
        ):  # TODO remove hard-coded value
            logger.warning(
                "Ignoring Mailgun tracking event for admin email %s", recipient
            )
            return
        if message_id is None:
            logger.warning(
                "Received Mailgun tracking event without message_id: %s", event
            )
            return

        email_message = get_email_message_log(event)

        if email_message is not None:
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
                # mta_response=event.mta_response,
                mta_response=None,
                user_agent=event.user_agent,
                click_url=event.click_url,
                esp_event=event.esp_event,
            )
        else:
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
                mta_response=None,
                user_agent=event.user_agent,
                click_url=event.click_url,
                esp_event=event.esp_event,
            )
        logger.info(
            "Created EmailTrackingEvent id=%s event_type=%s",
            obj.id,
            obj.event_type,
        )

    # catch-all for exceptions, since any exceptions here would send us into a loop
    except Exception as e:
        logger.error("Error handling mailgun tracking webhook: %s", e)


# record webhook tracking events (posthog)
@receiver(tracking)
def log_posthog_tracking_event(sender, event, esp_name, **_kwargs):
    # do not log admin error emails
    try:
        recipient = event.recipient
        admin_emails = [email for name, email in settings.ADMINS]
        if (
            recipient in admin_emails or recipient == "leigh+alerts@printnanny.ail"
        ):  # TODO remove hard-coded value
            logger.warning(
                "Ignoring Mailgun tracking event for admin email %s", recipient
            )
            return
        if event.message_id is None:
            logger.warning(
                "Received Mailgun tracking event without message_id: %s", event
            )
            return

        event_name = f"email_{event.event_type}"

        capture_params = {
            "message_id": event.message_id,
        }

        email_message = get_email_message_log(event)

        # add campaign tracking info
        if email_message is not None:
            capture_params["campaign_id"] = email_message.campaign.id
            capture_params["campaign_template"] = email_message.campaign.template
            capture_params["campaign_subject"] = email_message.campaign.subject

        if event.click_url is not None:
            capture_params["click_url"] = event.click_url

        if event.user_agent is not None:
            capture_params["user_agent"] = event.user_agent

        if event.tags is not None:
            capture_params["tags"] = event.tags

        if event.reject_reason is not None:
            capture_params["reject_reason"] = event.reject_reason

        posthog.capture(event.recipient, event=event_name, properties=capture_params)

        user = UserModel.objects.filter(email=event.recipient).first()  # type: ignore[has-type]

        identity_params = {
            "email": event.recipient,
        }

        if user is not None:
            identity_params["user_id"] = user.id
            posthog.alias(event.recipient, f"user:{user.id}")
        posthog.identify(event.recipient, identity_params)
    # catch-all for exceptions, since any exceptions here would send us into an email send/tracking loop
    except Exception as e:
        logger.error("Error handling mailgun tracking webhook: %s", e)
