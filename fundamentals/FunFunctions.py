
'''def odd_even(a,b,c):
	for c in range(a,b):
		if(c%2 == 0):
			print "Number is " + str(c) + "." + " This is an even number."
		else:
			print "Number is " + str(c) + "." + " This is an odd number."
odd_even(1,2000,1)'''

def multipy(a): 
	for x in range(a):
		b = x * 5
		# b = multipy(a)
		print b

multipy([2,4,10,16])