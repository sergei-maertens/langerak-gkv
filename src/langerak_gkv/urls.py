from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from surlex.dj import surl

from langerak_gkv.mailing.views import ActionRedirectView, RedirectUnsubscribeRequestView


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^api/v1/', include('langerak_gkv.api.urls', namespace='api')),
    url(r'^admin/rosetta/', include('rosetta.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^activities/', include('langerak_gkv.activities.urls', namespace='activities')),
    url(r'^liturgies/', include('langerak_gkv.liturgies.urls', namespace='liturgies')),
    url(r'^search/', include('langerak_gkv.search.urls', namespace='search')),
    url(r'^societies/', include('langerak_gkv.societies.urls', namespace='societies')),
    url(r'^users/', include('langerak_gkv.users.urls', namespace='users')),
    url(r'^users/password/', include('password_reset.urls')),
    url(r'^', include('langerak_gkv.homepage.urls')),

    # newsletter + hijack some urls
    surl(
        '^newsletter/<newsletter_slug:s>/<action=subscribe|update|unsubscribe>/'
        'activation-completed/$',
        ActionRedirectView.as_view(),
        name='newsletter_action_activated'),
    surl(
        '^newsletter/<newsletter_slug:s>/unsubscribe/confirm/$',
        RedirectUnsubscribeRequestView.as_view(confirm=True),
        name='newsletter_unsubscribe_confirm'
    ),
    url(r'^newsletter/', include('newsletter.urls')),

    url(r'^', include('cms.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# If settings.DEBUG is set to True, some URLs can be handled by Django.
# Normally, these URLs should be covered by the webserver for optimization.
if settings.DEBUG:
    import debug_toolbar
    # Static files are handled by the staticfiles package. This section only
    # adds media files to be served as well.
    urlpatterns += patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
