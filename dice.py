import random
import sys

#Matthew Leone, October 5, 2017, Gambling Dice Game that keeps track of previous balance. 
#No outside sources besides Ms. Healey, 
#On my honor I have neither given nor received unauthorized aid. 

def quit(): #this program will be utilized whenever the user inputs "quit" into any of the potential input areas (bet and guess). This way, the game does not simply end once they run out of money. They can walk away with their winnings just like in a real casino.
	global balance #global balance will keep the balance variable in all of the programs consistent. The balance will always be changing as a result.
	global name # global name is just so that way my program can say goodbye in a personal manner. Again, it takes the name inputted at the beginning.

	balance = balance*(0.95) #Casino wants a 5 percent cut of whatever the player walks away with. it is only fair.
	print('Final Balance: ' + str(balance)) # just to remind the user what it is that they are leaving the table with.
	print('Goodbye ' + name + '! We\'re taking 5% as a commission. Enjoy your winnings.')
	sys.exit() #this function quits the entire program without the option to restart. I assume that they are quitting and no longer want to play. 

def collectData(): #collect data is when the bulk of user input is obtained. This is where they enter their bets and guesses. If they choose to quit, this is where the user requests that also. Within this program, many other programs are referenced to maintain a clean overall code. 
	global bet #global bet makes it so that the bet inputted by the user here carries over to the game program, which is where the balances are handled.
	global guess #global guess also makes it so the guess inputted by the user here carries over to the game program, which is where the balances are handled, assuming that their guesses and bets aren't to quit and that they satisfy the integer values.
	global output #global output takes the dice output and carries it over to the game function. 
	global balance #stated above. 

	bet = ''
	while True: #while true is a loop that basically says that as long as all underlying conditions are maintained and abided by, the code within the program will run continuously.
		try: #basically if the underlying code is correctly followed, it will run, if it is not, the exception function will be run.
			bet = input('Place bet: ') #user bet input
			if bet == 'quit' or bet == 'QUIT' or bet == 'Quit' or bet == 'Quit': #user quit input.
				quit() #conditional statement. if user wants to quit. quit program will run
			else:
				bet = int(bet) #if user does not quit, and does not enter a string, the bet will run as an integer.
				if bet < 50 or bet > balance: 
					print('Please enter a bet that is between $50 and your balance of $' + str(balance) + '.')
				else:
					break
		except ValueError: #if bet is letters, but not quit, the while loop will rerun. 
			print('That bet is not an integer. Try again.')

	guess = ''
	while True: 
		try:
			guess = input('Guess a number: ')
			if guess == 'quit' or guess == 'QUIT' or guess == 'quit' or guess == 'Quit':
				quit()
			else:
				guess = int(guess)
				if guess < 2 or guess > 12:
					print('Please guess a number within the specified range of 2-12.')
				else: 
					break
		except ValueError:
			print('That guess is not an integer. Try again.')

	output = ''
	while True:
		output = int((int(random.randrange(1,7))) + (int(random.randrange(1,7)))) #the way dice work, odds of landing a number 1-12 are not all equal. 7 has highest likelihood. So, I basically made my output the sum of 2 dice rather than just a random integer 2-12.
		break

def restart(): #comes once user runs out of money. Will restart the game basically if the below conditions are run.
	global balance #needs the balance to know if it is less than 0

	restart = ''
	while True:
		restart = input('Would you like to start a new game (Y/N): ')
		if restart == 'Y' or restart =='y' or restart == 'Yes' or restart == 'yes' or restart == 'yea' or restart == 'ya' or restart == 'yeah':
			balance = int(1000) #because the balance became 0, I must give them a new balance of 1000. otherwise the new balance will be 0 since it is global.
			print('Balance: ' + str(balance))
			game() #will restart game if they want to.
		elif restart == 'N' or restart == 'n' or restart == 'NO' or restart == 'no' or restart == 'No' or restart == 'nah' or restart == 'Quit' or restart == 'QUIT' or restart == 'quit':
			print('Goodbye and thanks for the money! Here\'s $15 for a cab.') #i don't want to make them walk home. I just took all their money.
			sys.exit() #same as sys.exit above, ends the program.
		else:
			print('That\'s not an option.') #don't need exceptions here since it is a string. If they don't say yes or no it will prompt this. Numbers are handled as strings, not integers.

def game(): #takes all of the above programs and handles it. 
	global guess
	global balance
	global output
	global bet

	while True: 
		collectData() #taking all of the data from above.
		print('Your Guess: ' + str(guess))
		print('Dice Output: ' + str(output))
		print('Your Bet: ' + str(bet))
		print('Previous Balance:  ' + str(balance))
		if guess == output:
			balance = balance + bet*(1.5)
			print('Updated Balance: ' + str(balance))
		elif guess > 6 and output > 6:
			balance = balance + bet
			print('Updated Balance: ' + str(balance))
		elif guess < 6 and output <= 6:
			balance = balance + bet
			print('Updated Balance: ' + str(balance))
		else:
			balance = balance - bet
			print('Updated Balance: '+ str(balance))
		if balance < 50:
			print('Game over. You should probably not be gambling.')
			restart()
		else: 
			game()



name = input('Before we begin, what is your name?: ')
print(name + ', welcome to the Choate Casino.')
print('You have $1,000 to gamble with.')
print('Each round please guess the outcome of a pair of randomly rolled dice 2-12.')
print('If your guess >= 7 and the outcome >= 7, you win your bet.')
print('If your guess <= 6 and the outcome <= 6, you also win your bet.')
print('If you guess the correct outcome, you win your bet and an additional 50%.')
print('Otherwise, you lose your bet.')
print('Each bet must be at least $50 and less than your balance.')
print('The game ends once you run out of money or say (Quit) at any time.')
print('Good Luck!')

bet = ''
guess = ''
output = ''
balance = int(1000)


game() #this is the only program that actually runs. It has all of the above programs within it, so it will run continuously unless one of the code's within the program prompt an end. 



