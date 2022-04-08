import logging
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework.renderers import JSONRenderer
from google.cloud import iot_v1 as cloudiot_v1
from print_nanny_webapp.devices.models import (
    CloudiotDevice,
)
from print_nanny_webapp.events.api.serializers import PolymorphicEventSerializer
from .models import WebRTCEvent, Event
from .enum import WebRTCEventName

logger = logging.getLogger(__name__)


def publish_mqtt_command(
    cloudiot: CloudiotDevice, serializer: PolymorphicEventSerializer, subfolder=None
):
    """
    Publish data to MQTT events topic (optional subfolder)
    """
    data = JSONRenderer().render(serializer.data)

    request = cloudiot_v1.types.SendCommandToDeviceRequest(
        {
            "name": cloudiot.gcp_resource,
            "binary_data": data,
            # NOTE "subfolder" may be added to publish to a subfolder
            # "subfolder": device.cloudiot.event_topic,
        }
    )
    if subfolder is not None:
        request.subfolder = subfolder

    response = cloudiot.client.send_command_to_device(request=request)
    logger.info(
        "cloudiot.client.send_command_to_device response %s",
        response,
    )
    return response


def publish_channel_msg(events_channel: str, serializer: PolymorphicEventSerializer):
    """
    Publish data to Django channel (propagated to connected websockets)
    """
    channel_layer = get_channel_layer()
    data = dict(namespace="EVENTS", mutation="SET_RECEIVED_EVENT", data=serializer.data)
    utf8_data = JSONRenderer().render(data).decode("utf-8")

    async_to_sync(channel_layer.group_send)(
        events_channel,
        {
            "type": "event.send",
            "data": utf8_data,
        },
    )


def broadcast_event(event: Event):
    """
    Publishes event to all receiving channels

    /ws/events Websocket - receives all Events
    /devices/:id/commands/# MQTT command topic - receives all Events with Event.device set
    """
    serializer = PolymorphicEventSerializer(instance=event)

    if event.send_ws is True:
        publish_channel_msg(event.device.user.events_channel, serializer)
        logger.info("Published event %s to Django channel", event)
    else:
        logger.warning("Event.send_ws is False, skipping. %s", event)
    if hasattr(event, "device") and event.device is not None:
        if event.send_mqtt is True:
            publish_mqtt_command(event.device.cloudiot, serializer)
            logger.info("Published event %s to MQTT commands topic", event)
        else:
            logger.warning("Event.send_mqtt broadcast is False, skipping. %s", event)


def webrtc_stream_start(event: WebRTCEvent) -> WebRTCEvent:
    try:
        broadcast_event(event)
        logger.info("Success broadcasting event %s", event)
        return event
    except Exception as e:
        logger.error("Error handling event=%s error=%s", event.__dict__, e)
        error_event = WebRTCEvent.objects.create(
            event_name=WebRTCEventName.STREAM_START_ERROR,
            device=event.device,
            user=event.user,
            send_mqtt=False,
            stream=event.stream,
        )
        return error_event
