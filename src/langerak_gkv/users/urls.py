from django.conf.urls import patterns, url

from .views import (UserProfileView, UserListView, LoginView, LogoutView,
                    UserSearchView)


urlpatterns = patterns(
    '',
    url(r'^$', UserListView.as_view(), name='list'),
    url(r'^search/$', UserSearchView.as_view(), name='search'),
    url(r'^(?P<pk>\d+)/$', UserProfileView.as_view(), name='profile'),

    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
)
