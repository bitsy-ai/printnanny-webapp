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
    PrintNannyPluginEventType
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
        progress % alert_settings.print_progress_percent == 0 and progress != 100
    )
    logger.info(f"should_alert={should_alert} progress={progress} for event_type={event.event_type}")
    if should_alert:
        for alert_method in alert_settings.alert_methods:
            alert_message = AlertMessage.objects.create(
                alert_method=alert_method,
                event_type=AlertMessage.AlertMessageType.PRINT_PROGRESS,
                user=event.user,
                print_session=event.print_session,
                octoprint_device=event.octoprint_device,
                event=event
            )
            task = AlertTask(alert_message)
            task.trigger_alert()


def handle_print_status(event: PrintStatusEvent):
    """
    Exclude PrintDone if monitoring is active (video render will duplicate alert)
    """
    pass


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


HANDLER_FNS = {OctoprintEventType.PRINT_PROGRESS: handle_print_progress}

HANDLER_FNS.update(
    {value: handle_print_status for label, value in PrintStatusEventType.choices}
)

HANDLER_FNS.update({PrintNannyPluginEventType.CONNECT_TEST_MQTT_PING: handle_ping })

def get_resourcetype(validated_data):
    event_type = validated_data["event_type"]
    if event_type in OctoprintEventType:
        resourcetype = OctoPrintEvent._meta.object_name
    elif event_type in PrintStatusEventType:
        resourcetype = PrintStatusEvent._meta.object_name
    elif event_type in RemoteCommandEventType:
        resourcetype = RemoteCommandEvent._meta.object_name
    elif event_type in PrintNannyPluginEvent:
        resourcetype = PrintNannyPluginEvent._meta.object_name
    else:
        resourcetype = TelemetryEvent._meta.object_name
        logger.warning(f"Using base TelemetryEvent for event_type={event_type} - you probably want to create a more specific subclass. Recevied data={validated_data}")
    return resourcetype

def on_octoprint_event(message):
    from print_nanny_webapp.telemetry.api.serializers import TelemetryEventSerializer, TelemetryEventPolymorphicSerializer
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
        logger.error(f"Meta deserialization failed with errors {meta_serializer.errors} and data {data}")
        return message.ack()
    resourcetype = get_resourcetype(meta_serializer.validated_data)
    poly_serializer = TelemetryEventPolymorphicSerializer(data=dict(
        resourcetype=resourcetype,
        **data
    ))
    if not poly_serializer.is_valid():
        logger.error(f"Polymorphic deserialization failed with errors {poly_serializer.errors} and data {data}")
        return message.ack()
    instance = poly_serializer.save()
    logger.info(f"Created event {instance} event_type={instance.event_type}")
    handler_fn = HANDLER_FNS.get(instance.event_type)
    if handler_fn is not None:
        logger.info(f"Calling {handler_fn}({instance})")
        handler_fn(instance)

    # if not event_is_tracked(event_type):
    #     logger.error(
    #         f"Tracking event is not registered, ignoring event_type={event_type}"
    #     )
    #     return message.ack()

    # # TODO enforce a schema on this topic :facepalm:
    # event_data = data["event_data"]
    # metadata = data["metadata"]

    # octoprint_device_id = data.get("octoprint_device_id") or data.get(
    #     "metadata", {}
    # ).get("octoprint_device_id")
    # user_id = data.get("user_id") or data.get("metadata", {}).get("user_id")

    # if octoprint_device_id is None:
    #     logger.warning(f"Received {event_type} without octoprint_device_id {data}")
    #     message.ack()
    #     return
    # if user_id is None:
    #     logger.warning(f"Received {event_type} without user_id {data}")
    #     message.ack()
    #     return
    # if event_type in OctoPrintEventType:
    #     try:
    #         event = OctoPrintEvent.objects.create(
    #             created_dt=metadata["ts"],
    #             octoprint_device_id=octoprint_device_id,
    #             event_data=data,
    #             event_type=event_type,
    #             octoprint_version=metadata["octoprint_version"],
    #             plugin_version=metadata["plugin_version"],
    #             user_id=user_id,
    #         )
    #         handler_fn = HANDLER_FNS.get(event_type)
    #         if handler_fn is not None:
    #             handler_fn(data)
    #     except Exception as e:
    #         logger.error({"error": e, "data": data}, exc_info=True)
    # if event_type in PrintStatusEventType:
    #     try:
    #         PrintStatusEvent.objects.create(
    #             created_dt=metadata["ts"],
    #             # current_z=data["printer_data"]["currentZ"],
    #             octoprint_device_id=octoprint_device_id,
    #             event_data=data,
    #             event_type=event_type,
    #             job_data_file=data["printer_data"]["job"]["file"],
    #             octoprint_version=metadata["octoprint_version"],
    #             plugin_version=metadata["plugin_version"],
    #             # progress=data["printer_data"]["progress"],
    #             # state=data["printer_data"]["state"],
    #             user_id=user_id,
    #         )
    #         handler_fn = HANDLER_FNS.get(event_type)
    #         if handler_fn is not None:
    #             handler_fn(event)
    #     except Exception as e:
    #         logger.error({"error": e, "data": data})

    # if (
    #     OctoPrintPluginEvent.strip_octoprint_prefix(event_type)
    #     in OctoPrintPluginEvent.EventType
    # ):
    #     try:
    #         obj = OctoPrintPluginEvent.objects.create(
    #             created_dt=metadata["ts"],
    #             octoprint_device_id=octoprint_device_id,
    #             event_data=data,
    #             event_type=event_type,
    #             octoprint_version=metadata["octoprint_version"],
    #             plugin_version=metadata["plugin_version"],
    #             user_id=user_id,
    #             metadata=metadata,
    #             octoprint_job=data.get("octoprint_job"),
    #         )

    #         handler_fn = HANDLER_FNS.get(
    #             OctoPrintPluginEvent.strip_octoprint_prefix(event_type)
    #         )
    #         if handler_fn is not None:
    #             handler_fn(data)
    #     except Exception as e:
    #         logger.error({"error": e, "data": data})
    message.ack()


future = subscriber.subscribe(subscription_name, on_octoprint_event)

if __name__ == "__main__":
    logger.info(f"Initializing subscription to {subscription_name}")
    future.result()
