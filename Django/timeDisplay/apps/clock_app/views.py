# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
import datetime

def index(request):

    return render(request, 'clock_app/index.html')
