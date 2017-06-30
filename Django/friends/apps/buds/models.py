# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class FriendManager(models.Manager):
    def add(self, postData):
        results = {'status': True, 'errors': []}
        if not postData['name'] or len(postData['name']) < 3:
            results['status']= False
            results['errors'].append('Name is not valid')
        if not postData['age'] or len(postData['age']) < 1:
            results['status']= False
            results['errors'].append('Age is not valid')
        if results['status']:
            friend = Friend.objects.create(name=postData['name'], age=postData['age'])
            friend.save()
# Create your models here.
class Friend(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = FriendManager()
