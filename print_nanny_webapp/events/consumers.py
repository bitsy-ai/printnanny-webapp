import logging
from django.contrib.auth.models import AnonymousUser
from channels.generic.websocket import AsyncJsonWebsocketConsumer

logger = logging.getLogger(__name__)


class EventConsumer(AsyncJsonWebsocketConsumer):
    EVENTS_NAMESPACE = "EVENTS"
    ALERT_NAMESPACE = "ALERTS"

    EVENTS_MUTATION = "SET_RECEIVED_EVENT"

    user = None
    group_name = None

    async def connect(self):
        await self.accept()
        self.user = self.scope["user"]
        if isinstance(self.user, AnonymousUser):
            return
        else:
            self.group_name = self.user.events_channel
            logger.info("Websocket connection accepted scope=%s", self.scope)
            await self.channel_layer.group_add(self.group_name, self.channel_name)

    async def disconnect(self, code):
        await super().disconnect(code)
        if self.group_name:
            await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive_json(self, content, **kwargs):
        raise NotImplementedError("Receiving JSON not yet supported over websocket")

    async def event_send(self, event):
        await self.send(text_data=event["data"])
