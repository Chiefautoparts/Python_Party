# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
# Create your views here.
def index(request):
	
	return render(request, 'review_app/index.html')

def reg(request):
	results = User.objects.regval(request.POST)
	if not results['status']:
		for errors in results['errors']:
			messages.error(request, error)
			return redirect('review_app:index')
	return render(request, 'review_app/test.html')

