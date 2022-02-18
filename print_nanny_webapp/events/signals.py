import logging
from typing import Callable, Dict, Tuple

from django.dispatch import receiver
from django.db.models.signals import post_save
from print_nanny_webapp.events.models import Event, WebRTCEvent
from .services import (
    publish_cloudiot_command,
    webrtc_stream_start,
    webrtc_stream_start_success,
)
from .enum import WebRTCEventType

logger = logging.getLogger(__name__)

handlers: Dict[Tuple, Callable] = {
    WebRTCEventType.STREAM_START: webrtc_stream_start,
    WebRTCEventType.STREAM_START_SUCCESS: webrtc_stream_start_success,
}


# @receiver(post_save, dispatch_uid="event_mqtt_publisher")
# def publish_device_event(sender, instance, created, **kwargs):
#     logger.info(f"Saved DeviceEvent {instance}")
#     if isinstance(instance, DeviceEvent):
#         logger.info(f"Attempting to publish DeviceEvent to command topic {instance}")
#         publish_cloudiot_command(instance)


@receiver(post_save, dispatch_uid="event_handler")
def handle_event(sender, instance, created, **kwargs):
    if isinstance(instance, WebRTCEvent):
        handler = handlers.get(instance.event_type)
        if handler is None:
            logger.debug("No handler configured for event_type=%s in events.signals")
            return
        else:
            return handler(instance)
