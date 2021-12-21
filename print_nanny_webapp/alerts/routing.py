from discord import channel
from django.conf.urls import url

from .consumers import AlertConsumer, DiscordConsumer

websocket_urlpatterns = [url(r"^ws/alerts/$", AlertConsumer.as_asgi())]
