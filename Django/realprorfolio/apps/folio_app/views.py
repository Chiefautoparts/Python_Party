# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def index(request):
	return render(request, 'folio_app/index.html')

def show(request):
 	return render(request, 'folio_app/projects.html')

def about(request):
 	return render(request, 'folio_app/me.html')

def quotes(request):
 	return render(request, 'folio_app/testimonials.html')
	