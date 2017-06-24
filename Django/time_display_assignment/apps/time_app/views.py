# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render, HttpResponse
# import datetime

# # Create your views here.
# def index(request):
# 	return render(request, 'time_app/index.html')
	


from django.shortcuts import render, HttpResponse
def index(request):
  context = {
  "time":"H:i"
  }
  return render(request,'time_app/index.html', context)


	# time = {
	# 'datetime':'datetime'
	# }
	# return render(request, 'time_app/index.html', time)