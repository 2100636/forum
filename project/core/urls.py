# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.conf.urls import patterns, url
from project.core.views import PostsListView, PostDetailView, PostFormView

urlpatterns = patterns('',

    url(r'^$', PostsListView.as_view(), name='list'),   #  будет выводиться список постов
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()),   # будет выводиться пост с определенным номером
    url(r'^postform-(?P<pk>\d+)/$', PostFormView.as_view()),  #

)


