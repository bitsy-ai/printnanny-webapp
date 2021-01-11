from django.urls import path, include

import django_eventstream
from channels.routing import URLRouter
from .consumers import ObjectDetectEventConsumer, VideoConsumer

websocket_urlpatterns = [
    path("ws/remote-control/", URLRouter(django_eventstream.routing.urlpatterns), {'channels': ['remote-control-{device-id}']} ),
    path("ws/<int:device_id>/video/upload/", ObjectDetectEventConsumer.as_asgi()),
    path("ws/<int:device_id>/video/download/", VideoConsumer.as_asgi()),
]
