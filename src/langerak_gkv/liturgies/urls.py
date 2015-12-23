from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from .views import LiturgyListView, LiturgyDateDetailView


urlpatterns = [
    url(r'^$', LiturgyListView.as_view(), name='list'),
    url(_(r'^history/$'), LiturgyListView.as_view(), name='history'),
    url(r'^(?P<year>\d+)/(?P<month>[-\w]+)/(?P<day>\d+)/(?P<pk>\d+)/$',
        LiturgyDateDetailView.as_view(), name="archive_date_detail"),
]
