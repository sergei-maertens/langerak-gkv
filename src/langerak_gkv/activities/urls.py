from django.conf.urls import patterns, url

from .views import ActivityCalendarView, ActivityDetailView


urlpatterns = patterns(
    '',
    url(r'^$', ActivityCalendarView.as_view(), name='calendar'),
    url(r'^(?P<slug>[\w\-_]+)/$', ActivityDetailView.as_view(), name='detail'),
)
