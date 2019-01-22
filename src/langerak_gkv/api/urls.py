from django.conf.urls import include, url

urlpatterns = [
    url(r'^activities/', include('langerak_gkv.activities.api.urls', namespace='activities')),
]
