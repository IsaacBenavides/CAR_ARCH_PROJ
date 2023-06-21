from django.urls import path
from apps.students.views import LoadStudents

app_name = "Students"

urlpatterns = [path("load/", LoadStudents.as_view(), name="home")]
