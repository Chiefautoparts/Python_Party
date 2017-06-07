for x in range(1, 1000, 2): #set the numbers for where the loop is to start (1) and where it will stop (1000) increasing count by 2
	if(x%2 != 0): #checking that is the number (x) if it is even or odd, even would return 0 if divided by 2 when an odd will not
		print x #if number is odd print said number
for i in range(5,1000001):
	if(i%5 == 0):
		print i
a = [1, 2, 5, 10, 255, 3]
print sum(a) #prints the sum of array a
avg = sum(a) / len(a) #divids the sum of array a by the length of the array
print avg