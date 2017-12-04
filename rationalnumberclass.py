class Rationalnumber:
	def __init__(self, n, d):
		self.n = n
		self.d = d

	def __truediv__(self, y):
		return Rationalnumber(self.n * y.d, self.d * y.n)
	def __mul__(self, y):
		return Rationalnumber(self.n * y.n, self.d * y.d)
	def __add__(self, y):
		return Rationalnumber(self.n * y.d + self.d * y.n, self.d * y.d)
	def __sub__(self, y):
		return Rationalnumber(self.n * y.d - self.d * y.n, self.d * y.d)
	def __str__(self):
		return str(self.n) + '/' + str(self.d)

def main(): #Actually calling the above functions here. Do not need to say (__mul__) etc. Python interprets the symbols as a command to check the above code. 
	a = Rationalnumber(1,2)
	b = Rationalnumber(1,3)
	print(a)#1/2
	print(b)#1/3
	print(a+b)#5/6
	print(a-b)#1/6
	print(a*b)#1/6
	print(a/b)#3/2

main()
