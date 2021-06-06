import json
import logging
import base64
import hashlib
from channels.generic.websocket import (
    WebsocketConsumer,
    SyncConsumer,
    JsonWebsocketConsumer,
    AsyncWebsocketConsumer
)
from django.apps import apps
from django.contrib.auth import get_user_model
from django.conf import settings
from asgiref.sync import async_to_sync
from django.core.files.base import ContentFile

from print_nanny_webapp.utils.prometheus_metrics import (
    annotated_ws_publisher_connected_metric,
    annotated_ws_consumer_connected_metric,
)

logger = logging.getLogger(__name__)
User = get_user_model()

class MonitoringFrameReceiver(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        logger.info(f"Websocket connection accepted scope={self.scope} self={self}")
        self.user = self.scope["user"]
        self.octoprint_device_id = self.scope["url_route"]["kwargs"][
            "octoprint_device_id"
        ]
        self.group_name = f"video_{self.octoprint_device_id}"

    async def disconnect(self, close_code):

        await super().disconnect(close_code)
        await self.channel_layer.group_discard(
            self.group_name, self.channel_name
        )

    async def video_frame(self, message):
        logger.info(f"Received video_{self.octoprint_device_id} on channel {self.channel_name}")
        await self.send(base64.b64encode(message["image"]).decode())

    async def receive(self, bytes_data=None, text_data=None):
        if text_data is not None:
            data = json.loads(text_data)
            event_type = data.get("event_type")
            if event_type == "video_subscribe":
                await self.channel_layer.group_add(
                    self.group_name, self.channel_name
                )
        if bytes_data is not None:
            logger.info(f"Recevied {len(bytes_data)} bytes")
            await self.channel_layer.group_send(
                f"video_{self.octoprint_device_id}",
                {"type": "video.frame", "image": bytes_data},
            )
