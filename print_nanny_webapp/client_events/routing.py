from django.urls import path

from .consumers import PredictEventConsumer

websocket_urlpatterns = [
    path("ws/predict", PredictEventConsumer.as_asgi()),
]
