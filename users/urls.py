from django.urls import path

from users.views import LoginView, RegisterView, UserIdView, UserView

urlpatterns = [
    path("users/register/", RegisterView.as_view()),
    path("users/login/", LoginView.as_view()),
    path("users/", UserView.as_view()),
    path("users/<user_id>", UserIdView.as_view()),
]
