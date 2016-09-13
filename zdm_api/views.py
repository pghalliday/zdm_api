# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from django.db import transaction
from rest_framework import (
    permissions,
    response,
    schemas,
    viewsets,
    renderers,
    views,
    parsers,
    status,
)
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
import json

from .models import (
    Package,
    Version,
)

from .serializers import (
    PackagesSerializer,
    PackageSerializer,
    VersionSerializer,
)


@api_view()
@renderer_classes([OpenAPIRenderer])
def openapi_view(request):
    generator = schemas.SchemaGenerator(title='Zipped Dependency Manager API')
    return response.Response(generator.get_schema(request=request))


@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
def swagger_view(request):
    generator = schemas.SchemaGenerator(title='Zipped Dependency Manager API')
    return response.Response(generator.get_schema(request=request))


@api_view()
@renderer_classes([renderers.CoreJSONRenderer])
def coreapi_view(request):
    generator = schemas.SchemaGenerator(title='Zipped Dependency Manager API')
    return response.Response(generator.get_schema(request=request))


class PermissionsMixin():
    permission_classes = [
        permissions.IsAuthenticated,
    ]


class PackageViewSet(PermissionsMixin, viewsets.ViewSet):
    def list(self, request):
        queryset = Package.objects.all()
        serializer = PackagesSerializer(queryset, context={'request': request})
        return response.Response(serializer.data)

    def retrieve(self, request, package_name=None):
        queryset = Package.objects.filter(name=package_name)
        package = get_object_or_404(queryset, name=package_name)
        serializer = PackageSerializer(package, context={
            'request': request,
            'package_name': package_name,
        })
        return response.Response(serializer.data)


class LatestVersionView(PermissionsMixin, views.APIView):
    def get(self, request, package_name=None, format=None):
        version_name = get_object_or_404(
            Package,
            name=package_name
        ).latest()
        return response.Response(
            status = status.HTTP_302_FOUND,
            headers = {
                'Location': reverse(
                    'zdm_api:version',
                    request=request, 
                    kwargs={
                        'version_name': version_name,
                        'package_name': package_name,
                    }
                ),
            },
        )


class VersionView(PermissionsMixin, views.APIView):
    def get(self, request, version_name=None, package_name=None, format=None):
        queryset = Version.objects.filter(
            name=version_name,
            parent__name=package_name,
        )
        version = get_object_or_404(queryset, name=version_name)
        serializer = VersionSerializer(version, context={
            'request': request,
        })
        return response.Response(serializer.data)


class RootView(PermissionsMixin, views.APIView):
    def get(self, request, format=None):
        return response.Response({
            'packages': reverse('zdm_api:packages', request=request),
            'swagger': reverse('zdm_api:swagger', request=request),
            'coreapi': reverse('zdm_api:coreapi', request=request),
            'openapi': reverse('zdm_api:openapi', request=request),
            'publish': reverse('zdm_api:publish', request=request),
        })


class PublishView(PermissionsMixin, views.APIView):
    parser_classes = [
        parsers.MultiPartParser,
    ]

    def post(self, request, format=None):
        with transaction.atomic():
            metadata = json.loads(request.data['metadata'])
            readme = request.data['readme']
            archive = request.data['archive']
            package_name = metadata['name']
            version_name = metadata['version']
            dependencies = metadata.get('dependencies', {})
            (package, created) = Package.objects.get_or_create(
                name=package_name
            )
            version = package.versions.create(
                name=version_name,
                readme=readme,
                archive=archive,
            )
            for name, constraint in dependencies.items():
                version.dependencies.create(
                    name=name,
                    constraint=constraint,
                )
            return response.Response('ok')
