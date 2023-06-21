from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="CAR ARCHITECTURE API",
        default_version="v1",
        description="",
        terms_of_service="",
        contact=openapi.Contact(email="isaacxzx@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("", RedirectView.as_view(url="/redoc/", permanent=True)),
    path("admin/", admin.site.urls),
    path("", include("apps.user.urls")),
    path("students/", include("apps.students.urls")),
    path("api/v1/students/", include("apps.students.api.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
