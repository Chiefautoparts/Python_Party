# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Product
from django.shortcuts import render, HttpResponse

def index(request):
	context = {
		'products': Product.objects.all()
	}
        return render(request, 'prod_app/index.html', context)

def create_product(request):
	return request.method
	return render(request, 'prod_app/index.html')