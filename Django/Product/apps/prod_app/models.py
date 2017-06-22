# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
def prod_app(models.Model):
    name = models.Charfield(max_length=50),
    description = models.TextField(),
    weight = models.IntegerField(),
    price = models.IntegerField(),
    cost = models.IntegerField(),
    category = models.CharField(max_length=50),
    created_at = models.DateTimeField(auto_now_add=True),
    updated_at = models.DateTimeField(auto_now=True)
