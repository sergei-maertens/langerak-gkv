from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic.base import TemplateView


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    # Simply show the master template.
    (r'^$', TemplateView.as_view(template_name='home.html')),
)


# If settings.DEBUG is set to True, some URLs can be handled by Django.
# Normally, these URLs should be covered by the webserver for optimization.
if settings.DEBUG:
    # Static files are handled by the staticfiles package. This section only
    # adds media files to be served as well.
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
   )
