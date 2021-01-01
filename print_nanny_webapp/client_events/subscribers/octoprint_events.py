import asyncio
import json
import os
import logging

from google.cloud import pubsub_v1
from google.protobuf.json_format import MessageToDict
import sys

# import sys
# sys.path.insert(0,'/app')

# If DJANGO_SETTINGS_MODULE is unset, default to the local settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
# from django.conf import settings
# settings.configure()

from django.conf import settings
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
from django.apps import apps
from print_nanny_webapp.client_events.models import (
    OctoPrintEventCodes,
    PrintJobEventCodes,
)

OctoPrintEvent = apps.get_model("client_events", "OctoPrintEvent")
PrintJobEvent = apps.get_model("client_events", "PrintJobEvent")

logger = logging.getLogger(__name__)
subscriber = pubsub_v1.SubscriberClient()
subscription_name = settings.GCP_PUBSUB_OCTOPRINT_EVENTS_SUBSCRIPTION



def on_octoprint_event(message):
    data = message.data.decode('utf-8')
    data = json.loads(data)

    event_type = data["event_type"]
    logger.debug(f'Received {event_type} with data {data}')
    if data.get("device_id") is None:
        logger.warning(f'Received {event_type} without device_id {data}')
        message.ack()
        return
    if data.get("user_id") is None:
        logger.warning(f'Received {event_type} without user_id {data}')
        message.ack()
        return
    if event_type in OctoPrintEventCodes:
        OctoPrintEvent.objects.create(
            created_dt=data["created_dt"],
            device_id=data["device_id"],
            event_data=data,
            event_type=event_type,
            octoprint_version=data["octoprint_version"],
            plugin_version=data["plugin_version"],
            user_id=data["user_id"],
        )
    elif event_type in PrintJobEvent:
        PrintJobEvent.objects.create(
            created_dt=data["created_dt"],
            current_z=data["printer_data"]["currentZ"],
            device_id=data["device_id"],
            event_data=data,
            event_type=event_type,
            job_data_file=data["printer_data"]["job"]["file"],
            octoprint_version=data["octoprint_version"],
            plugin_version=data["plugin_version"],
            progress=data["printer_data"]["progress"],
            state=data["printer_data"]["state"],
            user_id=data["user_id"],
        )
    else:
        logger.error(f"Unrecognized event_type={event_type} with data {data}")
    message.ack()


future = subscriber.subscribe(subscription_name, on_octoprint_event)

if __name__ == "__main__":
    future.result()
