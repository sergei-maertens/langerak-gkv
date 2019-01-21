from django.conf.urls import patterns, url

from .views import SocietyDetailView

urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\d+)/$', SocietyDetailView.as_view(), name='detail'),
)
