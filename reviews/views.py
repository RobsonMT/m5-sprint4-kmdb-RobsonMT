from django.forms import ValidationError
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView, Response, Request, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from reviews.permissions import ReviewPermission
from reviews.serializer import ReviewSerializer

from .models import Review


class ReviewView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, _, movie_id: str):
        reviews = Review.objects.filter(movie_id=movie_id)
        serialized = ReviewSerializer(reviews, many=True)
        return Response(serialized.data, status.HTTP_200_OK)

    def post(self, request, movie_id: str):
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            serializer.save(critic=request.user, movie_id=movie_id)
            return Response(serializer.data, status.HTTP_201_CREATED)
        except ValidationError as err:
            return Response({"error": err}, status.HTTP_400_BAD_REQUEST)


class ListReviewView(APIView):
    def get(self, _: Request):
        reviews = Review.objects.all()
        serialized = ReviewSerializer(reviews, many=True)
        return Response(serialized.data, status.HTTP_200_OK)


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
