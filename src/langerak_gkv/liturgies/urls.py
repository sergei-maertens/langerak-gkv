from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _

from .views import liturgy_list, liturgy_detail

urlpatterns = patterns(
    '',
    url(r'^$', liturgy_list, name='list'),
    url(_(r'^history/$'), liturgy_list, name='history'),
    url(r'^(?P<liturgy_id>\d+)/$', liturgy_detail, name='detail'),
)
