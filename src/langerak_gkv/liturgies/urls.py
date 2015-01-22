from django.conf.urls import patterns, url

from .views import liturgy_list, liturgy_detail

urlpatterns = patterns(
    '',
    url(r'^$', liturgy_list, name='list'),
    url(r'^list/$', liturgy_list, name='list2'),
    url(r'^(?P<liturgy_id>\d+)/$', liturgy_detail, name='detail'),
)
