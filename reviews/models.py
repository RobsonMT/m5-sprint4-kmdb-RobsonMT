from uuid import uuid4
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class RecommendationType(models.TextChoices):
    MUST = "Must Watch"
    SHOULD = "Should Watch"
    AVOID = "Avoid Watch"
    NO = "No Opinion"


class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    stars = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    review = models.TextField()
    spoilers = models.BooleanField(default=False)

    recommendation = models.CharField(
        max_length=50,
        choices=RecommendationType.choices,
        default=RecommendationType.NO,
    )

    movie = models.ForeignKey(
        to="movies.Movie", on_delete=models.CASCADE, related_name="reviews"
    )

    critic = models.ForeignKey(
        to="users.User", on_delete=models.CASCADE, related_name="reviews"
    )
