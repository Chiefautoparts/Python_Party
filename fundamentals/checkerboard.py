a = 12 #height of checkerboard
b = 15 #width of checkerboard
board = []


for rows in range(a):
	board.append([])
	for columns in range(b):
		if(rows%2 == 0):
			board[rows].append('*')
			def make_Board(board):
				for rows in board:
					print " ".join(rows)
		else:
			board[rows].append(' ')
			def make_Board(board):
				for rows in board:
					print "*".join(rows)



print make_Board(board)