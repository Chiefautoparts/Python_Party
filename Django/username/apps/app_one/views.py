# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from .models import models
# Create your views here.
def index(request):
    return render(request, 'app_one/index.html')
def new(request):

    if user_name > 26:
        return render('Username too long')
    elif user_name < 6:
        return render('Username too short')
    else:
        return render('good job bud')
