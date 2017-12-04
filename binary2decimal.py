import sys
binary = str(input('Pick a binary number: '))
numdig = len(binary)
decimal = 0
x = 0

for x in range(0,numdig):
	decimal = decimal + (int(binary[x])*(2**x))
	x = x + 1
print(decimal)