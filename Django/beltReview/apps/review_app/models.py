# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import bcrypt
from datetime import datetime
from django.db import models

#Create your models here.
class UserManager(models.Manager):
	def regval(self, postData):
		results = {'status':True, 'errors':[], 'user': None}
		if not postData['name'] or len(postData['name']) < 2:
			results['status'] = False
			results['errors'].append('name is too short')
		if not postData['alias'] or len(postData['alias']) < 2:
			results['status'] = False
			results['errors'].append('alias must be longer than 2 characters')
		if not postData['email'] : #need regex for email
			results['status']=False
			results['errors'].append('email not valid')
		if not postData['password'] or len(postData['password']) < 2:
			results['status']=False
			results['errors'].append('password must be more than 2 characters')
		if not postData['confPassword'] or postData['confPassword']!=postData['password']:
			results['status']=False
			results['errors'].append('passwords do not match')

		if results['status'] == False:
			return results
		user = User.objects.filter(alias=postData['alias'])

		if results['status']:
			user.password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())

class User(models.Model):
	name = models.CharField(max_length=100)
	alias = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=20)
	confPassword = models.CharField(max_length=20)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

	def __str__(self):
		return str(self.id) + ' , ' + self.alias
	objects = UserManager()