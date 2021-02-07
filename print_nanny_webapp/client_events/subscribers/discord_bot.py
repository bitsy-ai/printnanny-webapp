import os
import django
import logging

import sys
sys.path.insert(0,"./")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
django.setup()

from django.conf import settings
from django.core.asgi import get_asgi_application
from channels.layers import get_channel_layer
from channels.routing import ProtocolTypeRouter
from channels.generic.websocket import AsyncJsonWebsocketConsumer

logger = logging.getLogger(__name__)

class DiscordConsumer(AsyncJsonWebsocketConsumer):
    def connect():
        print("connect")
        pass

    def disconnect():
        print("disconnect")
        pass

    def send():
        print("send")
        pass

    def receive():
        print("receive")
        pass

    def react():
        print("react")
        pass

    def get_channel():
        print("channel")
        pass

    def get_user():
        print("user")
        pass


ASGI_APPLICATION=""
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [settings.REDIS_URL],
        },
    },
}
# channel_routing = {
#     "discord.connect": connect,
#     "discord.disconnect": disconnect,
#     "discord.send": send,
#     "discord.receive": receive,
#     "discord.react": react,
#     "discord.get_channel": get_channel,
#     "discord.get_user": get_user,
# }
channel_layer = get_channel_layer()
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": DiscordConsumer.as_asgi(),
})
