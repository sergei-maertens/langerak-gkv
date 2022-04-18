from django.urls import path

from .views import (
    LoginModalView,
    LoginView,
    LogoutView,
    UpdateProfileView,
    UserListView,
    UserProfileView,
    UserSearchView,
)

app_name = "users"

urlpatterns = [
    path("", UserListView.as_view(), name="list"),
    path("search/", UserSearchView.as_view(), name="search"),
    path("me/", UpdateProfileView.as_view(), name="profile-edit"),
    path("<int:pk>/", UserProfileView.as_view(), name="profile"),
    path("modal/login/", LoginModalView.as_view(), name="login-modal-form"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
