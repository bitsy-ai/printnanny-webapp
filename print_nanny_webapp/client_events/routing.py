from django.urls import path

from .consumers import PredictEventConsumer, VideoConsumer

websocket_urlpatterns = [
    path("ws/predict/", PredictEventConsumer.as_asgi()),
    path("ws/video/", VideoConsumer.as_asgi()),
]
