from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from langerak_gkv.users.password_reset_urls import urlpatterns as password_urlpatterns

urlpatterns = [
    path("api/v1/", include("langerak_gkv.api.urls")),
    path("admin/rosetta/", include("rosetta.urls")),
    path("admin/", admin.site.urls),
    path("societies/", include("langerak_gkv.societies.urls")),
    path("password/", include((password_urlpatterns, "user_passwords"))),
] + staticfiles_urlpatterns()


# If settings.DEBUG is set to True, some URLs can be handled by Django.
# Normally, these URLs should be covered by the webserver for optimization.
if settings.DEBUG:
    import debug_toolbar

    # Static files are handled by the staticfiles package. This section only
    # adds media files to be served as well.
    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))] + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

urlpatterns += [path("", include("cms.urls"))]
