from django.urls import path

from users.views import LoginView, UserView

urlpatterns = [
    path("users/register/", UserView.as_view()),
    path("users/login/", LoginView.as_view()),
]
