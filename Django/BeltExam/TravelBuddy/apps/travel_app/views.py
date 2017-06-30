# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.
def index(request):
	#print '********INDEX?TRAVE********'
	return render(request, 'login_app/index.html')

def travel(request):
	#print '************WORKINGTravel***********'
	return render(request, 'travel_app/travels.html')