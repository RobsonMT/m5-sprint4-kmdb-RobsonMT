from django.forms import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView, Request, Response, status

from core.pagination import CustomPageNumberPagination
from reviews.permissions import ReviewPermission
from reviews.serializer import ReviewSerializer

from .models import Review


class ReviewView(APIView, CustomPageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, movie_id: str):
        reviews = Review.objects.filter(movie_id=movie_id)
        pagination = self.paginate_queryset(reviews, request, view=self)
        serialized = ReviewSerializer(pagination, many=True)

        return self.get_paginated_response(serialized.data)

    def post(self, request, movie_id: str):
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            serializer.save(critic=request.user, movie_id=movie_id)
            return Response(serializer.data, status.HTTP_201_CREATED)
        except ValidationError as err:
            return Response({"error": err}, status.HTTP_400_BAD_REQUEST)


class ListReviewView(APIView, CustomPageNumberPagination):
    authentication_classes = [TokenAuthentication]

    def get(self, request: Request):
        reviews = Review.objects.all()
        pagination = self.paginate_queryset(reviews, request, view=self)
        serialized = ReviewSerializer(pagination, many=True)

        return self.get_paginated_response(serialized.data)


class ReviewIdView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ReviewPermission]

    def delete(self, _, review_id: str):
        try:
            review = get_object_or_404(Review, pk=review_id)
            review.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        except ValidationError as error:
            return Response({"error": error}, status=status.HTTP_404_NOT_FOUND)
