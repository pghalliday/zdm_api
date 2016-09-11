# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import permissions, response, schemas, viewsets, renderers
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import (
    Package,
    Version,
)

from .serializers import (
    UserSerializer,
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

class UserViewSet(NestedViewSetMixin, viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides 'list' and 'detail' actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PackageViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    """
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class VersionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    """
    queryset = Version.objects.all()
    serializer_class = VersionSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]
