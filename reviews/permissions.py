from rest_framework.permissions import BasePermission
from rest_framework.views import Request

from reviews.models import Review


class ReviewPermission(BasePermission):
    def has_permission(self, request, view):

        if request.user.is_superuser:
            return True

        review_id = view.kwargs.get("review_id", None)
        review = Review.objects.get(id=review_id)

        if request.user.id == review.critic.id:
            return True

        return False
