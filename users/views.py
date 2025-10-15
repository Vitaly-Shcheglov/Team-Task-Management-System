from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
import bcrypt
from .models import User
from .serializers import UserSerializer, LoginSerializer
from apps.core.utils import generate_token


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


class LoginView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        try:
            user = User.objects.get(email=email, is_active=True)
        except User.DoesNotExist:
            return Response({"detail": "Неверные учетные данные"},
                            status=status.HTTP_401_UNAUTHORIZED)
        if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            token = generate_token(user)
            return Response({"token": token})
        else:
            return Response({"detail": "Неверные учетные данные"},
                            status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    permissionclasses = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        return Response({"detail": "Вы вышли из системы"}, status=status.HTTP200OK)
    