from urllib.parse import urlencode

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView

from langerak_gkv.utils.view_mixins import LoginRequiredMixin

from .filters import UserSearchFilter
from .forms import LoginForm, ProfileUpdateForm
from .models import User


class UserSearchMixin:
    search_filter = None
    filter_context_name = "filter"
    initial = {"sex": None}

    def get_search_filter(self):
        f = UserSearchFilter(self.request.GET, queryset=self.queryset.all())
        return f

    def get_context_data(self, **kwargs):
        search_filter = self.search_filter or self.get_search_filter()
        kwargs[self.filter_context_name] = search_filter

        query_data = search_filter.form.data.copy()
        if "page" in query_data:
            del query_data["page"]
        kwargs["search_form_qs"] = urlencode(query_data)

        return super(UserSearchMixin, self).get_context_data(**kwargs)


class UserListView(LoginRequiredMixin, UserSearchMixin, ListView):
    queryset = User.objects.only_real()
    context_object_name = "profiles"
    paginate_by = 15


class UserSearchView(UserListView):
    """Same as usual list view, except that it deals with the search form"""

    def get_queryset(self):
        qs = super(UserSearchView, self).get_queryset()
        if not self.search_filter.form.is_valid():
            return qs
        return self.search_filter.qs

    def get(self, request, *args, **kwargs):
        self.search_filter = self.get_search_filter()
        if not self.search_filter.form.is_valid():
            self.object_list = self.get_queryset().none()
        return super(UserSearchView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


class UserProfileView(LoginRequiredMixin, UserSearchMixin, DetailView):
    queryset = User.objects.only_real()
    context_object_name = "profile"
    filter_context_name = "search_filter"


class UpdateProfileView(LoginRequiredMixin, UserSearchMixin, UpdateView):
    queryset = User.objects.only_real()
    form_class = ProfileUpdateForm
    filter_context_name = "search_filter"

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
