import random

def collectData():
	# balance = int(1000)
	global bet
	global guess
	global output

	bet = ''
	while True:
		try:
			bet = int(input('Place bet: '))
			if bet < 50 or bet >= balance:
				print('Please enter a bet that is between $50 and your balance of $' + str(balance) +'.')
			else:
				break
		except ValueError:
			print('That bet is not an integer. Try again.')

	guess = ''
	while True:
		try:
			guess = int(input('Please guess a number 2-12: '))
			if guess < 2 or guess > 12:
				print('Please guess a number within the specified range of 2-12.')
			else: 
				break
		except ValueError:
			print('That guess is not an integer. Try again.')

	output = ''
	while True:
		output = int((int(random.randrange(1,7))) + (int(random.randrange(1,7))))
		break
def restart():
	global balance
	while True:
		restart = input('Would you like to start a new game (Y/N): ')
		if restart == 'Y':
			balance = int(1000)
			game()
		if restart == 'N':
			print('Goodbye')
		break
def game():
	global guess
	global balance
	global output
	global bet

	while True: 
		collectData()
		print('Your Guess: ' + str(guess))
		print('Dice Output: ' + str(output))
		print('Your Bet: ' + str(bet))
		print('Previous Balance:  ' + str(balance))
		if guess == output:
			balance = balance + bet*(1.5)
			print('Updated Balance: ' + str(balance))
		elif guess > 6 and output >= 6:
			balance = balance + bet
			print('Updated Balance: ' + str(balance))
		elif guess < 6 and output <= 6:
			balance = balance + bet
			print('Updated Balance: ' + str(balance))
		else:
			balance = balance - bet
			print('Updated Balance: '+ str(balance))
		if balance < 50:
			print('Game over. You should probably save your $50 and not be gambling.')
			restart()
			break
		else: 
			game()

name = input('Before we begin, what is your name?: ')
print(name + ', welcome to the dice table at the Choate Casino. You will be given $1,000 to gamble with. Each round, you will guess on the outcome of a pair of randomly rolled dice 2-12. If the outcome of the dice is on the same side of 6 as your bet, you will win the value of your bet. If your bet is on the wrong side of 6, you lose your bet. If your guess happens to be the correct number on the dice, you win your bet and an additional 50 percent. Each bet must be at least $50. You may quit at anytime by saying "End Game", otherwise the game will end once your money runs out. Good Luck!')
bet = ''
guess = ''
output = ''
balance = int(1000)


game()



