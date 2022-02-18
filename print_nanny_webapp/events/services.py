import logging
from typing import Dict, Any
from uuid import uuid4
import requests
from django.apps import apps
from rest_framework.renderers import JSONRenderer
from google.cloud import iot_v1 as cloudiot_v1
from print_nanny_webapp.devices.models import JanusStream
from print_nanny_webapp.events.api.serializers import PolymorphicEventSerializer
from rest_framework.renderers import JSONRenderer
from print_nanny_webapp.devices.enum import JanusConfigType
from django.conf import settings

from .models import WebRTCEvent
from .enum import WebRTCEventType


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
    stream = JanusStream.objects.get_or_create(device=device)
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


def webrtc_stream_start_success(event: WebRTCEvent):
    pass


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
        success_event = WebRTCEvent.objects.create(
            event_type=WebRTCEventType.STREAM_START_SUCCESS,
            stream=stream,
            device=event.device,
        )
        return success_event
    except Exception as e:
        logger.error("Error handling event=%s error=%s", event, e)
        error_event = WebRTCEvent.objects.create(
            event_type=WebRTCEventType.STREAM_START_ERROR,
            stream=stream,
            device=event.device,
        )
        return error_event


def publish_cloudiot_command(event: DeviceEvent):
    device: Device = event.device
    serializer = PolymorphicEventSerializer(instance=event)
    data = JSONRenderer().render(serializer.data)
    request = cloudiot_v1.types.SendCommandToDeviceRequest(
        {
            "name": device.cloudiot.gcp_resource,
            "binary_data": data,
            # NOTE "subfolder" may be added to publish to a subfolder
            # "subfolder": device.cloudiot.event_topic,
        }
    )

    response = device.cloudiot.client.send_command_to_device(request=request)
    logger.info(f"cloudiot.client.send_command_to_device response {response}")
    return response
