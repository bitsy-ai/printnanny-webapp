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
from print_nanny_webapp.telemetry.types import (
    OctoprintEventType,
    PrintStatusEventType,
    RemoteCommandEventType,
    PrintNannyPluginEventType,
)

User = get_user_model()
OctoPrintEvent = apps.get_model("telemetry", "OctoPrintEvent")
PrintNannyPluginEvent = apps.get_model("telemetry", "PrintNannyPluginEvent")
PrintStatusEvent = apps.get_model("telemetry", "PrintStatusEvent")
RemoteCommandEvent = apps.get_model("telemetry", "RemoteCommandEvent")
TelemetryEvent = apps.get_model("telemetry", "TelemetryEvent")
AlertSettings = apps.get_model("alerts", "AlertSettings")
PrintSession = apps.get_model("remote_control", "PrintSession")
RemoteControlCommand = apps.get_model("remote_control", "RemoteControlCommand")
OctoPrintDevice = apps.get_model("remote_control", "OctoPrintDevice")
AlertMessage = apps.get_model("alerts", "AlertMessage")

logger = logging.getLogger(__name__)
subscriber = pubsub_v1.SubscriberClient()
subscription_name = settings.GCP_PUBSUB_OCTOPRINT_EVENTS_SUBSCRIPTION


def handle_print_progress(event: PrintStatusEvent):
    from print_nanny_webapp.alerts.tasks.alerts import AlertTask

    progress = event.event_data["print_progress"]
    alert_settings, created = AlertSettings.objects.get_or_create(user=event.user)
    should_alert = (
        progress % alert_settings.print_progress_percent == 0
        and progress != 100
        and progress != 0
    )
    if event.print_session:
        PrintSession.objects.filter(id=event.print_session.id).update(
            filepos=event.octoprint_printer_data["progress"]["filepos"],
            print_progress=progress,
            time_elapsed=event.octoprint_printer_data["progress"]["printTime"],
            time_remaining=event.octoprint_printer_data["progress"]["printTimeLeft"],
        )

    if should_alert:
        for alert_method in alert_settings.alert_methods:
            alert_message = AlertMessage.objects.create(
                alert_method=alert_method,
                event_type=AlertMessage.AlertMessageType.PRINT_PROGRESS,
                user=event.user,
                print_session=event.print_session,
                octoprint_device=event.octoprint_device,
                event=event,
            )
            task = AlertTask(alert_message)
            task.trigger_alert()


def handle_print_status(event: PrintStatusEvent) -> OctoPrintDevice:
    """
    Exclude PrintDone if monitoring is active (video render will duplicate alert)
    """
    if event.printer_state:
        event.octoprint_device.printer_state = event.printer_state
    if event.event_type != PrintStatusEventType.PRINTER_STATE_CHANGED:
        event.octoprint_device.print_job_status = event.event_type
    return event.octoprint_device.save()

def handle_ping(event: OctoPrintEvent):
    try:
        RemoteControlCommand.objects.create(
            user=event.user,
            device=event.octoprint_device,
            command=RemoteControlCommand.Command.PONG,
        )
    except google.api_core.exceptions.FailedPrecondition as e:
        logger.error(
            f"Ping response for octoprint_event={event} octoprint_device={event.octoprint_device} failed with error={e}"
        )


HANDLER_FNS = { OctoprintEventType.PRINT_PROGRESS: handle_print_progress }

HANDLER_FNS.update(
    {value: handle_print_status for label, value in PrintStatusEventType.choices}
)

HANDLER_FNS.update({PrintNannyPluginEventType.CONNECT_TEST_MQTT_PING: handle_ping})


def get_resourcetype(validated_data):
    event_type = validated_data["event_type"]
    if event_type in OctoprintEventType:
        resourcetype = OctoPrintEvent._meta.object_name
    elif event_type in PrintStatusEventType:
        resourcetype = PrintStatusEvent._meta.object_name
    elif event_type in RemoteCommandEventType:
        resourcetype = RemoteCommandEvent._meta.object_name
    elif event_type in PrintNannyPluginEventType:
        resourcetype = PrintNannyPluginEvent._meta.object_name
    else:
        resourcetype = TelemetryEvent._meta.object_name
        logger.warning(
            f"Using base TelemetryEvent for event_type={event_type} - you probably want to create a more specific subclass. Recevied data={validated_data}"
        )
    return resourcetype


def on_octoprint_event(message):
    from print_nanny_webapp.telemetry.api.serializers import (
        TelemetryEventSerializer,
        TelemetryEventPolymorphicSerializer,
    )

    try:
        data = message.data.decode("utf-8")
    except UnicodeDecodeError as e:
        logger.error(e)
        logger.warning(f"Ignoring msg with content={message.data}")
        message.ack()
        return
    data = json.loads(data)
    logger.info(f"Received {data}")

    meta_serializer = TelemetryEventSerializer(data=data)
    logger.info(f"Received {data}")

    if not meta_serializer.is_valid():
        logger.error(
            f"Meta deserialization failed with errors {meta_serializer.errors} and data {data}"
        )
        return message.ack()
    resourcetype = get_resourcetype(meta_serializer.validated_data)
    

    data = dict(
        resourcetype=resourcetype,
        printer_state=data["octoprint_printer_data"]["state"]["text"],
        **data
    )
    poly_serializer = TelemetryEventPolymorphicSerializer(
        data=data
    )
    if not poly_serializer.is_valid():
        logger.error(
            f"Polymorphic deserialization failed with errors {poly_serializer.errors} and data {data}"
        )
        return message.ack()
    instance = poly_serializer.save()
    logger.info(f"Created event {instance} event_type={instance.event_type}")
    handler_fn = HANDLER_FNS.get(instance.event_type)
    if handler_fn is not None:
        logger.info(f"Calling {handler_fn}({instance})")
        handler_fn(instance)

    message.ack()


future = subscriber.subscribe(subscription_name, on_octoprint_event)

if __name__ == "__main__":
    logger.info(f"Initializing subscription to {subscription_name}")
    future.result()
