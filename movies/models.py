from pydoc import synopsis
from uuid import uuid4
from django.db import models


class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10)
    premiere = models.DateField()
    classification = models.IntegerField()
    synopsis = models.TextField()

    genres = models.ManyToManyField(to="genres.Genre")
