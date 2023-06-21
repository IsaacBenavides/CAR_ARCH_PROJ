from django.urls import path
from apps.courses.views import LoadCourses


urlpatterns = [path("load/", LoadCourses.as_view(), name="load courses")]
