from urllib.parse import urlencode

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin, UpdateView

from langerak_gkv.utils.view_mixins import LoginRequiredMixin

from .forms import LoginForm, ProfileUpdateForm, UserSearchForm
from .models import User


class UserSearchMixin(FormMixin):
    form = None
    form_context_name = "form"
    initial = {"sex": None}

    def get_search_form(self):
        form = super(UserSearchMixin, self).get_form(UserSearchForm)
        form.data = self.request.GET
        form.is_bound = True
        return form

    def get_context_data(self, **kwargs):
        search_form = self.form or self.get_search_form()
        kwargs[self.form_context_name] = search_form
        kwargs["search_form_qs"] = urlencode(search_form.data)
        return super(UserSearchMixin, self).get_context_data(**kwargs)


class UserListView(LoginRequiredMixin, UserSearchMixin, ListView):
    queryset = User.objects.only_real()
    context_object_name = "profiles"
    paginate_by = 15


class UserSearchView(UserListView):
    """ Same as usual list view, except that it deals with the search form """

    def get_queryset(self):
        qs = super(UserSearchView, self).get_queryset()
        if not self.form.is_valid():
            return qs
        return qs.filter(self.form.as_filters())

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        if not self.form.is_valid():
            self.object_list = self.get_queryset().none()
            return self.form_invalid(self.form)
        return super(UserSearchView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


class UserProfileView(LoginRequiredMixin, UserSearchMixin, DetailView):
    queryset = User.objects.only_real()
    context_object_name = "profile"


class UpdateProfileView(LoginRequiredMixin, UserSearchMixin, UpdateView):
    queryset = User.objects.only_real()
    form_class = ProfileUpdateForm
    form_context_name = "search_form"

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super(UpdateProfileView, self).get_context_data(**kwargs)
        context["profile"] = self.object
        return context


class LoginView(LoginView):
    template_name = "users/login.html"
    form_class = LoginForm


class LogoutView(LogoutView):
    template_name = "users/logout.html"
