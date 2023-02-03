import logging
import requests

from django.conf import settings
from djstripe import webhooks

logger = logging.getLogger(__name__)


@webhooks.handler("checkout.session.completed")
def notify_checkout_session_completed(event, **_kwargs):
    # session_id = event.data.get("id")
    # if session_id is None:
    #     logger.error("Failed to read event.id from event=%s", event)
    #     return

    # session = models.Session(id=session_id)
    # dashboard_url = session.get_stripe_dashboard_url()

    body = {"content": f"Stripe checkout.session.completed - {event}"}
    requests.post(settings.DISCORD_NEW_SIGNUP_WEBHOOK, json=body, timeout=30)


@webhooks.handler("checkout.session.expired")
def notify_checkout_session_expired(event, **_kwargs):
    # session_id = event.data.get("id")
    # if session_id is None:
    #     logger.error("Failed to read event.id from event=%s", event)
    #     return

    # session = models.Session(id=session_id)
    # dashboard_url = session.get_stripe_dashboard_url()

    body = {"content": f"Stripe checkout.session.expired- {event}"}
    requests.post(settings.DISCORD_NEW_SIGNUP_WEBHOOK, json=body, timeout=30)
