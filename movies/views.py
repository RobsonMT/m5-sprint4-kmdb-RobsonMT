from django.forms import ValidationError
from django.shortcuts import get_object_or_404

from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView, Request, Response, status
from core.pagination import CustomPageNumberPagination

from movies.models import Movie
from movies.permissions import MoviePermission
from movies.serializers import MovieSerializer


class MovieView(APIView, CustomPageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MoviePermission]

    def get(self, request: Request):
        movies = Movie.objects.all()
        pagination = self.paginate_queryset(queryset=movies, request=request, view=self)
        serialized = MovieSerializer(pagination, many=True)

        return self.get_paginated_response(serialized.data)

    def post(self, request: Request):
        serialized = MovieSerializer(data=request.data)

        serialized.is_valid(raise_exception=True)
        serialized.save()

        return Response(serialized.data, status.HTTP_201_CREATED)


class MovieIdView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MoviePermission]

    def get(self, _, movie_id: str):
        try:
            movie = get_object_or_404(Movie, pk=movie_id)
        except ValidationError as error:
            return Response({"error": error}, status=status.HTTP_404_NOT_FOUND)

        serialized = MovieSerializer(instance=movie)

        return Response(serialized.data, status.HTTP_200_OK)

    def patch(self, request, movie_id):
        try:
            movie = get_object_or_404(Movie, pk=movie_id)
        except ValidationError as error:
            return Response({"error": error}, status=status.HTTP_404_NOT_FOUND)

        serialized = MovieSerializer(movie, request.data, partial=True)
        serialized.is_valid(raise_exception=True)
        serialized.save()

        return Response(serialized.data)

    def delete(self, _, movie_id):
        try:
            movie = get_object_or_404(Movie, pk=movie_id)
        except ValidationError as error:
            return Response({"error": error}, status=status.HTTP_404_NOT_FOUND)

        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
