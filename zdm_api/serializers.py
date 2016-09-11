# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import (
    Package,
    Version,
)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    packages = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='zdm_api:users-package-detail',
        read_only=True,
    )

    class Meta:
        model = User
        fields = ['url', 'pk', 'username', 'packages']
        extra_kwargs = {
            'url': {'view_name': 'zdm_api:user-detail'},
        }


class PackageSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(
        view_name='zdm_api:user-detail',
        read_only=True,
    )

    class Meta:
        model = Package
        fields = ['url', 'pk', 'name', 'owner', 'created', 'modified']
        extra_kwargs = {
            'url': {'view_name': 'zdm_api:users-package-detail'},
        }


class VersionSerializer(serializers.HyperlinkedModelSerializer):
    package = serializers.HyperlinkedRelatedField(
        view_name='zdm_api:users-package-detail',
        read_only=True,
    )

    class Meta:
        model = Version
        fields = ['url', 'pk', 'name', 'package', 'created', 'modified']
        extra_kwargs = {
            'url': {'view_name': 'zdm_api:users-packages-version-detail'},
        }
