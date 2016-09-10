# -*- coding: utf-8 -*-
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns =  format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^swagger/$', views.schema_view),
    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>\d+)/$',
        views.UserDetail.as_view(),
        name='user-detail'),
    url(r'^packages/$',
        views.PackageList.as_view(),
        name='package-list'),
    url(r'^packages/(?P<pk>\d+)/$',
        views.PackageDetail.as_view(),
        name='package-detail'),
])
