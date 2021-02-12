from asyncio.events import new_event_loop
import logging

import asyncio
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer, AsyncConsumer
from discord import Client as DiscordClient
from django.conf import settings

logger = logging.getLogger(__name__)

# Initialize discord client on the main thread's event loop
discord_client = DiscordClient()
try:
    asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.get_event_loop()
    loop.create_task(discord_client.start(settings.DISCORD_TOKEN))
    logger.info("Started discord loop")


class AlertConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.user = self.scope["user"]
        async_to_sync(self.channel_layer.group_add)(
            f"alerts_{self.user.id}", self.channel_name
        )

        logger.info(f"Consumer for {self.user.id} connected")

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            f"alerts_{self.user.id}", self.channel_name
        )

        super().disconnect(close_code)

    def alert_message(self, message):
        self.send(message["data"])

        logger.info(f"Received message {message}")


class DiscordConsumer(AsyncConsumer):
    async def trigger_alert(self, data):
        logger.info(f"Received message for user_ids {data['user_ids']} and channel_ids {data['channel_ids']}")
        await discord_client.wait_until_ready()

        for user in data["user_ids"]:
            target = await discord_client.fetch_user(int(user))
            # TODO: Return an error
            await self._target_send(user, target, data["message"])

        for channel in data["channel_ids"]:
            target = await discord_client.fetch_channel(int(channel))
            await self._target_send(channel, target, data["message"])

    async def _target_send(self, _id, target, message):
            if target is None:
                # TODO: Return an error
                logger.error(f"Discord could not find item '{_id}'!")
                return None

            return await target.send(message)
