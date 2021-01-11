"""
ASGI config for Print Nanny Webapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/asgi/

"""
import os
import sys
import logging
from pathlib import Path


from django.core.asgi import get_asgi_application

# This allows easy placement of apps within the interior
# print_nanny_webapp directory.
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(ROOT_DIR / "print_nanny_webapp"))

# If DJANGO_SETTINGS_MODULE is unset, default to the local settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

# This application object is used by any ASGI server configured to use this file.
django_application = get_asgi_application()
# Apply ASGI middleware here.
# from helloworld.asgi import HelloWorldApplication
# application = HelloWorldApplication(application)

# Import websocket application here, so apps from django_application are loaded first
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import print_nanny_webapp.client_events.routing
import print_nanny_webapp.remote_control.routing

from rest_framework.authtoken.models import Token
from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser

logger = logging.getLogger(__name__)

async def application(scope, receive, send):
    if scope["type"] == "http":
        await django_application(scope, receive, send)
    elif scope["type"] == "websocket":
        await websocket_application(scope, receive, send)
    else:
        raise NotImplementedError(f"Unknown scope type {scope['type']}")

@database_sync_to_async
def get_user(headers):
    try:
        token_name, token_key = headers[b'authorization'].decode().split()
        if token_name == 'Bearer':
            token = Token.objects.get(key=token_key)
            return token.user
    except Token.DoesNotExist:
        return AnonymousUser()

##
# https://stackoverflow.com/questions/60009296/django-3-0-channels-asgi-tokenauthmiddleware
##
class TokenAuthMiddleware:
    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        headers = dict(scope['headers'])
        if b'authorization' in headers:
            scope['user'] = await get_user(headers)
        return await self.inner(scope, receive, send)


TokenAuthMiddlewareStack = lambda inner: TokenAuthMiddleware(AuthMiddlewareStack(inner))

websocket_urlpatterns = (
    print_nanny_webapp.client_events.routing.websocket_urlpatterns +
    print_nanny_webapp.remote_control.routing.websocket_urlpatterns
)
logging.info(f'Registering websocket urlpatterns {websocket_urlpatterns}')
application = ProtocolTypeRouter({
  "http": django_application,
  "websocket": TokenAuthMiddlewareStack(
      URLRouter(websocket_urlpatterns)),
  #"metrics": 
})