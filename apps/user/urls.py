from django.urls import path
from apps.user.views import *

app_name = "users"

urlpatterns = [
    path(
        "signup/",
        SignUpView.as_view(),
    ),
    path(
        "login/",
        LoginView.as_view(),
    ),
    path(
        "logout/",
        LogoutView.as_view(),
    ),
    path(
        "close/messages/",
        CloseMessages.as_view(),
    ),
]
