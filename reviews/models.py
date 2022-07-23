from uuid import uuid4
from django.db import models


class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    stars = models.IntegerField()
    review = models.TextField()
    spoilers = models.BooleanField(default=False)
    recomendation = models.CharField(max_length=50)
