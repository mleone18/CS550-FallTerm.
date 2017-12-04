import sys
birthday = input('Is it your birthday? ')
speed = int(input('Speed: '))


if birthday == ('No'):
	if speed <= 60:
		print('No Ticket')
	elif speed > 60 and speed < 80:
		print('Small Ticket')
	else:
		print('Big Ticket')
else:
	if speed <= 65:
		print('No Ticket')
	elif speed > 65 and speed <= 85:
		print('Small Ticket')
	else:
		print('Big Ticket')