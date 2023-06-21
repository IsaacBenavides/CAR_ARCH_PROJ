from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView


urlpatterns = [
    path("", RedirectView.as_view(url="/courses/load/", permanent=True)),
    path("admin/", admin.site.urls),
    path("", include("apps.user.urls")),
    path("students/", include("apps.students.urls")),
    path("api/v1/students/", include("apps.students.api.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
