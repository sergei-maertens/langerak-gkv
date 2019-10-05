from django.conf.urls import url

from haystack.forms import SearchForm as _SearchForm
from haystack.query import SearchQuerySet
from haystack.views import SearchView

sqs = SearchQuerySet()


class SearchForm(_SearchForm):
    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields["q"].required = True


urlpatterns = [
    url(
        r"^$",
        SearchView(
            form_class=SearchForm, searchqueryset=sqs, template="search/results.html"
        ),
        name="search",
    )
]
