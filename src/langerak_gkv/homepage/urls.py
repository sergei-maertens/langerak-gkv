from django.conf.urls import url

from .views import PODCreateView

urlpatterns = [url(r"^prayer-on-demand/$", PODCreateView.as_view(), name="pod")]
