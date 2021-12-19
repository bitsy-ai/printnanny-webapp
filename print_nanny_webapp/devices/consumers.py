import logging
from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer

logger = logging.getLogger(__name__)


class TaskStatusConsumer(JsonWebsocketConsumer):
    def connecr(self):
        self.accept()

        self.user = self.scope["user"]
        async_to_sync(self.channel_layer.group_add)(
            f"tasks_{self.user.id}", self.channel_name
        )

        logger.info(f"TaskStatusConsumer for {self.user} connected")

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            f"tasks_{self.user.id}", self.channel_name
        )

        super().disconnect(close_code)

    def receive_json(self, content):

        logger.info(f"Recevied JSON Task {content}")
