from django.conf.urls import url

from .views import HomepageView, PODCreateView

urlpatterns = [
    url(r'^$', HomepageView.as_view(), name='home'),
    url(r'^prayer-on-demand/$', PODCreateView.as_view(), name='pod'),
]
