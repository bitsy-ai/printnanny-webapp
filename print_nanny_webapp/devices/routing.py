from django.urls import path

from .consumers import TaskStatusConsumer

websocket_urlpatterns = [path("ws/tasks/", TaskStatusConsumer.as_asgi())]
