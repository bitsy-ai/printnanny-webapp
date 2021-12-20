from django.urls import path

from .consumers import TaskStatusConsumer

websocket_urlpatterns = [path("ws/tasks/<int:task_id>", TaskStatusConsumer.as_asgi())]
