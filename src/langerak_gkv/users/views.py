from django.views.generic import DetailView

from langerak_gkv.utils.view_mixins import LoginRequiredMixin
from .models import User
from .forms import UserSearchForm


class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        kwargs['form'] = UserSearchForm()
        return super(UserProfileView, self).get_context_data(**kwargs)
