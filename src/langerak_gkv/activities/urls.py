from django.conf.urls import url

from .views import (
    ActivityCalendarView, ActivityCreateView, ActivityDetailView,
    ActivityWeekArchiveView, ActivityDayArchiveView, ActivitySearchView, Feed
)


urlpatterns = [
    url(r'^$', ActivityCalendarView.as_view(), name='calendar'),
    url(r'^add/$', ActivityCreateView.as_view(), name='add'),
    url(r'^(?:(?P<pk>\d+)/)?feed.ics$', Feed(), name='ical-feed'),
    url(r'^searchresults/$', ActivitySearchView.as_view(), name='search'),
    url(r'^(?P<slug>[\w\-_]+)/$', ActivityDetailView.as_view(), name='detail'),
    url(r'^(?P<year>\d{4})/week/(?P<week>\d+)/$',
        ActivityWeekArchiveView.as_view(), name='week-archive'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$',
        ActivityDayArchiveView.as_view(), name='day-archive'),
]
