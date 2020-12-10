from django.urls import path

from .consumers import PredictEventConsumer

websocket_urlpatterns = [
    path(r'ws/predict/(?P<print_job_id>\d+)/$', PredictEventConsumer.as_asgi()),
]