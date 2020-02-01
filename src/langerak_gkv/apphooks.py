from django.conf import settings

from cms.api import create_page
from cms.models import Page


def ensure_apphook_installed(apphook_cls, title: str = "") -> None:
    apphook_name = apphook_cls.__name__

    apphook_pages = Page.objects.filter(
        application_urls=apphook_name, application_namespace=apphook_cls.app_name
    )

    if not apphook_pages.exists():
        home = Page.objects.get_home()
        create_page(
            title=title or apphook_cls.name,
            template=settings.CMS_TEMPLATES[0][0],
            language="nl",
            parent=home,
            apphook=apphook_cls,
            apphook_namespace=apphook_cls.app_name,
            published=True,
        )
