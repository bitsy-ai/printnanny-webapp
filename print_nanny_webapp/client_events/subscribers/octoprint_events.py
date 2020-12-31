import asyncio
import os
import logging
from django.conf import settings
from google.cloud import pubsub_v1

logger = logging.getLogger(__name__)
subscriber = pubsub_v1.SubscriberClient()
topic_name = settings.GCP_PUBSUB_OCTOPRINT_EVENTS_TOPIC
subscription_name = settings.GCP_PUBSUB_OCTOPRINT_EVENTS_SUBSCRIPTION

subscriber.create_subscription(
    name=subscription_name, topic=topic_name)

def on_octoprint_event(message):

    logger.debug(f'Received event {message.get("event_type")}')
    message.ack()

future = subscriber.subscribe(subscription_name, on_octoprint_event)

if __name__ '__main__':
    asyncio.run(future)
