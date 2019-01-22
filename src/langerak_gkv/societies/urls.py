from django.conf.urls import url

from .views import SocietyDetailView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', SocietyDetailView.as_view(), name='detail'),
]
