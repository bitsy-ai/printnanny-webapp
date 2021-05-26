import json
import os
import logging

from google.cloud import pubsub_v1

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
import google.api_core.exceptions

from django.contrib.auth import get_user_model

User = get_user_model()
OctoPrintEvent = apps.get_model("telemetry", "OctoPrintEvent")
OctoPrintPluginEvent = apps.get_model("telemetry", "OctoPrintPluginEvent")
PrintStatusEvent = apps.get_model("telemetry", "PrintStatusEvent")
AlertSettings = apps.get_model("alerts", "AlertSettings")
PrintSession = apps.get_model("remote_control", "PrintSession")
RemoteControlCommand = apps.get_model("remote_control", "RemoteControlCommand")
OctoPrintDevice = apps.get_model("remote_control", "OctoPrintDevice")
AlertMessage = apps.get_model("alerts", "AlertMessage")

logger = logging.getLogger(__name__)
subscriber = pubsub_v1.SubscriberClient()
subscription_name = settings.GCP_PUBSUB_OCTOPRINT_EVENTS_SUBSCRIPTION


def handle_print_progress(octoprint_event):
    from print_nanny_webapp.alerts.tasks.alerts import AlertTask

    user = User.objects.get(id=octoprint_event["metadata"]["user_id"])
    alert_settings, created = AlertSettings.objects.get_or_create(user=user)
    progress = octoprint_event.get("event_data", {}).get("print_progress")
    # update print session progress
    print_session = octoprint_event.get("metadata", {}).get("print_session")
    if print_session:
        PrintSession.objects.filter(session=print_session).update(
            print_progress=progress,
            # TODO
            # enrich print progress event with the following fields
            # filepos=octoprint_event.get("filepos"),
            # time_elapsed=octoprint_event.get("time_elapsed"),
            # time_remaining=octoprint_event.get("time_remaining"),
        )

    if (
        progress % alert_settings.print_progress_percent == 0 and progress != 100
    ):  # PrintDone / VideoDone events capture the case where a print is 100% complete
        # @TODO write octoprint_event serializer
        octoprint_device = octoprint_event.get("metadata", {}).get(
            "octoprint_device_id"
        )
        for alert_method in alert_settings.alert_methods:
            alert_message = AlertMessage.objects.create(
                alert_method=alert_method,
                event_type=AlertMessage.AlertMessageType.PRINT_PROGRESS,
                user=user,
                print_session_session=print_session,
                octoprint_device_id=octoprint_device,
            )
            task = AlertTask(alert_message)
            task.trigger_alert()


def handle_print_status(octoprint_event):
    """
    Exclude PrintDone if monitoring is active (video render will duplicate alert)
    """
    pass


def handle_ping(octoprint_event):
    device_id = octoprint_event["metadata"]["octoprint_device_id"]
    user_id = octoprint_event["metadata"]["user_id"]
    device = OctoPrintDevice.objects.get(id=device_id)
    user = User.objects.get(id=user_id)
    try:

        RemoteControlCommand.objects.create(
            user=user,
            device=device,
            command=RemoteControlCommand.Command.PONG,
        )
    except google.api_core.exceptions.FailedPrecondition as e:
        logger.error(
            f"Ping response for octoprint_device={octoprint_device} failed with error={e}"
        )


HANDLER_FNS = {OctoPrintEvent.EventType.PRINT_PROGRESS: handle_print_progress}

HANDLER_FNS.update(
    {value: handle_print_status for label, value in PrintStatusEvent.EventType.choices}
)

HANDLER_FNS.update({OctoPrintPluginEvent.EventType.CONNECT_TEST_MQTT_PING: handle_ping})

def event_is_tracked(event_type):
    return (
        event_type in OctoPrintEvent.EventType or
        event_type in PrintStatusEvent.EventType or
        event_type in OctoPrintPluginEvent.EventType or
        OctoPrintPluginEvent.strip_octoprint_prefix(event_type)
        in OctoPrintPluginEvent.EventType
    )

def on_octoprint_event(message):
    try:
        data = message.data.decode("utf-8")
    except UnicodeDecodeError as e:
        logger.error(e)
        logger.warning(f"Ignoring msg with content={message.data}")
        message.ack()
        return
    data = json.loads(data)

    event_type = data["event_type"]

    logger.info(f"Received {event_type} with data {data}")
    if not event_is_tracked(event_type):
        logger.error(f"Tracking event is not registered, ignoring event_type={event_type}")
        return message.ack()

    # TODO enforce a schema on this topic :facepalm:
    octoprint_device_id = data.get("octoprint_device_id") or data.get(
        "metadata", {}
    ).get("octoprint_device_id")
    user_id = data.get("user_id") or data.get("metadata", {}).get("user_id")

    if octoprint_device_id is None:
        logger.warning(f"Received {event_type} without octoprint_device_id {data}")
        message.ack()
        return
    if user_id is None:
        logger.warning(f"Received {event_type} without user_id {data}")
        message.ack()
        return
    if event_type in OctoPrintEvent.EventType:
        try:
            event = OctoPrintEvent.objects.create(
                created_dt=data["metadata"]["ts"],
                octoprint_device_id=octoprint_device_id,
                event_data=data,
                event_type=event_type,
                octoprint_version=data["metadata"]["octoprint_version"],
                plugin_version=data["metadata"]["plugin_version"],
                user_id=user_id,
            )
            handler_fn = HANDLER_FNS.get(event_type)
            if handler_fn is not None:
                handler_fn(data)
        except Exception as e:
            logger.error({"error": e, "data": data}, exc_info=True)
    if event_type in PrintStatusEvent.EventType:
        try:
            PrintStatusEvent.objects.create(
                created_dt=data["created_dt"],
                current_z=data["printer_data"]["currentZ"],
                octoprint_device_id=octoprint_device_id,
                event_data=data,
                event_type=event_type,
                job_data_file=data["printer_data"]["job"]["file"],
                octoprint_version=data["metadata"]["octoprint_version"],
                plugin_version=data["metadata"]["plugin_version"],
                progress=data["printer_data"]["progress"],
                state=data["printer_data"]["state"],
                user_id=user_id,
            )
            handler_fn = HANDLER_FNS.get(event_type)
            if handler_fn is not None:
                handler_fn(event)
        except Exception as e:
            logger.error({"error": e, "data": data})

    if (
        OctoPrintPluginEvent.strip_octoprint_prefix(event_type)
        in OctoPrintPluginEvent.EventType
    ):
        try:
            obj = OctoPrintPluginEvent.objects.create(
                created_dt=data["metadata"]["ts"],
                octoprint_device_id=octoprint_device_id,
                event_data=data,
                event_type=event_type,
                octoprint_version=data["metadata"]["octoprint_version"],
                plugin_version=data["metadata"]["plugin_version"],
                user_id=user_id,
                metadata=data["metadata"],
                octoprint_job=data["octoprint_job"],
            )

            handler_fn = HANDLER_FNS.get(
                OctoPrintPluginEvent.strip_octoprint_prefix(event_type)
            )
            if handler_fn is not None:
                handler_fn(data)
        except Exception as e:
            logger.error({"error": e, "data": data})
    message.ack()


future = subscriber.subscribe(subscription_name, on_octoprint_event)

if __name__ == "__main__":
    logger.info(f"Initializing subscription to {subscription_name}")
    future.result()
