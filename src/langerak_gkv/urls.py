from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^api/v1/', include('langerak_gkv.api.urls', namespace='api')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^activities/', include('langerak_gkv.activities.urls', namespace='activities')),
    url(r'^liturgies/', include('langerak_gkv.liturgies.urls', namespace='liturgies')),
    url(r'^users/', include('langerak_gkv.users.urls', namespace='users')),
    url(r'^', include('langerak_gkv.homepage.urls')),

    url(r'^', include('cms.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# If settings.DEBUG is set to True, some URLs can be handled by Django.
# Normally, these URLs should be covered by the webserver for optimization.
if settings.DEBUG:
    # Static files are handled by the staticfiles package. This section only
    # adds media files to be served as well.
    urlpatterns += patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
