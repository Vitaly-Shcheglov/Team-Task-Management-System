from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'middle_name', 'last_name', 'email', 'password', 'role')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            import bcrypt
            hashedpassword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            instance.password = hashedpassword.decode('utf-8')
        instance.save()
        return instance


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
