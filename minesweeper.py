import sys
import random
import AnimationTest


board = []
empty = []

def printNice(twodee):
	for row in range(1, len(twodee)-1):
		for col in range(1, len(twodee[0])-1):
			print(twodee[row][col], end=' ')
		print('')
level = input("Would you like to play on Easy, Medium or Hard?")
if level == 'easy' or level == 'Easy':
	width = int(5)+2
	height = int(5)+2
	mines = int(5)
if level == 'medium' or level == 'Medium':
	width = int(12)+2
	height = int(12)+2
	mines = int(15)
if level == 'hard' or level == 'Hard':
	width = int(30)+2
	height = int(15)+2
	mines = int(50)
	#return width, height, mines
def AnswerBoard():
	global board
	global height
	global width
	global mines

	board = [] #adding blank spaces
	for i in range(height):
		row = ['.']*width
		board.append(row)
	# add mines to the board
	for i in range(mines):
		x = random.randint(1,height-2)
		y = random.randint(1,width-2)
		while board[x][y] == '*':
			x = random.randint(1,height-2)
			y = random.randint(1,width-2)
		board[x][y] = '*'
	for r in range(1, len(board)-1):  #adding neighbor numbers
		for c in range(1, len(board[0])-1):
			if board[r][c] != '*':
				neighbors = 0
				if board[r][c-1] == '*':
					neighbors += 1
				if board[r][c+1] == '*':
					neighbors += 1
				if board[r-1][c] == '*':
					neighbors += 1
				if board[r+1][c] == '*':
					neighbors += 1
				if board[r-1][c-1] == '*':
					neighbors += 1
				if board[r+1][c-1] == '*':
					neighbors += 1
				if board[r-1][c+1] == '*':
					neighbors += 1
				if board[r+1][c+1] == '*':
					neighbors += 1
				if neighbors > 0:
					board[r][c] = neighbors
def NewGame():
	global width
	global height
	global mines 

	level = input("Would you like to play on Easy, Medium or Hard?")
	if level == 'easy' or level == 'Easy':
		width = int(5)+2
		height = int(5)+2
		mines = int(5)
	if level == 'medium' or level == 'Medium':
		width = int(12)+2
		height = int(12)+2
		mines = int(15)
	if level == 'hard' or level == 'Hard':
		width = int(30)+2
		height = int(15)+2
		mines = int(50)
def Neighbor(r,c):
	global board
	global empty
	check = []

	if board[r][c-1] == '.':
		empty[r][c-1] = board[r][c-1]
		check.append((r,c-1))
	if board[r][c+1] == '.':
		empty[r][c+1]= board[r][c+1]
		check.append((r,c+1))
	if board[r-1][c] == '.':
		empty[r-1][c]=board[r-1][c]
		check.append((r-1,c))
	if board[r+1][c] == '.':
		empty[r+1][c]= board[r+1][c] 
		check.append((r+1,c))
	if board[r-1][c-1] == '.':
		empty[r-1][c-1]=board[r-1][c-1]
		check.append((r+1,c))
	if board[r+1][c-1] == '.':
		empty[r+1][c-1] = board[r+1][c-1]
		check.append((r+1,c-1))
	if board[r-1][c+1] == '.':
		empty[r-1][c+1] = board[r-1][c+1]
		check.append((r+1,c-1))
	if board[r+1][c+1] == '.':
		empty[r+1][c+1] = board[r+1][c+1]
		check.append((r+1,c-1))
	empty.append([check])

				
def BlankBoard():
	global empty
	global height
	global width 
	empty = []
	for i in range(height):
		row = ['[]']*width
		empty.append(row)
	printNice(empty)
def Guess():
	global board
	global empty

	AnswerBoard()
	BlankBoard()
	while True:
		y = int(input('To Guess, specify column'))
		x = int(input('To Guess, specify row'))
		if board[x][y] == '*':
			AnimationTest.explode()
			AnimationTest.cls()
			print('You hit a bomb.')
			new = input('Play again?')
			if new == 'Yes' or new == 'yes':
				NewGame()
				AnimationTest.cls()
				Guess()
			else:
				sys.exit()
		elif board[x][y] == '.':
			Neighbor(x,y)
			printNice(empty)
		else:
			empty[x][y] = board[x][y]
			AnimationTest.cls()
			printNice(empty)




Guess()


#calculate()
#guess()
#check()






#On our honor, we did not give or receive any unauthorized aid. 

#Matthew Leone, Brain McGlinchey, Faisal Alsaif

#only source was MS. Healey's original board code.






