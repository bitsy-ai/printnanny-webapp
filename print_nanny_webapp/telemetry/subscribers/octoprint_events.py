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

OctoPrintEvent = apps.get_model("telemetry", "OctoPrintEvent")
OctoPrintPluginEvent = apps.get_model("telemetry", "OctoPrintEvent")
PrintStatusEvent = apps.get_model("telemetry", "PrintStatusEvent")
AlertSettings = apps.get_model("alerts", "AlertSettings")
PrintSession = apps.get_model("remote_control", "PrintSession")

logger = logging.getLogger(__name__)
subscriber = pubsub_v1.SubscriberClient()
subscription_name = settings.GCP_PUBSUB_OCTOPRINT_EVENTS_SUBSCRIPTION


def handle_print_progress(octoprint_event):
    alert_settings, created = AlertSettings.objects.get_or_create(
        user=octoprint_event.user
    )
    progress = octoprint_event.get("print_progress")

    # update print session progress
    print_session = octoprint_event.get("metadata", {}).get("print_session")
    if print_session:
        print_session = PrintSession.objects.get(session=print_session).update(
            progress = progress,
            filepos = octoprint_event.get("filepos"),
            time_elapsed = octoprint_event.get("time_elapsed"),
            time_remaining = octoprint_event.get("time_remaining")
        )

    if progress % self.on_progress_percent == 0 and progress != 100: # PrintDone / VideoDone events capture the case where a print is 100% complete
        # @TODO write octoprint_event serializer
        print_session = octoprint_event.get('metadata', {}).get('print_session')
        octoprint_device = octoprint_event.get('metadata', {}).get('octoprint_device_id')
        for alert_method in self.alert_methods:
            alert_message = AlertMessage(
                alert_method=alert_method,
                event_type=AlertEventTypes.PRINT_PROGRESS,
                extra_data=octoprint_event,
                print_session=print_session,
                user=self.user,
                octoprint_device=octoprint_device_id
            )
            task = PrintStatusAlertTask(self)
        


def handle_print_status(octoprint_event):
    """
        Exclude PrintDone if monitoring is active (video render will duplicate alert)
    """
    pass



HANDLER_FNS = {OctoPrintEvent.EventType.PRINT_PROGRESS: handle_print_progress}

HANDLER_FNS.update(
    {value: handle_print_status for label, value in PrintStatusEvent.EventType.choices}
)


def on_octoprint_event(message):
    data = message.data.decode("utf-8")
    data = json.loads(data)

    event_type = data["event_type"]

    logger.debug(f"Received {event_type} with data {data}")
    if data.get("octoprint_device_id") is None:
        logger.warning(f"Received {event_type} without octoprint_device_id {data}")
        message.ack()
        return
    if data.get("user_id") is None:
        logger.warning(f"Received {event_type} without user_id {data}")
        message.ack()
        return
    if event_type in OctoPrintEvent.EventType:
        try:
            event = OctoPrintEvent.objects.create(
                created_dt=data["created_dt"],
                octoprint_device_id=data["octoprint_device_id"],
                event_data=data,
                event_type=event_type,
                octoprint_version=data["octoprint_version"],
                plugin_version=data["plugin_version"],
                user_id=data["user_id"],
            )
            handler_fn = HANDLER_FNS.get(event_type)
            if handler_fn is not None:
                handler_fn(event)
        except Exception as e:
            logger.error({"error": e, "data": data}, exc_info=True)
    elif event_type in PrintStatusEvent.EventType:
        try:
            PrintStatusEvent.objects.create(
                created_dt=data["created_dt"],
                current_z=data["printer_data"]["currentZ"],
                octoprint_device_id=data["octoprint_device_id"],
                event_data=data,
                event_type=event_type,
                job_data_file=data["printer_data"]["job"]["file"],
                octoprint_version=data["octoprint_version"],
                plugin_version=data["plugin_version"],
                progress=data["printer_data"]["progress"],
                state=data["printer_data"]["state"],
                user_id=data["user_id"],
            )
            handler_fn = HANDLER_FNS.get(event_type)
            if handler_fn is not None:
                handler_fn(event)
        except Exception as e:
            logger.error({"error": e, "data": data})

    elif (
        OctoPrintPluginEvent.strip_plugin_identifier(event_type)
        in OctoPrintPluginEvent.EventType
    ):
        try:
            OctoPrintPluginEvent.objects.create(
                created_dt=data["created_dt"],
                current_z=data["printer_data"]["currentZ"],
                octoprint_device_id=data["octoprint_device_id"],
                event_data=data,
                event_type=event_type,
                octoprint_version=data["octoprint_version"],
                plugin_version=data["plugin_version"],
                user_id=data["user_id"],
            )
        except Exception as e:
            logger.error({"error": e, "data": data})
    else:
        logger.error(f"Unrecognized event_type={event_type} with data {data}")
    message.ack()


future = subscriber.subscribe(subscription_name, on_octoprint_event)

if __name__ == "__main__":
    future.result()
