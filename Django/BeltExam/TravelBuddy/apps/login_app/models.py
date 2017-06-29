# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import password_validation

# Create your models here.
class LoginManager(models.Manager):
    def register(self, postData):
        errors = []
        if not postData['name'] or len(postData['name']) < 3:
            errors.append('Name is not valid, must be minimum 3 characters')
        if not postData['username'] or len(postData['username']) < 3:
            errors.append('Username is not valid')
        if not postData['password'] or len(postData['password']) < 3:
            errors.append('password field requires minimum 3 characters')
        if not postData['confirm_password'] or postData['confirm_password'] == postData['password']:
            errors.append('your passwords do not match')
        if errors == []:
            return render()
            user = Register.objects.create(name=postData['name'], username=postData['username'], password=postData['password'], confirm_password=postData['confirm_password'])
            user.save()
    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
class Login(models.Model):
    username = models.CharField(max_length=125)
    password = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Register(models.Model):
    name = models.CharField(max_length=75)
    username = models.CharField(max_length=75)
    password = models.CharField(max_length=25)
    confirm_password = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = LoginManager()

class Schedule(models.Model):
    destination = models.CharField(max_length=150)
    description = models.TextField()
    departure_date = DateField()
    arrival_date = DateField()
    user = models.ForeignKey(username, )