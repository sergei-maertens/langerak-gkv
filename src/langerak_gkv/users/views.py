from django.views.generic import DetailView, ListView

from class_based_auth_views.views import LoginView, LogoutView

from langerak_gkv.utils.view_mixins import LoginRequiredMixin
from .models import User
from .forms import UserSearchForm, LoginForm


class UserListView(LoginRequiredMixin, ListView):
    model = User


class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        kwargs['form'] = UserSearchForm()
        return super(UserProfileView, self).get_context_data(**kwargs)


class LoginView(LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm


class LogoutView(LogoutView):
    template_name = 'users/logout.html'
