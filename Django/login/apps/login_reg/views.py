# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
# Create your views here.
def index(request):
	#print '*********TEST******'
	return render(request, 'login_reg/index.html')

def register(request):
	results = User.objects.reg(request.POST)
	print "***UserResult, back in views ***", results['status']
	if not results['status']: 
		for error in results['errors']:
			messages.error(request, error)
			return redirect('login_reg/index.html')
	request.session['id']=results['user'].id 
	return redirect('login_reg/main.html')

def login(request):
	results = User.objects.login(request.POST)
	if results['status'] is False:
		for error in results['errors']:
			messages.error(request, error)
			return redirect('login_reg/index.html')
	else:
		user = User.Objects.get(id=results['user'])
		request.session['id']=user.id 
	return redirect('login_reg/main.html')