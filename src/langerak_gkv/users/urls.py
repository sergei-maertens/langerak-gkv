from django.conf.urls import patterns, url

from .views import UserProfileView


urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\d+)/$', UserProfileView.as_view(), name='profile'),
)
