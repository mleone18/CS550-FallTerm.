import sys 

from random import randint

x = (randint(0,100)/100)

print(x)

if x < 0.5:
	print('False')
else:
	print('True')
