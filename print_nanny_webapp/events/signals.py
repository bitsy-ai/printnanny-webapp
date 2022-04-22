import logging
from typing import Callable, Dict, Tuple, Any

from django.dispatch import receiver
from django.db.models.signals import post_save
from print_nanny_webapp.events.models import Event
from .services import (
    broadcast_event,
    webrtc_stream_start,
    webrtc_stream_stop,
)
from .enum import WebRTCEventName, WebRTCCommandName

logger = logging.getLogger(__name__)

created_handlers: Dict[str, Callable[..., Any]] = {
    WebRTCCommandName.STREAM_START.value: webrtc_stream_start,
    WebRTCCommandName.STREAM_STOP.value: webrtc_stream_stop,
    WebRTCEventName.STREAM_START_ERROR.value: broadcast_event,
    WebRTCEventName.STREAM_START_SUCCESS.value: broadcast_event,
}


@receiver(post_save, dispatch_uid="event_handler")
def handle_event(sender, instance, created, **kwargs):
    if created is True and isinstance(instance, Event):
        handler = created_handlers.get(instance.event_name)
        logger.info(
            "events.signals.handle_event calling handler %s with instance %s event_type %s",
            handler,
            instance,
            instance.model,
        )

        if handler is None:
            logger.debug("No handler configured for event_type=%s in events.signals")
            return
        else:
            return handler(instance)
