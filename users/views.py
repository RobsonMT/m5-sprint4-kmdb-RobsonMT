from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView, Request, Response, status

from users.models import User

from users.serializers import UserSerializer


class UserView(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, _: Request):
        users = User.objects.all()
        serialized = UserSerializer(users, many=True)

        return Response(serialized.data, status.HTTP_200_OK)

    def post(self, request: Request):
        serialized = UserSerializer(data=request.data)

        serialized.is_valid(raise_exception=True)
        serialized.save()

        return Response(serialized.data, status.HTTP_201_CREATED)
