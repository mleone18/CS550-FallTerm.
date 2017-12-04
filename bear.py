class Bear:
	def __init__(self, name, age, breed, color, tactic):
		self.color = color
		self.name = name
		self.age = age
		self.breed = breed
		self.tactic = tactic
		self.energy = 1
		self.hunger = 1
		self.isAlive = True

	def eat(self, amount): 
		if self.hunger > 0:
			self.hunger -= amount
			self.energy += amount
			print("You fed borus.")
		else:
			print(str(self.name) + " isn't hungry.")

	def play(self, intensity):
		if self.hunger <= 0 and self.energy > 0:
			self.hunger += intensity 
			self.energy -= intensity
			print(str(self.name) + " is playing.")
		else:
			print(str(self.name) + " is too tired to play.")

	def sleep(self, time):
		if self.energy < 0:
			print("Borus is now tired and went to sleep.")
			self.energy += time*0.2
		else: 
			print(str(self.name) + " isn't tired yet.")

	def snore(self, time): #must put same time in snore as in sleep
		if time > 4:
			print("ZZZZZZzzzzzz.")
			self.energy +=time*0.2
		else: 
			print("Shh. You might wake" + str(self.name))

	def growl(self):
		if self.energy > 0:
			print("GRRRRRRRRR!!!!!!! You woke " + str(self.name))
			self.energy -= 1
		else: 
			print(str(self.name) + "is too tired to growl.")

	def stats(self):
		print("Name: " + str(self.name))
		print("Energy: "+ str(self.energy))
		print("Hunger: "+ str(self.hunger))

mybear = Bear("Borus", 7, "Pol-Grizzly", "White with brown polka dots", "Growl and Kick")
mybear.stats()
mybear.play(5)
mybear.eat(1)
mybear.play(5)
mybear.sleep(10)
mybear.snore(10)
mybear.growl()


