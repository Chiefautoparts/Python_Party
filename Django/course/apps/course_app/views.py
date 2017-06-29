# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
	#print '***********WORKING************'
	return render(request, 'course_app/index.html')

def create(request):
	