from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin, UpdateView

from class_based_auth_views.views import LoginView, LogoutView

from langerak_gkv.utils.view_mixins import LoginRequiredMixin
from .models import User
from .forms import UserSearchForm, LoginForm, ProfileUpdateForm


class UserSearchMixin(FormMixin):
    form = None
    form_context_name = 'form'
    initial = {
        'sex': None
    }

    def get_search_form(self):
        return super(UserSearchMixin, self).get_form(UserSearchForm)

    def get_context_data(self, **kwargs):
        kwargs[self.form_context_name] = self.form or self.get_search_form()
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
        self.form = self.get_search_form()
        if self.form.is_valid():
            return self.get(request, *args, **kwargs)
        else:
            return self.form_invalid(self.form)


class UserProfileView(LoginRequiredMixin, UserSearchMixin, DetailView):
    model = User
    context_object_name = 'profile'


class UpdateProfileView(LoginRequiredMixin, UserSearchMixin, UpdateView):
    model = User
    form_class = ProfileUpdateForm
    form_context_name = 'search_form'

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super(UpdateProfileView, self).get_context_data(**kwargs)
        context['profile'] = self.object
        return context


class LoginView(LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm


class LogoutView(LogoutView):
    template_name = 'users/logout.html'
