from django.urls import path

from .views import index

app_name = "industry"

urlpatterns = [
    path("", index, name="index"),
]