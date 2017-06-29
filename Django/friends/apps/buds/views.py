# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import Friend
from django.contrib import messages
# Create your views here.
def index(request):
    # print 'kfjjs;lfgjfsd;lkjg'
    return render(request, 'buds/index.html')
def create(request):
    return render(request, 'buds/create.html')
def add(request):
    results = Friend.objects.add(request.POST)
    if results['status'] == False:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/create')
    print messages.success(request, 'you have a friend')
    return redirect('/')
