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
from google.protobuf.message import DecodeError
from print_nanny_webapp.alerts.tasks.alerts import AlertTask
from print_nanny_client.protobuf.alert_pb2 import VideoRenderRequest

OctoPrintEvent = apps.get_model("telemetry", "OctoPrintEvent")
OctoPrintPluginEvent = apps.get_model("telemetry", "OctoPrintEvent")
AlertSettings = apps.get_model("alerts", "AlertSettings")
AlertMessage = apps.get_model("alerts", "AlertMessage")
PrintSession = apps.get_model("remote_control", "PrintSession")

logger = logging.getLogger(__name__)
subscriber = pubsub_v1.SubscriberClient()
subscription_name = settings.GCP_PUBSUB_OCTOPRINT_ALERTS_SUBSCRIPTION


def on_alert_event(message):
    render_video_msg = VideoRenderRequest()
    try:
        render_video_msg.ParseFromString(message.data)
    except DecodeError as e:
        logger.exception(e)
        logger.error(message)
        return message.ack()

    logger.info(render_video_msg)
    user_id = render_video_msg.metadata.user_id
    print_session_str = render_video_msg.metadata.print_session.session
    octoprint_device_id = render_video_msg.metadata.octoprint_device_id
    annotated_video_path = os.path.join(
        render_video_msg.cdn_output_path, "annotated_video.mp4"
    )
    annotated_video_path = annotated_video_path.replace(
        "media/", ""
    )  # django will prepend media root, this prevents a string like print-nanny-sandbox/media/media/path/to/upload

    alert_settings, created = AlertSettings.objects.get_or_create(
        user_id=user_id,
    )
    logger.info(f"Retrieving print_session={print_session_str}")
    try:
        print_session = PrintSession.objects.get(session=print_session_str)
    except PrintSession.DoesNotExist as e:
        logger.error(e)
        logger.error(render_video_msg)
        return message.ack()

    alert_exists_for_session = AlertMessage.objects.filter(
        print_session=print_session,
        event_type=AlertMessage.AlertMessageType.VIDEO_DONE,
    ).first()

    # pubsub guarantees message deliver *at least* once, but potentially more than once. Ignore duplicate alert requests for session
    # also prevents late session data from causing alert to fire more than once
    if alert_exists_for_session:
        logger.warning(
            f"{AlertMessage.AlertMessageType.VIDEO_DONE} slert issued for session {print_session} - ignoring VideoRenderRequest {render_video_msg}"
        )
    else:
        for alert_method in alert_settings.alert_methods:
            alert_message = AlertMessage.objects.create(
                user_id=user_id,
                event_type=AlertMessage.AlertMessageType.VIDEO_DONE,
                octoprint_device_id=octoprint_device_id,
                annotated_video=annotated_video_path,
                print_session=print_session,
                alert_method=alert_method,
            )
            logger.info(f"Created AlertMessage with id={alert_message.id}")
            task = AlertTask(alert_message)
            try:
                task.trigger_alert()
            except Exception as e:
                logger.exception(e)
    message.ack()


future = subscriber.subscribe(subscription_name, on_alert_event)

if __name__ == "__main__":
    logger.info(f"Initializing subscription to {subscription_name}")
    future.result()
