from django.urls import path

from .views import index

app_name = "digital"

urlpatterns = [
    path("", index, name="index"),
]