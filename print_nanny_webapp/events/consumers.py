import logging
from channels.generic.websocket import AsyncJsonWebsocketConsumer

logger = logging.getLogger(__name__)


class EventConsumer(AsyncJsonWebsocketConsumer):
    # set in print_nanny_vue/src/store/tasks/index.js
    EVENTS_NAMESPACE = "EVENTS"
    ALERT_NAMESPACE = "ALERTS"

    EVENTS_MUTATION = "SET_EVENT"
    EVENTS_ACTION = "handleEvent"

    user = None
    group_name = None

    async def connect(self):
        await self.accept()
        self.user = self.scope["user"]
        self.group_name = f"events_{self.user.id}"
        logger.info("Websocket connection accepted scope=%s", self.scope)
        await self.channel_layer.group_add(self.group_name, self.channel_name)

    async def disconnect(self, code):
        await super().disconnect(code)
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive_json(self, content, **kwargs):
        raise NotImplementedError("Receiving JSON not yet supported over websocket")

    async def event_send(self, event):
        """
        https://github.com/nathantsoi/vue-native-websocket#with-format-json-enabled

        vue-native-websocket will automatically map the following values if provided:
        .namespace - map to module namespace defined in print_nanny_vue/src/store/index.js
        .mutation - automatically call SOCKET_[mutation value]
        .action - automatically call action
        """
        event["namespace"] = self.EVENTS_NAMESPACE
        event["mutation"] = self.EVENTS_MUTATION
        event["action"] = self.EVENTS_ACTION
        logger.info(
            "Sending event scope=%s group_name=%s event=%s",
            self.scope,
            self.group_name,
            event,
        )
        await self.send_json(event)
