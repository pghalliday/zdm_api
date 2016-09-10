# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import generics, permissions, response, schemas
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
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Zipped Dependency Manager API')
    return response.Response(generator.get_schema(request=request))

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('zdm_api:user-list', request=request, format=format),
        'packages': reverse('zdm_api:package-list', request=request, format=format)
    })

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
