import random


play = 'yes'
while play == 'yes':
	a = random.randrange(0,100)
	print(a)

	guess = int(input('Please Guess, number must be between 0 and 100: '))
	while guess != a:
		if guess < a:
			print('Too Low')
		else:
			print('Too High')
		
		guess = int(input('Guess Again: '))
	print('You win!')
	play = input('Do you want to play again?')
print('Have a nice day!')
