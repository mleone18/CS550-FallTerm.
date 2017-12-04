n = int(input('N: '))

for a in range(n):
	if 2**a > n:
		break
	print(2**a)