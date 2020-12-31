import json
import logging
import base64
import hashlib
from channels.generic.websocket import WebsocketConsumer, SyncConsumer
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

PrintJob = apps.get_model("remote_control", "PrintJob")
ObjectDetectEventImage = apps.get_model("client_events", "ObjectDetectEventImage")

User = get_user_model()


class VideoConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.user = self.scope["user"]
        async_to_sync(self.channel_layer.group_add)(
            f"video_{self.user.id}", self.channel_name
        )

        annotated_ws_consumer_connected.inc()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            f"video_{self.user.id}", self.channel_name
        )

        super().disconnect(close_code)

        annotated_ws_consumer_connected.dec()

    def video_frame(self, message):
        logging.info("Received video message")
        self.send(message["data"])


class ObjectDetectEventConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.user = self.scope["user"]

        annotated_ws_publisher_connected_metric.inc()

    def disconnect(self, close_code):

        super().disconnect(close_code)
        annotated_ws_publisher_connected_metric.dec()

    def receive(self, text_data):
        data = json.loads(text_data)

        if data.get("event_type") == "ping":
            return self.send(text_data="pong")

        elif data.get("event_type") == "predict":
            annotated_image = base64.b64decode(data["annotated_image"])

            async_to_sync(self.channel_layer.group_send)(
                f"video_{self.user.id}",
                {"type": "video.frame", "data": data["annotated_image"]},
            )

            original_image = ContentFile(data["original_image"])
            annotated_image = ContentFile(data["annotated_image"])

            event = ObjectDetectEventImage.objects.create(
                created_dt=data["ts"],
                uuid=data["uuid"],
                user=self.scope.user,
                print_job=job,
            )

            event.annotated_image.save(f'{event.uuid}.jpg', annotated_image)
            event.original_image.save(f'{event.uuid}.jpg', original_image)
            event.save()
