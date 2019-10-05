from django.urls import path, re_path

from .views import (
    ActivityCalendarView,
    ActivityCreateView,
    ActivityDayArchiveView,
    ActivityDetailView,
    ActivitySearchView,
    ActivityWeekArchiveView,
    Feed,
)

app_name = "activities"

urlpatterns = [
    path("", ActivityCalendarView.as_view(), name="calendar"),
    path("add/", ActivityCreateView.as_view(), name="add"),
    re_path(r"^(?:(?P<pk>\d+)/)?feed.ics$", Feed(), name="ical-feed"),
    path("searchresults/", ActivitySearchView.as_view(), name="search"),
    path("<slug:slug>/", ActivityDetailView.as_view(), name="detail"),
    re_path(
        r"^(?P<year>\d{4})/week/(?P<week>\d+)/$",
        ActivityWeekArchiveView.as_view(),
        name="week-archive",
    ),
    re_path(
        r"^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$",
        ActivityDayArchiveView.as_view(),
        name="day-archive",
    ),
]
