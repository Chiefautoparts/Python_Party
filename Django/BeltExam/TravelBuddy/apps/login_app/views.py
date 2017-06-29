# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import LoginManager
# Create your views here.\
app_name='login_app'
def index(request):
	print '************LoginIndex*********'
	return render(request, 'login_app/index.html')

def travel(request):
	print '************LoginWORKING***********'
	return render(request, 'travel_app/travel.html')