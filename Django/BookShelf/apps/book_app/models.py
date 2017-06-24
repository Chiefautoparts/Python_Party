# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Book(models.Model):
	title = models.CharField(max_length=100),
	author = models.CharField(max_length=100),
	published_date = DateTimeField(auto_now_add=False),
	category = CharField(max_length=50),
	created_at = DateTimeField(auto_now_add=True),
	updated_at = DateTimeField(auto_now=True)
# Create your models here.
