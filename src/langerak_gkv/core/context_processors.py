from typing import Any, Dict

from django.http import HttpRequest

from cms.models import Page

from langerak_gkv.activities.models import Activity


def globals(request: HttpRequest) -> Dict[str, Any]:
    current_page = request.current_page
    if not current_page:
        home_context = {}
    else:
        home = Page.objects.get_home()
        home_context = {
            "home_url": home.get_absolute_url(),
            "home_title": home.get_title(),
            "is_homepage": current_page.is_home,
        }

    qs = Activity.objects.upcoming(n=3).select_related("liturgy", "liturgy__service")
    return {"upcoming_activities": qs, **home_context}
