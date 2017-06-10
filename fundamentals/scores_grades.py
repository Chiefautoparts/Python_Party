import random

def grades():
	print 'Scores and Grades'
	for a in xrange(10):
		score = random.randint(60,100)
		if score <= 69:
			print 'Score: ' + str(score) + '; Your grade is D'
		elif score  <= 79:
			print 'Score: ' + str(score) + '; Your grade is C'
		elif score <= 89:
			print 'Score: ' + str(score) + '; Your grade is B'
		else:
			print 'Score: ' + str(score) + '; Your grade is A'
	print 'End of the program. Bye!'

grades()