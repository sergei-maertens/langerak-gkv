from typing import Dict

from langerak_gkv.activities.models import Activity

from .forms import PrayerOnDemandForm


def sidebar(request):
    return {
        "upcoming_activities": Activity.objects.upcoming(n=5),
        "pod_form": PrayerOnDemandForm(request=request),
    }


def home(request) -> Dict[str, str]:
    if not request.current_page:
        return {}
    root = request.current_page.get_root()
    return {
        "home_url": root.get_absolute_url(),
        "home_title": root.get_title(),
        "is_homepage": root == request.current_page,
    }
