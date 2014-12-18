from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^liturgies/', include('langerak_gkv.liturgies.urls', namespace='liturgies')),
    url(r'^users/', include('langerak_gkv.users.urls', namespace='users')),
    url(r'^', include('langerak_gkv.homepage.urls')),

)


# If settings.DEBUG is set to True, some URLs can be handled by Django.
# Normally, these URLs should be covered by the webserver for optimization.
if settings.DEBUG:
    # Static files are handled by the staticfiles package. This section only
    # adds media files to be served as well.
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
   )
