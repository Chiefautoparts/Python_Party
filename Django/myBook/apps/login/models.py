# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import bcrypt
from datetime import datetime
from django.db import models

# Create your models here.

class UserManager(models.Manager):
	def add(self, postData):
        errors = []
        if not postData['fname'] or len(postData['fname']) < 3:
            errors.append('Name is not valid')
        if not postData['lname'] or len(postData['lname']) < 1:
			errors.append('name is not valid')
         if not postData['email'] or len(postData['email']) < 3:
         	errors.append('Fake Email')
         if not postData['username'] or len(postData['username']) < 3:
         	errors.append('Lies and slander')
         if not postData['password'] or len(postData['password']) < 2:
         	errors.append('make a real password')
         if not postData['confPassword'] != postData['password']:
         	errors.append('passwords do not match')
         if not postData['dob'] < 13:
         	errors.append('too young go to disney.com')
        if len(errors[]) == 0:
        	user = User.objects.create(fname=postData['fname'], lname=postData['lname'], email=postData['email'], password=postData['password'], confPassword=postData['confPassword'], dob=postData['dob'])
        	user.save()


class User(models.Model):
	fname = models.CharField(max_length=100)
	lname = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	confPassword = models.CharField(max_length=100)
	dob = models.DateField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)




# bcrypt
#