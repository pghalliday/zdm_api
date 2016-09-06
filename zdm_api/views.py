# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
    Package,
    Version,
    Dependency,
)


class PackageCreateView(CreateView):

    model = Package


class PackageDeleteView(DeleteView):

    model = Package


class PackageDetailView(DetailView):

    model = Package


class PackageUpdateView(UpdateView):

    model = Package


class PackageListView(ListView):

    model = Package


class VersionCreateView(CreateView):

    model = Version


class VersionDeleteView(DeleteView):

    model = Version


class VersionDetailView(DetailView):

    model = Version


class VersionUpdateView(UpdateView):

    model = Version


class VersionListView(ListView):

    model = Version


class DependencyCreateView(CreateView):

    model = Dependency


class DependencyDeleteView(DeleteView):

    model = Dependency


class DependencyDetailView(DetailView):

    model = Dependency


class DependencyUpdateView(UpdateView):

    model = Dependency


class DependencyListView(ListView):

    model = Dependency
