x = ['magical','unicorns']

if(all(isinstance(x, int) for i in x)) == True:
  print "The array entered is of integer type"
  print sum(list)
elif(all(isinstance(x, str) for i in x)) == True:
  print "The array entered is of string type"
  print list.join(str(x)for i in x)
else:
  print "The array entered is of mixed type"
