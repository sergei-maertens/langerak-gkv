from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
    url(r'^activities/', include('langerak_gkv.activities.api.urls', namespace='activities')),
)
