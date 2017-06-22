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

	if name == 'farm':
		request.session['Moneys'] += randint(10,20)
		return render(request, 'gold_app/index.html')
	elif name == 'cave':
		request.session['Moneys'] += randint(10,30)
		return render(request, 'gold_app/index.html')
	elif name == 'casino':
		x = randint(0,1):
		if x == 0:
			request.session['Moneys'] -= randint(0,50)
			return render(request, 'gold_app/index.html')
		elif:
			request.session['Moneys'] += randint(0,50)
			return render(request, 'gold_app/index.html')
	else name == 'house':
		request.session['Moneys'] += randint(0,30)
		return render(request, 'gold_app/index.html')
