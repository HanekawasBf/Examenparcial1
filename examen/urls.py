"""URL configuration for the examen project."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("parcial1.urls")),
]
