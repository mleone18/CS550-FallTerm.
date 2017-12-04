import random
seven = 0
others = 0
n = int(input('number of times: '))

for x in range(0,n):
	output = int((int(random.randrange(1,7))) + (int(random.randrange(1,7))))
	if output == 7:
		seven = seven + 1
	else: 
		others = others + 1


percentage = (seven/ (seven + others))*100


print(percentage)