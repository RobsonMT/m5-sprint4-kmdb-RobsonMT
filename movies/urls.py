from django.urls import path

from movies.views import MovieIdView, MovieView


urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("movies/<movie_id>", MovieIdView.as_view()),
]
