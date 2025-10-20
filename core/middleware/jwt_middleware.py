import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.deprecation import MiddlewareMixin

User = get_user_model()


class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION", "")
        if auth_header.startswith("Bearer "):
            token = auth_header.split("Bearer ")[1]
            try:
                payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
                user_id = payload.get("user_id")
                try:
                    user = User.objects.get(id=user_id, is_active=True)
                    request.user = user
                except User.DoesNotExist:
                    request.user = None
            except jwt.ExpiredSignatureError:
                request.user = None
            except jwt.InvalidTokenError:
                request.user = None
        else:
            request.user = None
