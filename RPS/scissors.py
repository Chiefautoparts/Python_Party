user = input('scissors')
win = 0
lose = 0
tie = 0

from random import randint

c = ['rock', 'paper', 'scissors']

comp = c[randint(0,2)]

print comp

if comp == rock:
	print 'you win'
	win++
elif comp == paper:
	print 'you lose'
	lose++
else:
	print 'you tie!!'
	tie++