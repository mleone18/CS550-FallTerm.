n = int(input('N: '))
a = 0
b = 1
c = 0

while c <= n:
	if c == 0:
		b = 0
	elif c == 1:
		b = 1
	else:
		temp = a + b 
		a = b 
		b = temp
	c += 1
print(b)
