from django.conf.urls import patterns, url

from .views import ActivityCalendarView, ActivityDetailView, ActivityWeekArchiveView


urlpatterns = patterns(
    '',
    url(r'^$', ActivityCalendarView.as_view(), name='calendar'),
    url(r'^(?P<slug>[\w\-_]+)/$', ActivityDetailView.as_view(), name='detail'),
    url(r'^(?P<year>\d{4})/week/(?P<week>\d+)/$', ActivityWeekArchiveView.as_view(), name='week-archive'),
)
