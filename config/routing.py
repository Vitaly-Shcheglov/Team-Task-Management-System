from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import apps.tasks.routing

application = ProtocolTypeRouter({
    "http":  AuthMiddlewareStack(
                URLRouter([
                ])
             ),
    "websocket": AuthMiddlewareStack(
          URLRouter(
              apps.tasks.routing.websocket_urlpatterns
          )
    ),
})
