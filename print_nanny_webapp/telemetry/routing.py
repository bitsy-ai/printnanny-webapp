from django.urls import path

from .consumers import MonitoringFrameReceiver


websocket_urlpatterns = [
    path(
        "ws/<int:octoprint_device_id>/video/upload/", MonitoringFrameReceiver.as_asgi()
    )
]
