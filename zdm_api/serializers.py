# -*- coding: utf-8 -*-
from rest_framework import serializers
from rest_framework.reverse import reverse
from functools import reduce
from collections import OrderedDict

from .models import (
    Package,
    Version,
)


def reduce_dependency(dependencies, value):
    dependencies[value['name']] = value['constraint']
    return dependencies


class PackagesSerializer(serializers.Serializer):
    def reduce_package(self, packages, value):
        packages[value['name']] = reverse(
            'zdm_api:package',
            kwargs={
                'package_name': value['name'],
            },
            request=self.context['request'],
        )
        return packages

    def to_representation(self, obj):
        return reduce(self.reduce_package, obj.order_by('name').values(), OrderedDict())


class VersionListingField(serializers.RelatedField):
    def reduce_version(self, versions, value):
        print(value)
        versions[value['name']] = reverse(
            'zdm_api:version',
            kwargs={
                'package_name': self.context['package_name'],
                'version_name': value['name'],
            },
            request=self.context['request'],
        )
        return versions

    def to_representation(self, value):
        return reduce(self.reduce_version, value.order_by('-name').values(), OrderedDict())


class PackageSerializer(serializers.ModelSerializer):
    lookup_field = 'name'
    versions = VersionListingField(
        read_only=True,
    )

    class Meta:
        model = Package
        fields = [
            'pk',
            'name',
            'latest',
            'created',
            'modified',
            'versions',
        ]


class DependencyListingField(serializers.Field):
    def to_representation(self, value):
        return reduce(reduce_dependency, value.order_by('name').values(), OrderedDict())


class VersionSerializer(serializers.ModelSerializer):
    lookup_field = 'name'
    dependencies = DependencyListingField(
        read_only=True,
    )

    class Meta:
        model = Version
        fields = [
            'pk',
            'name',
            'readme',
            'archive',
            'dependencies',
            'created',
            'modified',
        ]
