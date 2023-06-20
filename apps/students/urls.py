from django.urls import path
from apps.students.views import HomeView

app_name = "Students"

urlpatterns = [path("", HomeView.as_view(), name="home")]
