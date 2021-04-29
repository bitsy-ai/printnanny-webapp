from django.urls import path, re_path

from .consumers import MonitoringFrameReceiver, MonitoringFramePublisher


websocket_urlpatterns = [
    path(
        "ws/<int:octoprint_device_id>/video/upload/", MonitoringFrameReceiver.as_asgi()
    ),
    path(
        "ws/<int:octoprint_device_id>/video/download/",
        MonitoringFramePublisher.as_asgi(),
    ),
]
