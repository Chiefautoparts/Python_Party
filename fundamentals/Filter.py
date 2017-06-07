
x = ['name','address','phone number','social security number']
if type(x) == int:
	if x>=100:
		print "That's a big number!"
	elif x<100:
		print "That's a small number"
elif type(x) == str:
	if len(x)>=50:
		print "Long sentence."
	elif len(x)<50:
		print "Short sentence."
elif type(x) == list:
	if len(x)>=10:
		print "Big list!"
	elif len(x)<10:
		print "Short list."
