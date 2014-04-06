from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import TaskList, TaskDetail

urlpatterns = patterns(
        'api.views',
        url(r'^tasks/$', TaskList.as_view(), name='task_list'),
        url(r'^tasks/(?P<pk>[0-9]+)$', TaskDetail.as_view(), name='task_detail'),
        )

urlpatterns = format_suffix_patterns(urlpatterns)
