# -*- coding: utf-8 -*-

from django.db import models
from model_utils.models import TimeStampedModel


class Package(TimeStampedModel):
    name = models.CharField(max_length=100, blank=False)


class Version(TimeStampedModel):
    pass


class Dependency(TimeStampedModel):
    pass
