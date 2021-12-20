from django.urls import path

from .consumers import DeviceConsumer

websocket_urlpatterns = [path("ws/devices/<int:device_id>/", DeviceConsumer.as_asgi())]
