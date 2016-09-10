# -*- coding: utf-8 -*-
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^$', views.schema_view),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>\d+)/$', views.UserDetail.as_view()),
    url(r'^packages/$', views.PackageList.as_view()),
    url(r'^packages/(?P<pk>\d+)/$', views.PackageDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
