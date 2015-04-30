from haystack import indexes

from .models import Activity


class ActivityIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.NgramField(document=True, use_template=True)

    def get_model(self):
        return Activity

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
