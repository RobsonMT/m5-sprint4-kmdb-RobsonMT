from django.urls import path

from . import views


urlpatterns = [
    path("movies/", views.MovieView.as_view()),
    path("movies/<movie_id>/", views.MovieIdView.as_view()),
]
