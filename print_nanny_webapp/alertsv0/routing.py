from django.conf.urls import url

from .consumers import AlertConsumer

websocket_urlpatterns = [url(r"^ws/alerts/$", AlertConsumer.as_asgi())]
