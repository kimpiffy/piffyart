"""URL configuration for piffyart project."""

from django.contrib import admin
from django.urls import include, path

from .views import home_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("personal/", include("personal.urls")),
    path("digital/", include("digital.urls")),
    path("community/", include("community.urls")),
    path("industry/", include("industry.urls")),
    path("shop/", include("shop.urls")),
    path("contact/", include("contact.urls")),
    path("accounts/", include("accounts.urls")),
]