# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'packages', views.PackageViewSet)

urlpatterns = [
    url(r'^swagger/$', views.swagger_view),
    url(r'^coreapi/$', views.coreapi_view),
    url(r'^openapi/$', views.openapi_view),
    url(r'^', include(router.urls)),
]
