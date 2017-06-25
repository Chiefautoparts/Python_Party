# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# name, description, weight, price, cost (to seller), and category
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    weight = models.IntegerField()
    price = models.IntegerField()
    cost = models.IntegerField()
    category = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
