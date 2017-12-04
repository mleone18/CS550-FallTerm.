import sys

t = float(input('T: '))

v = float(input('V: '))


w = (35.74 + (0.6215*t) + (((0.4275*t) - 35.75)*(v**0.16)))

if (3 < v < 120) and (t < abs(50)):
	print(w)

