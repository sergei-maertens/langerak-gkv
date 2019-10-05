from django.conf.urls import url

from .views import ActivityListApiView

app_name = "activities"

urlpatterns = [
    url(r'^activity/$', ActivityListApiView.as_view(), name='list'),
]
