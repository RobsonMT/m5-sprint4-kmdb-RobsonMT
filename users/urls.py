from django.urls import path

from . import views

urlpatterns = [
    path("users/register/", views.RegisterView.as_view()),
    path("users/login/", views.LoginView.as_view()),
    path("users/", views.UserView.as_view()),
    path("users/<user_id>/", views.UserIdView.as_view()),
]
