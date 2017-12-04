


def average(x,y,z=None):
	if z == None:
		try:
			return ((int(x)+ int(y))/2)
		except ValueError:
			return None
	else:
		try:
			return ((int(x) + int(y) + int(z))/3)
		except ValueError:
			return None

print(average(5,6))
print(average(5,6,7))
print(average(5,6,'7'))
print(average('5','6','7'))
print(average('5','6'))
