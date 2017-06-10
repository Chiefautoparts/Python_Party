import random
def tossCoins():
	
	heads = 0
	tails = 0
	counter = 0
	for x in range(1,5001):
		flip = random.randint(1,2)
		if flip == 1:
			heads+=1
			counter+=1
			print "Attempt # " + str(counter) + " Throwing a coin... It's a head! ...Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"
		else:
			tails+=1
			counter+=1
			print "Attempt # " + str(counter) + " Throwing a coin... It's a tail! ...Got " + str(heads) + ' head(s) so far and ' + str(tails) + ' tail(s) so far'
	print 'Ending the program, thank you!'

tossCoins()