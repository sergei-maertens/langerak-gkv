from django.views.generic import DetailView, ListView

from class_based_auth_views.views import LoginView, LogoutView

from langerak_gkv.utils.view_mixins import LoginRequiredMixin
from .models import User
from .forms import UserSearchForm, LoginForm


class UserSearchMixin(object):
    def get_context_data(self, **kwargs):
        kwargs['form'] = UserSearchForm()
        return super(UserSearchMixin, self).get_context_data(**kwargs)


class UserListView(LoginRequiredMixin, UserSearchMixin, ListView):
    model = User
    context_object_name = 'profiles'
    paginate_by = 15


class UserProfileView(LoginRequiredMixin, UserSearchMixin, DetailView):
    model = User
    context_object_name = 'profile'


class LoginView(LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm


class LogoutView(LogoutView):
    template_name = 'users/logout.html'
