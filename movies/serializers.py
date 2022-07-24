from rest_framework import serializers

from genres.models import Genre
from genres.serializers import GenreSerializer
from movies.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10)
    premiere = serializers.DateField()
    classification = serializers.IntegerField()
    synopsis = serializers.CharField(style={"base_template": "textarea.html"})

    genres = GenreSerializer(many=True)

    def create(self, validated_data):
        genres_data = validated_data.pop("genres")
        movie = Movie.objects.create(**validated_data)

        for genre in genres_data:
            genre, _ = Genre.objects.get_or_create(**genre)
            movie.genres.add(genre)

        return movie

    def update(self, instance, validated_data):

        if "genres" in validated_data:
            instance.genres.clear()

            genres_data = validated_data.pop("genres")
            for genre in genres_data:
                genre, _ = Genre.objects.get_or_create(**genre)
                instance.genres.add(genre)

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance
