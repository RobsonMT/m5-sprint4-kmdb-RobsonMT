from uuid import uuid4
from django.db import models


class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    stars = models.IntegerField()
    review = models.TextField()
    spoilers = models.BooleanField(default=False)
    recomendation = models.CharField(max_length=50)

    movie = models.ForeignKey(
        to="movies.Movie", on_delete=models.CASCADE, related_name="reviews"
    )

    critic = models.ForeignKey(
        to="users.User", on_delete=models.CASCADE, related_name="reviews"
    )
