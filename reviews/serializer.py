from django.forms import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from movies.models import Movie
from users.models import User

from .models import Review


class CriticSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name"]


class ReviewSerializer(serializers.ModelSerializer):
    critic = CriticSerializer(read_only=True)

    class Meta:
        model = Review

        fields = [
            "id",
            "stars",
            "review",
            "spoilers",
            "recommendation",
            "movie_id",
            "critic",
        ]

    def create(self, validated_data):
        movie_id = validated_data.pop("movie_id")
        movie: Movie = get_object_or_404(Movie, pk=movie_id)
        review = Review.objects.create(movie=movie, **validated_data)

        return review
