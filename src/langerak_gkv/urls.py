from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from surlex.dj import surl

from langerak_gkv.mailing.views import (
    ActionRedirectView, RedirectUnsubscribeRequestView
)

admin.autodiscover()


urlpatterns = [
    path('api/v1/', include('langerak_gkv.api.urls')),
    path('admin/rosetta/', include('rosetta.urls')),
    path('admin/', admin.site.urls),
    path('activities/', include('langerak_gkv.activities.urls')),
    path('liturgies/', include('langerak_gkv.liturgies.urls')),
    path('search/', include('langerak_gkv.search.urls')),
    path('societies/', include('langerak_gkv.societies.urls')),
    path('users/', include('langerak_gkv.users.urls')),
    path('users/password/', include('password_reset.urls')),
    path('', include('langerak_gkv.homepage.urls')),

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
    path('newsletter/', include('newsletter.urls')),

    path('', include('cms.urls')),

] + staticfiles_urlpatterns()


# If settings.DEBUG is set to True, some URLs can be handled by Django.
# Normally, these URLs should be covered by the webserver for optimization.
if settings.DEBUG:
    import debug_toolbar
    # Static files are handled by the staticfiles package. This section only
    # adds media files to be served as well.
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
