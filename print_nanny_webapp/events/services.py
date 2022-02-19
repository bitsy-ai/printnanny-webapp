import logging
from typing import Dict, Any
from uuid import uuid4
import requests
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.conf import settings
from django.apps import apps
from rest_framework.renderers import JSONRenderer
from google.cloud import iot_v1 as cloudiot_v1
from print_nanny_webapp.devices.models import CloudiotDevice, JanusStream
from rest_framework.renderers import JSONRenderer
from print_nanny_webapp.devices.enum import JanusConfigType
from print_nanny_webapp.events.api.serializers import PolymorphicEventSerializer

from .models import WebRTCEvent, Event
from .enum import WebRTCEventType

CloudiotDevice = apps.get_model("devices", "CloudiotDevice")
Device = apps.get_model("devices", "Device")
JanusAuth = apps.get_model("devices", "JanusAuth")
JanusStream = apps.get_model("devices", "JanusStream")

logger = logging.getLogger(__name__)


def janus_admin_add_token(janus_auth: JanusAuth) -> Dict[str, Any]:
    if janus_auth.config_type == JanusConfigType.CLOUD:
        req = dict(
            janus="add_token",
            token=janus_auth.api_token,
            admin_secret=settings.JANUS_CLOUD_ADMIN_SECRET,
            plugins=["janus.plugin.streaming"],
        )
        res = requests.post(janus_auth.admin_url, data=req)
        logger.info("Got response to POST %s: %s", janus_auth.admin_url, res)
        res.raise_for_status()
        return res.json()
    else:
        raise NotImplementedError(
            f"janus_admin_add_token not implemented in events.services for JanusConfigType={JanusConfigType.Edge}"
        )


def janus_cloud_get_or_create_stream(device: Device, auth: JanusAuth) -> JanusStream:
    url = f"{settings.JANUS_CLOUD_API_URL}"
    stream, _created = JanusStream.objects.get_or_create(device=device)
    media = [
        # video stream
        dict(type="video", mid=uuid4().hex, port=5105)
        # overlay
    ]
    req = dict(
        request="create",
        token=auth.api_token,
        admin_key=settings.JANUS_CLOUD_ADMIN_SECRET,
        is_private=True,
        secret=stream.secret,
        pin=stream.pin,
        media=media,
    )
    res = requests.post(url, data=req)
    logger.info("Got response to POST %s: %s", url, req)
    res.raise_for_status()

    req = dict(
        request="info",
        token=auth.api_token,
        admin_key=settings.JANUS_CLOUD_ADMIN_SECRET,
        secret=stream.secret,
    )
    res = requests.post(url, data=req)
    logger.info("Got response to POST %s: %s", url, req)
    res.raise_for_status()
    stream.info = res.json()
    stream.save()
    return stream


def publish_mqtt_command(cloudiot: CloudiotDevice, data: str, subfolder=None):
    """
    Publish data to MQTT events topic (optional subfolder)
    """
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


def publish_channel_msg(events_channel: str, data: str):
    """
    Publish data to Django channel (propagated to connected websockets)
    """
    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        events_channel,
        {
            "type": "event.send",
            # https://github.com/nathantsoi/vue-native-websocket#with-format-json-enabled
            "data": JSONRenderer().render(data),
        },
    )


# def webrtc_stream_start_success(event: WebRTCEvent):
#     serializer = PolymorphicEventSerializer(instance=event)
#     data = JSONRenderer().render(serializer.data)
#     publish_mqtt_msg(event.device.cloudiot, data)
#     publish_channel_msg(event.device.user.events_channel, data)


def broadcast_event(event: Event):
    """
    Publishes event to all receiving channels

    /ws/events Websocket - receives all Events
    /devices/:id/commands/# MQTT command topic - receives all Events with Event.device set
    """
    serializer = PolymorphicEventSerializer(instance=event)
    data = JSONRenderer().render(serializer.data)

    publish_channel_msg(event.device.user.events_channel, data)
    logger.info("Published event %s to Django channel", event)

    if hasattr(event, "device") and event.device is not None:
        publish_mqtt_command(event.device.cloudiot, data)
        logger.info("Published event %s to MQTT commands topic", event)


def webrtc_stream_start(event: WebRTCEvent) -> WebRTCEvent:
    # 1) get or create JanusAuth for user
    # TODO: implement JanusAuth.get_or_create for config_type=Edge
    try:
        janus_auth, created = JanusAuth.objects.get_or_create(
            user=event.user, config_type=JanusConfigType.CLOUD
        )
        logger.debug(
            "Retrieved JanusAuth id=%s user=%s created=%s",
            janus_auth.id,
            event.user.id,
            created,
        )

        # 2) ensure token added to Janus Gateway
        # Janus stores tokens in memory, so added tokens are flushed on restart
        janus_admin_add_token(janus_auth)

        # 3) Create steaming mountpoint
        stream = janus_cloud_get_or_create_stream(event.device, janus_auth)
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
            event_type=WebRTCEventType.STREAM_START_ERROR,
            device=event.device,
            user=event.user,
        )
        return error_event
