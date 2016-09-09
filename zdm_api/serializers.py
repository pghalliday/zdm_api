from django.contrib.auth.models import User
from rest_framework import serializers

from .models import (
    Package,
    Version,
    Dependency,
)


class UserSerializer(serializers.ModelSerializer):
    packages = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Package.objects.all(),
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'packages']


class PackageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Package
        fields = ['id', 'name', 'owner', 'created', 'modified']


class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = ['id', 'created', 'modified']


class DependencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependency
        fields = ['id', 'created', 'modified']
