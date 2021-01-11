import logging

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer, SyncConsumer

logger = logging.getLogger(__name__)

class AlertConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.user = self.scope["user"]
        # self.device_id = self.scope["url_route"]["kwargs"]["device_id"]
        async_to_sync(self.channel_layer.group_add)(
            f"alerts_{self.user.id}", self.channel_name
        )

        # logger.info(f'Consumer for {self.device_id} connected')


    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            f"alerts_{self.user.id}", self.channel_name
        )

        super().disconnect(close_code)


    def alert(self, message):
        self.send(message)
