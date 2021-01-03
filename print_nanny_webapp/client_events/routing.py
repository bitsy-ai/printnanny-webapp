from django.urls import path

from .consumers import ObjectDetectEventConsumer, VideoConsumer

websocket_urlpatterns = [
    path("ws/images/<str:serial>/", ObjectDetectEventConsumer.as_asgi()),
    path("ws/video/<str:serial>/", VideoConsumer.as_asgi()),
]
