from django.conf.urls import url

from .views import ActivityListApiView

urlpatterns = [
    url(r'^activity/$', ActivityListApiView.as_view(), name='list'),
]
