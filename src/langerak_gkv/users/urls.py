from django.urls import path

from .views import (
    LoginView,
    LogoutView,
    UpdateProfileView,
    UserListView,
    UserProfileView,
    UserSearchPDFView,
    UserSearchView,
)

app_name = "users"

urlpatterns = [
    path("", UserListView.as_view(), name="list"),
    path("search/", UserSearchView.as_view(), name="search"),
    path("search/pdf/", UserSearchPDFView.as_view(), name="search-pdf"),
    path("me/", UpdateProfileView.as_view(), name="profile-edit"),
    path("<int:pk>/", UserProfileView.as_view(), name="profile"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
