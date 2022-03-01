import logging
from typing import Dict, Any
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.conf import settings
from django.apps import apps
from rest_framework.renderers import JSONRenderer
from google.cloud import iot_v1 as cloudiot_v1
from print_nanny_webapp.devices.models import (
    CloudiotDevice,
    JanusStream,
    JanusAuth,
    Device,
)
from print_nanny_webapp.devices.enum import JanusConfigType
from print_nanny_webapp.events.api.serializers import PolymorphicEventSerializer
from .models import WebRTCEvent, Event
from .enum import WebRTCEventName

logger = logging.getLogger(__name__)


def janus_cloud_get_or_create_stream(device: Device, auth: JanusAuth) -> JanusStream:
    url = f"{settings.JANUS_CLOUD_API_URL}"
    stream, _created = JanusStream.objects.get_or_create(device=device)
    return stream


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
    bytes_data = JSONRenderer().render(data)

    async_to_sync(channel_layer.group_send)(
        events_channel,
        {
            "type": "event.send",
            "data": bytes_data,
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


def janus_cloud_setup(device: Device) -> JanusStream:
    # 1) get or create JanusAuth for user
    # TODO: implement JanusAuth.get_or_create for config_type=Edge
    janus_auth, created = JanusAuth.objects.get_or_create(
        user=device.user, config_type=JanusConfigType.CLOUD
    )
    logger.debug(
        "Retrieved JanusAuth id=%s user=%s created=%s",
        janus_auth.id,
        device.user.id,
        created,
    )

    # 2) ensure token added to Janus Gateway
    # Janus stores tokens in memory, so added tokens are flushed on restart
    # janus_admin_add_token(janus_auth)
    # 3) Create steaming mountpoint
    stream = janus_cloud_get_or_create_stream(device, janus_auth)
    return stream


def webrtc_stream_start(event: WebRTCEvent) -> WebRTCEvent:
    try:
        stream = janus_cloud_setup(event.device)
        event.stream = stream
        event.save()
        logger.info(
            "Added stream %s to event %s, sending to device %s via command topic %s",
            stream,
            event,
            event.device,
            event.device.cloudiot.command_topic,
        )
        broadcast_event(event)
        return event
    except Exception as e:
        logger.error("Error handling event=%s error=%s", event.__dict__, e)
        error_event = WebRTCEvent.objects.create(
            event_name=WebRTCEventName.STREAM_START_ERROR,
            device=event.device,
            user=event.user,
            send_mqtt=False,
        )
        return error_event
