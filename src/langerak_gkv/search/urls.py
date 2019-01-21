from django.conf.urls import patterns, url

from haystack.forms import SearchForm
from haystack.query import SearchQuerySet
from haystack.views import SearchView

sqs = SearchQuerySet()


urlpatterns = patterns(
    '',
    url(r'^$', SearchView(form_class=SearchForm, searchqueryset=sqs,
                          template='search/results.html'), name='search'),
)
