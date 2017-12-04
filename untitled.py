
def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

print(fib(4))

def fact(n):
	if n == 1:
		return 1
	elif n == 2:
		return 2
	elif n == 3:
		return 6
	else:
		return n*(fact(n-1))

print(fact(8))