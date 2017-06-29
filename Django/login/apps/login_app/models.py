# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class LoginManager(models.Manager):
    def login(self, postData):
        

class Login(models.Model):
    email = models.CharField(max_length=125)
    password = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class Register(models.Model):
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    email = models.CharField(max_length=125)
    password = models.CharField(max_length=25)
    confirm_password = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
