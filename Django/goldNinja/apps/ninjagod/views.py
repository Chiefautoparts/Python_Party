# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
	try:
		request.session['gold']
	except:
		request.session['gold'] = 0
	
	try: 
		request.session['messages']
	except: 
		request.session['messages'] = []
	return render(request, 'ninjagod/index.html')

def farm(request):
	request.session['gold'] += 10
	request.session['messages'].append('win')
	return redirect('/')