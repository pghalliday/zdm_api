# -*- coding: utf-8 -*-
from django.conf.urls import url

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
