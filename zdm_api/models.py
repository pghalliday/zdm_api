# -*- coding: utf-8 -*-

from django.db import models
from model_utils.models import TimeStampedModel
from semantic_version.django_fields import VersionField, SpecField
from functools import reduce

def archive_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/archives/<package>-<version>.zip
    return 'archives/{0}-{1}.zip'.format(instance.parent.name, instance.name)

class Package(TimeStampedModel):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    
    def latest(self):
        return self.versions.aggregate(models.Max('name'))['name__max']


class Version(TimeStampedModel):
    parent = models.ForeignKey('Package', related_name='versions', on_delete=models.CASCADE, null=False)
    name = VersionField(blank=False, null=False)
    readme = models.TextField(blank=True, null=False)
    archive = models.FileField(upload_to=archive_path, blank=False, null=False)

    class Meta:
        unique_together = [
            'parent',
            'name',
        ]

class Dependency(TimeStampedModel):
    parent = models.ForeignKey('Version', related_name='dependencies', on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    constraint = SpecField(max_length=100, blank=False, null=False)

    class Meta:
        unique_together = [
            'parent',
            'name',
        ]
