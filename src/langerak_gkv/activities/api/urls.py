from django.urls import path

from .views import ActivityListApiView

app_name = "activities"

urlpatterns = [
    path("activity/", ActivityListApiView.as_view(), name="list"),
]
