import random
n = int(input('Number of flips: '))
heads = 0
tails = 0

for x in range(0,n):
	output = random.uniform(0,1)
	if output < 0.5:
		tails = tails + 1
	else:
		heads = heads + 1

percent = (heads / (heads + tails)) * 100

print(percent)