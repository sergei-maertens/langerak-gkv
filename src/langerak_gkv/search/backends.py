from django.conf import settings
from haystack.backends.elasticsearch_backend import ElasticsearchSearchEngine, ElasticsearchSearchBackend


class ConfigurableElasticBackend(ElasticsearchSearchBackend):
    """
    Allows you to tweak the ElasticSearch backend settings.

    DEFAULT_SETINGS = {
        u'settings': {
            u'analysis': {
                u'filter': {
                    u'haystack_edgengram': {
                        u'max_gram': 15,
                        u'type': u'edgeNGram',
                        u'min_gram': 2
                    },
                    u'haystack_ngram': {
                        u'max_gram': 15,
                        u'type': u'nGram',
                        u'min_gram': 3
                    }
                },
                u'tokenizer': {
                    u'haystack_ngram_tokenizer': {
                        u'max_gram': 15,
                        u'type': u'nGram',
                        u'min_gram': 3
                    },
                    u'haystack_edgengram_tokenizer': {
                        u'max_gram': 15,
                        u'type': u'edgeNGram',
                        u'side': u'front',
                        u'min_gram': 2
                    }
                },
                u'analyzer': {
                    u'edgengram_analyzer': {
                        u'filter': [u'haystack_edgengram'],
                        u'type': u'custom',
                        u'tokenizer': u'lowercase'
                    },
                    u'ngram_analyzer': {
                        u'filter': [u'haystack_ngram'],
                        u'type': u'custom',
                        u'tokenizer': u'lowercase'
                    }
                }
            }
        }
    }
    """
    def __init__(self, connection_alias, **connection_options):
        super(ConfigurableElasticBackend, self).__init__(
                                connection_alias, **connection_options)
        user_settings = getattr(settings, 'ELASTICSEARCH_INDEX_SETTINGS', None)
        if user_settings is not None:
            setattr(self, 'DEFAULT_SETTINGS', user_settings)

    def build_search_kwargs(self, query_string, **kwargs):
        """
        Allows you to tweak the search query passed to ElasticSearch.

        :param query_string:
        :param kwargs:
        :return:
        """
        search_kwargs = super(ConfigurableElasticBackend, self).build_search_kwargs(query_string, **kwargs)
        search_kwargs.update({
            # 'minimum_should_match': '80%',
        })

        # When executing a query always ensure the analyzer is 'snowball'. Otherwise
        # 'edgengram_analyzer' seems to be used, which incorrectly splits up the words in our
        # query leading to odd & too many matches
        try:
            search_kwargs['query']['filtered']['query']['query_string']['analyzer'] = 'default'
        except KeyError:
            pass
        return search_kwargs


class ConfigurableElasticSearchEngine(ElasticsearchSearchEngine):
    backend = ConfigurableElasticBackend
