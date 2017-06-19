# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def index(request):
	return render(request, 'port_app/index.html')

def show(request):
	return render(request, 'port_app/testimonials.html')

# Create your views here.
