from discord import channel
from django.urls import path

from .consumers import AlertConsumer, DiscordConsumer

websocket_urlpatterns = [path("ws/alerts/", AlertConsumer.as_asgi())]
