from django.views.generic import DetailView

from langerak_gkv.utils.view_mixins import LoginRequiredMixin
from .models import User


class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    context_object_name = 'user'
