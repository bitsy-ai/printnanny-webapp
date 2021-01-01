import asyncio
import os
import logging
from django.conf import settings
from django.apps import apps
from google.cloud import pubsub_v1

from print_nanny_webapp.client_events.models import OctoPrintEventTypeChoices, PrintJobEventTypeChoices
OctoPrintEvent = apps.get_model('remote_control', 'OctoPrintEvent')
PrintJobEvent = apps.get_model('remote_control', 'OctoPrintEvent')

logger = logging.getLogger(__name__)
subscriber = pubsub_v1.SubscriberClient()
subscription_name = settings.GCP_PUBSUB_OCTOPRINT_EVENTS_SUBSCRIPTION


def on_octoprint_event(message):

    logger.debug(f'Received event {message.get("event_type")}')
    message.ack()

future = subscriber.subscribe(subscription_name, on_octoprint_event)

if __name__ '__main__':
    asyncio.run(future)
