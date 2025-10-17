from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import apps.tasks.routing
from django.urls import re_path
from tasks.consumers import TaskConsumer

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter([
            re_path(r"ws/tasks/$", TaskConsumer.as_asgi()),
        ])
    ),
})
