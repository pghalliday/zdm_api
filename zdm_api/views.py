# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions

from .models import (
    Package,
)

from .serializers import (
    UserSerializer,
    PackageSerializer,
)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PackageList(generics.ListCreateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PackageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]
