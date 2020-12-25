import json
import logging
import base64
import hashlib
from .models import PredictEvent, PredictEventFile
from channels.generic.websocket import WebsocketConsumer, SyncConsumer
from django.core.files.uploadedfile import SimpleUploadedFile
from django.apps import apps
from django.contrib.auth import get_user_model
from asgiref.sync import async_to_sync


logger = logging.getLogger(__name__)

PrintJob = apps.get_model("remote_control", "PrintJob")
User = get_user_model()

class VideoConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.user = self.scope["user"]
        async_to_sync(self.channel_layer.group_add)("video", self.channel_name)

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)("video", self.channel_name)

class MetricsConsumer(SyncConsumer):

    pass


class PredictEventConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.user = self.scope["user"]
        async_to_sync(self.channel_layer.group_add)("predict", self.channel_name)

        self.predict_session = PredictSession.objects.create(channel_name=self.channel_name, user=self.user)

    def disconnect(self, close_code):
        self.predict_session.closed = True
        self.predict_session.save()

    def receive(self, text_data):
        data = json.loads(text_data)
        logger.info(data)

        if data.get("event_type") == "ping":
            return self.send(text_data="pong")

        elif data.get("event_type") == "predict":
            annotated_image = base64.b64decode(data["annotated_image"])

            async_to_sync(self.channel_layer.group_send_json)(
                'video',
                {
                    'type': 'annotated_image',
                    'data': data["annotated_image"]
                })

            async_to_sync(self.channel_layer.group_send_json)(
                'metrics',
                {
                    'type': 'predict_data',
                    'data': data["predict_data"],
                    'user_id': self.user.id
                }
            )
            print_job_id = data.get("print_job_id")

            original_img = base64.b64decode(data["original_image"])
            imghash = hashlib.md5(original_img).hexdigest()

            files = PredictEventFile.objects.create(
                annotated_image=SimpleUploadedFile(
                    "annotated_image.jpg", annotated_image),
                hash=imghash,
                original_image=SimpleUploadedFile(
                    "original_image.jpg", base64.b64decode(data["original_image"])
                ),
            )

            if print_job_id is not None:
                job = PrintJob(id=print_job_id)
            else:
                job = None

            predict_event = PredictEvent.objects.create(
                dt=data["ts"],
                predict_data=data["predict_data"],
                user=self.user,
                files=files,
                print_job=job,
            )