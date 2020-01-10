from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

urlpatterns = [
    path("api/v1/", include("langerak_gkv.api.urls")),
    path("admin/rosetta/", include("rosetta.urls")),
    path("admin/", admin.site.urls),
    path("search/", include("langerak_gkv.search.urls")),
    path("societies/", include("langerak_gkv.societies.urls")),
    path("", include("langerak_gkv.homepage.urls")),
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
