
number = int(input('Pick a number: '))
if number%11 == 0 or number%11 == 1:
	print('Your number is special')
else:
	print('Your number is not special')




def specialNumbers(number):
	if number%11 == 0 or number%11 ==1:
		return True;
	else:
		return False;