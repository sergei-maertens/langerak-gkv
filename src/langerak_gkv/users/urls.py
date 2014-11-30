from django.conf.urls import patterns, url

from .views import UserProfileView, LoginView, LogoutView


urlpatterns = patterns(
    '',
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^(?P<pk>\d+)/$', UserProfileView.as_view(), name='profile'),
)
