# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import permissions, response, schemas, viewsets, renderers
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

from .models import (
    Package,
)

from .serializers import (
    UserSerializer,
    PackageSerializer,
)


@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
def swagger_view(request):
    generator = schemas.SchemaGenerator(title='Zipped Dependency Manager API')
    return response.Response(generator.get_schema(request=request))

@api_view()
@renderer_classes([renderers.CoreJSONRenderer])
def coreapi_view(request):
    generator = schemas.SchemaGenerator(
	title='Zipped Dependency Manager API',
    )
    return response.Response(generator.get_schema(request=request))

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides 'list' and 'detail' actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PackageViewSet(viewsets.ModelViewSet):
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
