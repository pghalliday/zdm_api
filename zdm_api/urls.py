# -*- coding: utf-8 -*-
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(
        regex="^packages/$",
        view=views.package_list,
        name='package_list',
    ),
    url(
        regex="^packages/(?P<pk>\d+)/$",
        view=views.package_detail,
        name='package_detail',
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
