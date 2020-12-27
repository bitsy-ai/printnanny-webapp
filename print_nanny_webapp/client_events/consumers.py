import json
import logging
import base64
import hashlib
# from .models import ObjectDetectEvent, ObjectDetectEventFile
from channels.generic.websocket import WebsocketConsumer, SyncConsumer
from django.core.files.uploadedfile import SimpleUploadedFile
from django.apps import apps
from django.contrib.auth import get_user_model
from django.conf import settings
from asgiref.sync import async_to_sync
from google.cloud import pubsub_v1

import avro.schema
from avro.datafile import DataFileReader
from avro.io import DatumWriter


arvo_schema = avro.schema.parse(open("arvo/models.avsc", "rb").read())

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

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            f"video_{self.user.id}", self.channel_name
        )

    def video_frame(self, message):
        logging.info("Received video message")
        self.send(message["data"])


class MetricsConsumer(SyncConsumer):

    pass


class ObjectDetectEventConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.user = self.scope["user"]


        # @todo prometheus event
        self.predict_session = PredictSession.objects.create(
            channel_name=self.channel_name, user=self.user
        )

    def disconnect(self, close_code):
        # @todo prometheus event
        self.predict_session.closed = True
        self.predict_session.save()

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

            filelike = io.BytesIO()
            writer = DataFileWriter(filelike), DatumWriter(), arvo_schema)
            writer.append({
                'created_ts': data['created_dt'].time,
                'predict_session_id': self.scope.predict_session_id,
                'user_id': self.scope.user.id,
                'print_job_id': print_job_id
            })

        

            future = publisher.publish(
                topic_path, 
                filelike.read(),
                print_job_id=print_job_id,
                user_id=self.scope.user.id,
                self.scope.predict_session.id
            )
            future.result()


            # predict_event = ObjectDetectEvent.objects.create(
            #     dt=data["ts"],
            #     predict_data=data["predict_data"],
            #     files=files,
            #     print_job=job,
            #     predict_session=self.predict_session,
            # )
