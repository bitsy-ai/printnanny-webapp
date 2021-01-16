from django.urls import path, re_path

from .consumers import ObjectDetectEventConsumer, VideoConsumer


websocket_urlpatterns = [
    path("ws/<int:device_id>/video/upload/", ObjectDetectEventConsumer.as_asgi()),
    path("ws/<int:device_id>/video/download/", VideoConsumer.as_asgi()),
]
