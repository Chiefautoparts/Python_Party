# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
	try:
		request.session['Moneys']
	except:
		request.session['Moneys'] = 0

	try:
		request.session['Messages']
	except:
		request.session['Messages'] = []

	if 	
	return render(request, 'gold_app/index.html')
