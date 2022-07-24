from django.contrib.auth import authenticate
from django.forms import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView, Request, Response, status

from users.models import User

from users.permissions import UserPermission

# from rest_framework.permissions import IsAuthenticated


from users.serializers import LoginSerializer, UserSerializer


class RegisterView(APIView):
    def post(self, request: Request):
        serialized = UserSerializer(data=request.data)

        serialized.is_valid(raise_exception=True)
        serialized.save()

        return Response(serialized.data, status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request: Request):
        serialized = LoginSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)

        user: User = authenticate(**serialized.validated_data)

        if not user:
            return Response(
                {"detail": "Invalid email or password."}, status.HTTP_401_UNAUTHORIZED
            )

        token, _ = Token.objects.get_or_create(user=user)

        return Response({"token": token.key}, status.HTTP_200_OK)


class UserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermission]
    # permission_classes = [IsAuthenticated]

    def get(self, _: Request):
        users = User.objects.all()
        serialized = UserSerializer(users, many=True)

        return Response(serialized.data, status.HTTP_200_OK)


class UserIdView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermission]

    def get(self, _, user_id: str):
        try:
            user: User = get_object_or_404(User, pk=user_id)
        except ValidationError as error:
            return Response({"error": error}, status=status.HTTP_404_NOT_FOUND)

        serialized = UserSerializer(instance=user)

        return Response(serialized.data, status.HTTP_200_OK)
