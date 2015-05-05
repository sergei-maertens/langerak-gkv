from django.conf.urls import url, patterns

from .views import SocietyDetailView


urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\d+)/$', SocietyDetailView.as_view(), name='detail'),
)
