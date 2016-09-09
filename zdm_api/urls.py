# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(
        regex="^users/$",
        view=views.UserList.as_view(),
        name='user_list',
    ),
    url(
        regex="^users/(?P<pk>\d+)/$",
        view=views.UserDetail.as_view(),
        name='user_detail',
    ),
    url(
        regex="^packages/$",
        view=views.PackageList.as_view(),
        name='package_list',
    ),
    url(
        regex="^packages/(?P<pk>\d+)/$",
        view=views.PackageDetail.as_view(),
        name='package_detail',
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(
        regex="^auth/",
        view=include(
            'rest_framework.urls',
            namespace='rest_framework',
        ),
        name='auth',
    ),
]
