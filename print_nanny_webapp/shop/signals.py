import logging
import requests

from django.conf import settings
from djstripe import webhooks

logger = logging.getLogger(__name__)


@webhooks.handler("checkout.session.completed")
def notify_checkout_session_completed(event, **kwargs):
    logger.info("checkout.session.completed event=%s kwargs=%s", event, kwargs)
    body = {"content": f"Stripe checkout.session.completed - {event}"}
    requests.post(settings.DISCORD_NEW_SIGNUP_WEBHOOK, json=body, timeout=30)


@webhooks.handler("checkout.session.expired")
def notify_checkout_session_expired(event, **kwargs):
    logger.info("checkout.session.expired event=%s kwargs=%s", event, kwargs)
    body = {"content": f"Stripe checkout.session.expired- {event}"}
    requests.post(settings.DISCORD_NEW_SIGNUP_WEBHOOK, json=body, timeout=30)
