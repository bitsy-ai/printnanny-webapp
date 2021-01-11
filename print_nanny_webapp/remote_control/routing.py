from django.urls import path

from .consumers import RemoteControlCommandConsumer

websocket_urlpatterns = [
    path("ws/<int:device_id>/remote-control/", RemoteControlCommandConsumer.as_asgi())
]