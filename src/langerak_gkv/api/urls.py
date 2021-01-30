from django.urls import include, path

app_name = "api"

urlpatterns = [path("activities/", include("langerak_gkv.activities.api.urls"))]
