import logging
import requests
from django.apps import apps
from rest_framework.renderers import JSONRenderer
from google.cloud import iot_v1 as cloudiot_v1
from print_nanny_webapp.events.api.serializers import PolymorphicEventSerializer
from rest_framework.renderers import JSONRenderer
from print_nanny_webapp.devices.enum import JanusConfigType
from django.conf import settings

from print_nanny_webapp.devices.models import (
    Device,
    JanusAuth,
    JanusStream,
)

Device = apps.get_model("devices", "Device")
DeviceEvent = apps.get_model("events", "DeviceEvent")

logger = logging.getLogger(__name__)


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


def janus_cloud_add_token(token: str) -> Dict[str, Any]:
    url = f"{settings.JANUS_CLOUD_ADMIN_URL}"
    req = dict(
        janus="add_token",
        token=token,
        admin_secret=settings.JANUS_CLOUD_ADMIN_SECRET,
        plugins=["janus.plugin.streaming"],
    )
    res = requests.post(url, data=req)
    logger.info("Got response to POST %s: %s", url, res)
    res.raise_for_status()
    return res.json()


def janus_cloud_get_or_create_media(device: Device, auth: JanusAuth) -> JanusStream:
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


def janus_stream_get_or_create(device: Device) -> JanusStream:
    # 2) get or create Janus credentials
    janus_cloud_auth, created = JanusAuth.objects.get_or_create(user=device.user)
    logger.debug(
        "retrieved JanusAuth id=%s user=%s created=%s",
        janus_cloud_auth.id,
        device.user.id,
        created,
    )
    # 3) ensure token added to Janus gateway
    janus_cloud_add_token(janus_cloud_auth.api_token)

    # 4) create streaming mountpoint
    stream = janus_cloud_get_or_create_media(device, janus_cloud_auth)
    return stream
    # # 5) send mqtt message with streaming mountpoint
    # logger.info("Created task=%s with task_status=%s", task, task_status)
    # # serialize to json
    # serializer = MonitoringStartTaskSerializer(instance=task)
    # msg = JSONRenderer().render(serializer.data)
    # logger.info("Serialized msg % with payload %", task.name, msg)
