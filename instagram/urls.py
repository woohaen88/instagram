from django.urls import path
from .views import index, post_new


app_name = "instagram"
urlpatterns = [
    path("", index, name="index"),
    path("post/new/", post_new, name="post_new"),
]
