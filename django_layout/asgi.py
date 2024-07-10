"""
ASGI config for django_layout project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from channels_auth_token_middlewares.middleware import (
    DRFAuthTokenMiddleware,
    SimpleJWTAuthTokenMiddleware,
)
from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator

from apps.ws.routing import websocket_urlpatterns
from middleware.authentication.authentication import WSAuthentication

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setting.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AllowedHostsOriginValidator(
            WSAuthentication(URLRouter(websocket_urlpatterns))
        ),
    }
)
