from django.urls import path

from apps.ws import consumers

websocket_urlpatterns = [
    path(r"ws", consumers.WsConsumer.as_asgi()),
]