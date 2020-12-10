import json

from .models import PredictEvent, PredictEventFile
from channels.generic.websocket import WebsocketConsumer
from django.core.files.uploadedfile import SimpleUploadedFile

class PredictEventConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data = json.loads(text_data)
        print_job_id = self.scope['url_route']['kwargs']['print_job_id']
        files = PredictEventFile.objects.create(
            annotated_image=SimpleUploadedFile('annotated_image.jpg', data['annotated_image']),
            hash=data['file'],
            original_image=SimpleUploadedFile('original_image.jpg', data['original_image']),
        )

        predict_event = PredictEvent.objects.create(
            dt=data['ts'],
            predict_data=data['predict_data'],
            user=self.request.user,
            files=files,
            print_job=print_job_id
        )

