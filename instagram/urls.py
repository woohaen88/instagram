from django.urls import path
from .views import index


app_name = "instagram"
urlpatterns = [
    path("", index, name="index"),
]
