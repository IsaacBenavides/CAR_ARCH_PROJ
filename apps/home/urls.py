from django.urls import path
from apps.home.views import HomeView

app_name = "Home"

urlpatterns = [path("", HomeView.as_view(), name="home")]
