import sys
import random
import AnimationTest

def printNice(twodee):
	for row in range(1, len(twodee)-1):
		for col in range(1, len(twodee[0])-1):
			print(twodee[row][col], end=' ')
		print('')#Don't want to print board


level = input("Would you like to play on Easy, Medium or Hard?")
if level == 'easy':
	width = int(5)+2
	height = int(5)+2
	mines = int(5)
if level == 'medium':
	width = int(12)+2
	height = int(12)+2
	mines = int(15)
if level == 'hard':
	width = int(30)+2
	height = int(15)+2
	mines = int(50)
	#return width, height, mines

def newboard():
	newboard.board = [] #adding blank spaces
	for i in range(height):
		row = ['.']*width
		newboard.board.append(row)
	# add mines to the newboard.board
	for i in range(mines):
		x = random.randint(1,height-2)
		y = random.randint(1,width-2)
		while newboard.board[x][y] == '*':
			x = random.randint(1,height-2)
			y = random.randint(1,width-2)
		newboard.board[x][y] = '*'
	
	for r in range(1, len(newboard.board)-1):  #adding neighbor numbers
		for c in range(1, len(newboard.board[0])-1):
			if newboard.board[r][c] != '*':
				neighbors = 0
				if newboard.board[r][c-1] == '*':
					neighbors += 1
				if newboard.board[r][c+1] == '*':
					neighbors += 1
				if newboard.board[r-1][c] == '*':
					neighbors += 1
				if newboard.board[r+1][c] == '*':
					neighbors += 1
				if newboard.board[r-1][c-1] == '*':
					neighbors += 1
				if newboard.board[r+1][c-1] == '*':
					neighbors += 1
				if newboard.board[r-1][c+1] == '*':
					neighbors += 1
				if newboard.board[r+1][c+1] == '*':
					neighbors += 1
				if neighbors > 0:
					newboard.board[r][c] = neighbors
	return newboard.board
def Guess():
	board = newboard.board
	x = int(input('To Guess, specify row'))
	y = int(input('To Guess, specify column'))
	turn = board[x][y]
	if board[x][y] == '*':
		AnimationTest.explode()
		sys.exit()
	else:
		Neighbor()
		print(board[r][c])

#def check(): #compare guess to calculate

# print the completed board using my helper function		
printNice(newboard())

while True:
	Guess()


#calculate()
#guess()
#check()














