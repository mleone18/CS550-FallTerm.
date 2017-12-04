class Bank:
	def __init__(self, account, balance, pin, isOpen):
		self.account = account
		self.balance = balance
		self.pin = pin
		self.isOpen = True

	def closed(self):
		if self.isOpen == True:
			print("Account is open. Balance: " + str(self.balance)) 
		else:
			print("Account closed.")

	def deposit(self, amount):
		self.balance += amount
		print("You deposited: " +str(amount))
		print("New Balance = " + str(self.balance))

	def withdraw(self, amount):
		self.balance -= amount
		print("You withdrew: "+ str(amount))
		print("New Balance = " + str(self.balance))

	def interest(self, time, rate):
		self.balance = int(self.balance)*((1+rate)**time)
		print("After " + str(time) + " years, Balance = " + str(self.balance))

mybank = Bank(696969, 100000, 1234, 5)
mybank.closed()
mybank.deposit(500)
mybank.withdraw(250)
mybank.interest(5, 0.015)