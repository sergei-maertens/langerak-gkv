from django.conf.urls import include, patterns, url

urlpatterns = patterns(
    '',
    url(r'^activities/', include('langerak_gkv.activities.api.urls', namespace='activities')),
)
