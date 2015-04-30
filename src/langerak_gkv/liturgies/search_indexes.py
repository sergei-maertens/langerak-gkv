from haystack import indexes

from .models import Liturgy


class LiturgyIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)

    def get_model(self):
        return Liturgy

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
