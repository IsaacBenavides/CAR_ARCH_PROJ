from django.urls import path
from apps.students.api.views import StudentsAPIView

app_name = "Students Api"

urlpatterns = [
    path("", StudentsAPIView.as_view(), name="Students"),
]
