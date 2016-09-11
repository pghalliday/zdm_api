# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework_extensions.routers import ExtendedDefaultRouter

from . import views

router = ExtendedDefaultRouter()
router.register(r'users',
                views.UserViewSet,
                base_name='user',
                ) \
      .register(r'packages',
                views.PackageViewSet,
                base_name='users-package',
                parents_query_lookups=['package'],
                ) \
      .register(r'versions',
                views.VersionViewSet,
                base_name='users-packages-versions',
                parents_query_lookups=['package', 'version'],
                )

urlpatterns = [
    url(r'^swagger/$', views.swagger_view),
    url(r'^coreapi/$', views.coreapi_view),
    url(r'^openapi/$', views.openapi_view),
]
urlpatterns += router.urls
