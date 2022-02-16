import logging
import requests
from uuid import uuid4
from typing import Any, Dict
from django.conf import settings
from rest_framework.renderers import JSONRenderer

from print_nanny_webapp.devices.models import (
    Device,
    JanusCloudAuth,
    JanusCloudMediaStream,
)
from print_nanny_webapp.tasks.models import (
    Task,
    MonitoringStartTask,
    MonitoringStopTask,
)
from .api.serializers import MonitoringStartTaskSerializer

logger = logging.getLogger(__name__)


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


def janus_cloud_get_or_create_stream(device: Device, auth: JanusCloudAuth):
    url = f"{settings.JANUS_CLOUD_API_URL}"
    stream = JanusCloudMediaStream.objects.get_or_create(device=device)
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
    return res.json()


def monitor_start(device: Device):
    # 2) get or create Janus credentials
    janus_cloud_auth, created = JanusCloudAuth.objects.get_or_create(user=device.user)
    logger.debug(
        "Retreived JanusCloudAuth id=%s user=%s created=%s",
        janus_cloud_auth.id,
        device.user.id,
        created,
    )
    # 3) ensure token added to Janus gateway
    janus_cloud_add_token(janus_cloud_auth.api_token)

    # 4) create streaming mountpoint
    stream = janus_cloud_get_or_create_stream(device, janus_cloud_auth)
    # 5) send mqtt message with streaming mountpoint
    task = MonitoringStartTask.objects.create(device=device, janus_media_stream=stream)
    task_status = TaskStatus.objects.create(task=task, status=TaskStatusType.PENDING)
    logger.info("Created task=%s with task_status=%s", task, task_status)
    # serialize to json
    serializer = MonitoringStartTaskSerializer(instance=task)
    msg = JSONRenderer().render(serializer.data)
    logger.info("Serialized msg % with payload %", task.name, msg)


def monitor_stop(device: Device):
    # send mqtt message
    # destroy mountpoint
    pass
