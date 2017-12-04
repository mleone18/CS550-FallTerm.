import sys

x = float(input('X: '))
y = float(input('Y: '))
z = float(input('Z: '))

if (x<y<z) or (x>y>z): 
	print('True')

if (x>y<z) or (x<y>z):
	print('False')