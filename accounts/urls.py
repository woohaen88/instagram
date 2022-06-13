from django.urls import path
from .views import (
    signup,
    SigninView,
    SignoutView,
    profile_edit,
    AuthPasswordChangeView,
)
from django.contrib.auth import views as auth_views

app_name = "accounts"
urlpatterns = [
    path("signup/", signup, name="signup"),
    path("signin/", SigninView.as_view(), name="signin"),
    path("signout/", SignoutView.as_view(), name="signout"),
    path("password_change/", AuthPasswordChangeView.as_view(), name="password_change",),
    path("edit/", profile_edit, name="profile_edit"),
]
