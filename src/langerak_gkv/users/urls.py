from django.conf.urls import url

from .views import (
    LoginView, LogoutView, UpdateProfileView, UserListView, UserProfileView,
    UserSearchPDFView, UserSearchView
)

urlpatterns = [
    url(r'^$', UserListView.as_view(), name='list'),
    url(r'^search/$', UserSearchView.as_view(), name='search'),
    url(r'^search/pdf/$', UserSearchPDFView.as_view(), name='search-pdf'),
    url(r'^me/$', UpdateProfileView.as_view(), name='profile-edit'),
    url(r'^(?P<pk>\d+)/$', UserProfileView.as_view(), name='profile'),

    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]
