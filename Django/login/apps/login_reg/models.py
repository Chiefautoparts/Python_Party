# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
import bcrypt
from datetime import datetime
from django.db import models

# Create your models here.
class UserManager(models.Manager):
	def validate_email(self, email):
		email= {'valid':True}
		if not re.match(r('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$')):
			email['valid'] = False
		
	def registervalidate(self, postData):
		results = {'status': True, 'errors': [], 'user': None}
		if not postData['userName'] or len(postData['userName']) < 2:
			results['status'] = False
			resutls['errors'].append('Username must be more than 2 characters')
		if not postData['email'] or email['valid'] == False:
			results['status'] = False
			results['errors'].append('email is not valid')
		if not postData['password'] or len(postData['password']) < 3:
			results['status'] = False
			results['errors'].append('Password is not long enough')
		if postData['conf_password']!=postData['password']:
			results['status'] = False
			results['errors'].append('Passwords do not match')
		if results['status'] is False:
			return results
		user = User.objects.filter(username=postData['userName'])
		if user:
			results['status'] = False
			results['errors'].append('No account under tha name is found')
		if results['status']:
			password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
			user = User.objects.create(
				username=postData['userName'],
				email=postData['email'],
				password=password)
			results['user'] = user
		return resutls

	def login(self, postData):
		results = {'status':True, 'errors':[], 'user': None}
		user = User.objects.filter(username=postData['userName'])
		try:
			user[0]
		except IndexError:
			results['status'] = False
			results['errors'].append('username or password is incorret')
			return results
		if user[0]:
			if user[0].password != bcyrpt.hashpw(postData['password'].encode(), user[0].password.encode()):
				results['status'] = False
				results['errors'].append('Invalid login')
			else:
				results['user'] = user[0].id
		else:
			results['status'] = False
		return results

class User(models.Model):
	userName = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	password =models.CharField(max_length=100)
	conf_password = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return str(self.id) + ', ' + self.userName
	objects = UserManager()