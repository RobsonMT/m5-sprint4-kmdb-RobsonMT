from django.urls import path

from . import views

urlpatterns = [
    path("movies/<movie_id>/reviews/", views.ReviewView.as_view()),
    path("reviews/<review_id>/", views.ReviewIdView.as_view()),
    path("reviews/", views.ListReviewView.as_view()),
]
