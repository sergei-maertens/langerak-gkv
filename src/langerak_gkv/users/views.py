from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin

from class_based_auth_views.views import LoginView, LogoutView

from langerak_gkv.utils.view_mixins import LoginRequiredMixin
from .models import User
from .forms import UserSearchForm, LoginForm


class UserSearchMixin(FormMixin):
    form_class = UserSearchForm
    form = None
    initial = {
        'sex': None
    }

    def get_form(self):
        form_class = self.get_form_class()
        return super(UserSearchMixin, self).get_form(form_class)

    def get_context_data(self, **kwargs):
        kwargs['form'] = self.form or self.get_form()
        return super(UserSearchMixin, self).get_context_data(**kwargs)


class UserListView(LoginRequiredMixin, UserSearchMixin, ListView):
    model = User
    context_object_name = 'profiles'
    paginate_by = 15


class UserSearchView(UserListView):
    """ Same as usual list view, except that it deals with the search form """

    def get_queryset(self):
        qs = super(UserSearchView, self).get_queryset()
        return qs.filter(self.form.as_filters())

    def post(self, request, *args, **kwargs):
        self.form = self.get_form()
        if self.form.is_valid():
            return self.get(request, *args, **kwargs)
        else:
            return self.form_invalid(self.form)


class UserProfileView(LoginRequiredMixin, UserSearchMixin, DetailView):
    model = User
    context_object_name = 'profile'


class LoginView(LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm


class LogoutView(LogoutView):
    template_name = 'users/logout.html'
