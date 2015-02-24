from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _

from .views import LiturgyListView, LiturgyDetailView


urlpatterns = patterns(
    '',
    url(r'^$', LiturgyListView.as_view(), name='list'),
    url(_(r'^history/$'), LiturgyListView.as_view(), name='history'),
    url(r'^(?P<pk>\d+)/$', LiturgyDetailView.as_view(), name='detail'),
)
