import json
import logging
import base64
import hashlib
from channels.generic.websocket import WebsocketConsumer, SyncConsumer, JsonWebsocketConsumer
from django.apps import apps
from django.contrib.auth import get_user_model
from django.conf import settings
from asgiref.sync import async_to_sync
from django.core.files.base import ContentFile

from print_nanny_webapp.utils.constants import PluginEvents
from print_nanny_webapp.utils.prometheus_metrics import (
    annotated_ws_publisher_connected_metric,
    annotated_ws_consumer_connected_metric,
)

logger = logging.getLogger(__name__)

PrintJob = apps.get_model("remote_control", "PrintJob")
ObjectDetectEventImage = apps.get_model("client_events", "ObjectDetectEventImage")

User = get_user_model()


class MonitoringFramePublisher(JsonWebsocketConsumer):
    def connect(self):
        self.accept()
        self.user = self.scope["user"]
        self.device_id = self.scope["url_route"]["kwargs"]["device_id"]
        async_to_sync(self.channel_layer.group_add)(
            f"video_{self.device_id}", self.channel_name
        )

        logger.info(f"Consumer for {self.device_id} connected")

        annotated_ws_consumer_connected_metric.inc()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            f"video_{self.device_id}", self.channel_name
        )

        super().disconnect(close_code)

        annotated_ws_consumer_connected_metric.dec()

    def video_frame(self, message):
        self.send_json(message)


class MonitoringFrameReceiver(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.user = self.scope["user"]
        self.device_id = self.scope["url_route"]["kwargs"]["device_id"]

        logger.info(f"Publisher for {self.device_id} connected")

        annotated_ws_publisher_connected_metric.inc()

    def disconnect(self, close_code):

        super().disconnect(close_code)
        annotated_ws_publisher_connected_metric.dec()

    def receive(self, text_data):
        data = json.loads(text_data)

        if data.get("event_type") == "ping":
            return self.send(text_data="pong")

        elif data.get("event_type") == PluginEvents.MONITORING_FRAME_DONE.value:
            async_to_sync(self.channel_layer.group_send)(
                f"video_{self.device_id}",
                {"type": "video.frame", **data},
            )
