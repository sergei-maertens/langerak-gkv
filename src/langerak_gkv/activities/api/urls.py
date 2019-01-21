from django.conf.urls import patterns, url

from .views import ActivityListApiView

urlpatterns = patterns(
    '',
    url(r'^activity/$', ActivityListApiView.as_view(), name='list'),
)
