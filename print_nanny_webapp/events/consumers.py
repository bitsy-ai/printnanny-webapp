import logging
from channels.generic.websocket import AsyncJsonWebsocketConsumer

logger = logging.getLogger(__name__)


class EventConsumer(AsyncJsonWebsocketConsumer):
    # set in print_nanny_vue/src/store/tasks/index.js
    TASK_NAMESPACE = "TASKS"
    ALERT_NAMESPACE = "ALERTS"

    MUTATION_SET_TASK_DATA = "SET_TASK_DATA"
    MUTATION_SET_DEVICE_DATA = "SET_DEVICE_DATA"

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
        """
        https://github.com/nathantsoi/vue-native-websocket#with-format-json-enabled

        vue-native-websocket will automatically map the following values if provided:
        .namespace - map to module namespace defined in print_nanny_vue/src/store/index.js
        .mutation - automatically call SOCKET_[mutation value]
        .action - automatically call action
        """
        event["namespace"] = self.TASK_NAMESPACE
        event["mutation"] = self.MUTATION_SET_TASK_DATA
        logger.info(
            f"Sending event scope={self.scope} group_name={self.group_name} event={event}"
        )
        await self.send_json(event)
