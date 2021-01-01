from django.urls import path

from .consumers import ObjectDetectEventConsumer, VideoConsumer

websocket_urlpatterns = [
    path("ws/images/", ObjectDetectEventConsumer.as_asgi()),
    path("ws/video/", VideoConsumer.as_asgi()),
]
