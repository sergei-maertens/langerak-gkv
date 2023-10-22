from django.urls import path, re_path
from django.utils.translation import gettext_lazy as _

from .views import (
    LiturgyArchiveView,
    LiturgyDateDetailView,
    LiturgyListView,
    LiturgyMonthArchiveView,
)

app_name = "liturgies"

urlpatterns = [
    path("", LiturgyListView.as_view(), name="list"),
    re_path(_(r"^history/$"), LiturgyArchiveView.as_view(), name="history"),
    re_path(
        r"^(?P<year>\d+)/(?P<month>[-\w]+)/$",
        LiturgyMonthArchiveView.as_view(),
        name="archive_date_month",
    ),
    re_path(
        r"^(?P<year>\d+)/(?P<month>[-\w]+)/(?P<day>\d+)/(?P<pk>\d+)/$",
        LiturgyDateDetailView.as_view(),
        name="archive_date_detail",
    ),
]
