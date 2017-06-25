# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Book

def index(request):
	context = {
		'books': Book.objects.all()
	}
	Book.objects.create(title='Tom the working Toms Tom', author='Tom Tomson', published='Jan 1, 2016', category='Drama')
	books = Book.objects.all()
	print (books)
	return render(request, 'bookapp/index.html', context)
# Create your views here.
