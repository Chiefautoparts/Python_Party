
def play():

	from random import randint
	
	c = ['rock', 'paper', 'scissors']
	
	comp = c[randint(0,2)]
	
	win = 0
	lose = 0
	tie = 0
	if comp == "rock":
		print 'you tie'
		tie += 1
		print tie
	elif comp == 'paper':
		print 'you lose'
		lose += 1
		print lose
	else:
		print 'you win!!'
		win += 1
		print win
print play()