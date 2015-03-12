# coding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'core.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('project.core.urls')),
    url(r'^forum/', include('pybb.urls', namespace='pybb')),
    # url(r'^blog/', include('core.urls')),

)
