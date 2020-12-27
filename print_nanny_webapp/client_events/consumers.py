import json
import logging
import base64
import hashlib
from channels.generic.websocket import WebsocketConsumer, SyncConsumer
from django.apps import apps
from django.contrib.auth import get_user_model
from django.conf import settings
from asgiref.sync import async_to_sync

from print_nanny_webapp.utils.prometheus_metrics import (
    annotated_ws_publisher_connected_metric,
    annotated_ws_consumer_connected_metric
)


logger = logging.getLogger(__name__)

PredictSession = apps.get_model("client_events", "PredictSession")
PrintJob = apps.get_model("remote_control", "PrintJob")
User = get_user_model()

publisher = pubsub_v1.PublisherClient()
pubsub_topic_path = publisher.topic_path(settings.GCP_PROJECT_ID, settings.PUBSUB_CLIENT_EVENT_TOPIC)


class VideoConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.user = self.scope["user"]
        async_to_sync(self.channel_layer.group_add)(
            f"video_{self.user.id}", self.channel_name
        )

        annotated_ws_consumer_connected_metric.inc()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            f"video_{self.user.id}", self.channel_name
        )

        super().disconnect(close_code)

        annotated_ws_consumer_connected_metric.dec()

    def video_frame(self, message):
        logging.info("Received video message")
        self.send(message["data"])


class ObjectDetectEventConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.user = self.scope["user"]

        annotated_image_ws_connected_metric.inc()


    def disconnect(self, close_code):

        super().disconnect(close_code)
        annotated_image_ws_connected_metric.dec()


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

            # filelike = io.BytesIO()
            # writer = DataFileWriter(filelike, DatumWriter(), avro_schema)
            # writer.append({
            #     'created_ts': data['ts'].time,
            #     'predict_session_id': self.scope.predict_session_id,
            #     'user_id': self.scope.user.id,
            #     'print_job_id': print_job_id,
            #     'object_detect_data': data["predict_data"],
            #     'annotated_image': base64.b64decode(data["annotated_image"]),
            #     'original_image': base64.b64decode(data["original_image"])
            # })

            # future = publisher.publish(
            #     topic_path, 
            #     filelike.read(),
            #     print_job_id=print_job_id,
            #     user_id=self.scope.user.id,
            #     predict_session_id=self.scope.predict_session.id
            # )
            # future.result()

            # event = ObjectDetectEvent.objects.create(
            #     created_dt=data["ts"],
            #     predict_data=data["predict_data"],
            #     files=files,
            #     print_job=job,
            #     predict_session=self.predict_session,
            # )
