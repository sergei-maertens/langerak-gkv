from django.conf.urls import patterns, url

from .views import ActivityCalendarView


urlpatterns = patterns(
    '',
    url(r'^$', ActivityCalendarView.as_view(), name='calendar')
)
