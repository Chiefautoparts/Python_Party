# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from .models import Product

def index(request):
    product = Product.objects.create(name='potato', description='object like thing for activities', weight='3', price='14', cost='2', category='item')
    products = Product.objects.all()
    for product in products:
        print product.name, product.description, product.weight, product.price, product.cost, product.category

    return render(request, 'product_app/index.html' )
