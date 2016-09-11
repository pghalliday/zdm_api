# -*- coding: utf-8 -*-

from django.db import models
from model_utils.models import TimeStampedModel


class Package(TimeStampedModel):
    name = models.CharField(max_length=100, blank=False)
    owner = models.ForeignKey('auth.User', related_name='packages')


class Version(TimeStampedModel):
    name = models.CharField(max_length=100, blank=False)
    package = models.ForeignKey('Package', related_name='versions')


class Dependency(TimeStampedModel):
    pass
