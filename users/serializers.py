from rest_framework import serializers, status

from core.exceptions import UniqueException
from users.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    email = serializers.EmailField(max_length=255)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=128, write_only=True)

    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def validate_email(self, email: str):
        email_exists = User.objects.filter(email=email).exists()

        if email_exists:
            raise UniqueException(
                {"email": ["email already exists."]}, status.HTTP_409_CONFLICT
            )

        return email

    def create(self, validated_data: dict):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
