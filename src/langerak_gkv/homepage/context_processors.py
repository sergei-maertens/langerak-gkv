from langerak_gkv.activities.models import Activity
from .forms import PrayerOnDemandForm


def sidebar(request):
    return {
        'upcoming_activities': Activity.objects.upcoming(n=5),
        'pod_form': PrayerOnDemandForm(request=request),
        'preacher': 'ds H.J. Lopers',
    }
