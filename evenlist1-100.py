#generates list of first 50 even numbers 1-100.
l1 = []
for x in range(1,51):
	l1.append(x)
l2 = [x * 2 for x in l1]
print(l2)

