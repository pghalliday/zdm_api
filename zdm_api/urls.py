# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^swagger/$', views.swagger_view, name='swagger'),
    url(r'^coreapi/$', views.coreapi_view, name='coreapi'),
    url(r'^openapi/$', views.openapi_view, name='openapi'),
    url(r'^publish/$', views.PublishView.as_view(), name='publish'),
    url(
        r'^packages/(?P<package_name>[^/]+)/latest/$',
        views.LatestVersionView.as_view(),
        name='latest-version'
    ),
    url(
        r'^packages/(?P<package_name>[^/]+)/(?P<version_name>[^/]+)/$',
        views.VersionView.as_view(),
        name='version'
    ),
    url(
        r'^packages/(?P<package_name>[^/]+)/$',
        views.PackageViewSet.as_view({'get': 'retrieve'}),
        name='package'
    ),
    url(
        r'^packages/$',
        views.PackageViewSet.as_view({'get': 'list'}),
        name='packages'
    ),
    url(r'^$', views.RootView.as_view(), name='root'),
]
