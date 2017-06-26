# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from .models import User
# Create your views here.
def index(request):
    return render(request, 'app_one/index.html')
def new(request):

    if User.name > 26:
        return render('Username too long')
    elif user_namever
     < 6:
        return render('Username too short')
    else:
        return render('good job bud')
