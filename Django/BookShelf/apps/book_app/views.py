# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
	return render(request, 'book_app/index.html')
# Create your views here.
def create(request):
	if request.method == 'POST':
		print (request.POST)
	else: 
		return redirect('/')