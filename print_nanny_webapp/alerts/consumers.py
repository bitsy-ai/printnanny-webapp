import logging

import asyncio
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer, AsyncConsumer

# from discord import (
#     InvalidData,
#     HTTPException,
#     NotFound,
#     Forbidden,
#     Client as DiscordClient,
# )
from django.conf import settings

logger = logging.getLogger(__name__)

# Initialize discord client on the main thread's event loop
# discord_client = DiscordClient()
# try:
#     asyncio.get_running_loop()
# except RuntimeError:
#     loop = asyncio.get_event_loop()
#     loop.create_task(discord_client.start(settings.DISCORD_TOKEN))
#     logger.info("Started discord loop")


class AlertConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.user = self.scope["user"]
        async_to_sync(self.channel_layer.group_add)(
            f"alerts_{self.user.id}", self.channel_name
        )

        logger.info(f"AlertConsumer for {self.user} connected")

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            f"alerts_{self.user.id}", self.channel_name
        )

        super().disconnect(close_code)

    def alert_message(self, message):
        self.send(message["data"])

        logger.info(f"Received message {message}")


# class DiscordConsumer(AsyncConsumer):
#     groups = []

#     async def trigger_alerts(self, data):
#         logger.info(
#             f"Received message for user IDs {data['user_ids']} and channel IDs {data['channel_ids']}"
#         )
#         await discord_client.wait_until_ready()

#         for user in data["user_ids"]:
#             target = await discord_client.fetch_user(int(user))
#             # TODO: Return an error
#             await self._target_send(user, target, data["message"])

#         for channel in data["channel_ids"]:
#             target = await discord_client.fetch_channel(int(channel))
#             await self._target_send(channel, target, data["message"])

#     async def _target_send(self, _id, target, message):
#         if target is None:
#             # TODO: Return an error
#             logger.error(f"Discord could not find item '{_id}'!")
#             return None

#         return await target.send(message)

#     async def validate_id(self, data):
#         logger.info(f"Validating {data['target_id_type']} ID {data['target_id']}")
#         await discord_client.wait_until_ready()
#         res = {"is_valid": True, "value": data["target_id"], "error": ""}

#         fetcher = None
#         if data["target_id_type"] == "USER":
#             fetcher = discord_client.fetch_user
#         elif data["target_id_type"] == "CHANNEL":
#             fetcher = discord_client.fetch_channel
#         else:
#             res["is_valid"] = False
#             res["error"] = "Unknown ID type"
#             await self.base_send(res)

#         try:
#             await fetcher(int(data["target_id"]))
#         except (InvalidData, HTTPException, NotFound, Forbidden) as e:
#             res["is_valid"] = False
#             res[
#                 "error"
#             ] = f"During '{data['target_id']}' {data['target_id_type']} validation, the following error occurred: {e}"
#             await self.base_send(res)

#         await self.base_send(res)
