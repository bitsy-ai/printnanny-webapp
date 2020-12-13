from django.urls import path

from .consumers import PredictEventConsumer

websocket_urlpatterns = [
    path("ws/predict/<print_job_id>", PredictEventConsumer.as_asgi()),
]
