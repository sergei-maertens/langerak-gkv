from django.conf.urls import patterns, url

from .views import HomepageView, PODCreateView

urlpatterns = patterns(
    '',
    url(r'^$', HomepageView.as_view(), name='home'),
    url(r'^prayer-on-demand/$', PODCreateView.as_view(), name='pod'),
)
