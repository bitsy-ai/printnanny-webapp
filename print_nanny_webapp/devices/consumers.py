import logging
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncJsonWebsocketConsumer

logger = logging.getLogger(__name__)


class TaskStatusConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()

        self.user = self.scope["user"]
        self.task_id = self.scope["url_route"]["kwargs"]["task_id"]
        self.group_name = f"task_{self.task_id}"

        logger.info(f"Websocket connection accepted scope={self.scope}")

    async def disconnect(self, close_code):

        await super().disconnect(close_code)
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive_json(self, content):

        logger.info(f"Recevied JSON Task {content}")
