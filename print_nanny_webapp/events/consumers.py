import logging
from channels.generic.websocket import AsyncJsonWebsocketConsumer

logger = logging.getLogger(__name__)


class EventConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.user = self.scope["user"]
        self.group_name = f"events_{self.user.id}"
        logger.info(f"Websocket connection accepted scope={self.scope}")
        await self.channel_layer.group_add(self.group_name, self.channel_name)

    async def disconnect(self, close_code):

        await super().disconnect(close_code)
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive_json(self, content):
        logger.info(f"Recevied JSON {content}")
        raise NotImplementedError("Receiving JSON not yet supported over websocket")

    async def task_status(self, event):
        logger.info(
            f"Received event scope={self.scope} group_name={self.group_name} event={event}"
        )
        await self.send_json(event)
