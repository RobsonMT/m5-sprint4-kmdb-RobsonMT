from django.forms import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView, Request, Response, status
from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieView(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, _: Request):
        movies = Movie.objects.all()
        serialized = MovieSerializer(movies, many=True)

        return Response(serialized.data, status.HTTP_200_OK)

    def post(self, request: Request):
        serialized = MovieSerializer(data=request.data)

        serialized.is_valid(raise_exception=True)
        serialized.save()

        return Response(serialized.data, status.HTTP_201_CREATED)


class MovieIdView(APIView):
    def get(self, _, movie_id: str):
        try:
            movie = get_object_or_404(Movie, pk=movie_id)
        except ValidationError as error:
            return Response({"error": error}, status=status.HTTP_404_NOT_FOUND)

        serialized = MovieSerializer(instance=movie)

        return Response(serialized.data, status.HTTP_200_OK)
