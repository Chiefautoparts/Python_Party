a = 12 #height of checkerboard
b = 15 #width of checkerboard
sweater = []


for rows in range(a):
	sweater.append([])
	for columns in range(b):
		if(rows%2 == 0):
			sweater[rows].append('*')
			def make_Board(sweater):
				for rows in sweater:
					print " ".join(rows)
		else:
			sweater[rows].append(' ')
			def make_Board(sweater):
				for rows in sweater:
					print "*".join(rows)



print make_Board(sweater)