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
import stringcase

application = get_wsgi_application()
from django.apps import apps
from print_nanny_webapp.alerts.models import AlertEventTypes
from print_nanny_webapp.alerts.tasks.alerts import AlertTask
from print_nanny_client.flatbuffers.alerts import Alert, AlertEventTypeEnum


OctoPrintEvent = apps.get_model("telemetry", "OctoPrintEvent")
OctoPrintPluginEvent = apps.get_model("telemetry", "OctoPrintEvent")
PrintStatusEvent = apps.get_model("telemetry", "PrintStatusEvent")
AlertSettings = apps.get_model("alerts", "AlertSettings")
AlertMessage = apps.get_model("alerts", "AlertMessage")
PrintSession = apps.get_model("remote_control", "PrintSession")

logger = logging.getLogger(__name__)
subscriber = pubsub_v1.SubscriberClient()
subscription_name = settings.GCP_PUBSUB_OCTOPRINT_ALERTS_SUBSCRIPTION

def flatbuffer_enum_to_choices(event_type):
    name = AlertEventTypeEnum(event_type).name
    attr = stringcase.uppercase(name)
    return getattr(AlertEventTypes, atrr)

def on_alert_event(message):
    obj = Alert.Alert.GetRootAsMonitoringEvent(message.data, 0)

    flatbuffer_event_type = obj.EventType()
    choices_event_type = flatbuffer_enum_to_choices(flatbuffer_event_type)    
    if flatbuffer_event_type == AlertEventTypeEnum.video_done:
        user_id = obj.Metadata().UserId()
        octoprint_device_id = obj.Metadata().OctoPrintDeviceId()
        print_session = obj.Metadata().PrintSession()
        annotated_video = obj.AnnotatedVideo().CdnRelativePath()

        alert_settings, created = AlertSettings.objects.get_or_create(
            user=user_id,
        )
        print_session = PrintSession.objects.get(session=print_session)
        for alert_method in alert_settings.alert_methods:
            alert_message = AlertMessage.objects.create(
                user_id=user_id,
                event_type=choices_event_type,
                octoprint_device_id=octoprint_device_id,
                annotated_video=annotated_video,
                print_session=print_session,
                alert_method=alert_method
            )
            logger.info(f"Created AlertMessage with id={alert_message.id}")
            task = AlertTask(alert_message)
            task.trigger_alert()
    else:
        logger.error(f"Received event_type={flatbuffer_event_type} but no handler configured, ignoring")
    message.ack()


future = subscriber.subscribe(subscription_name, on_alert_event)

if __name__ == "__main__":
    future.result()
