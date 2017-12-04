class Cat:
	def __init__(self, name, age, breed, color): 
	self.color = color
	self.name = name
	self.age = age
	self.breed = breed
	self.size = 150
	self.energy = 100
	self.hunger = 300
	self.isAlive = True 

	def eat(self): 
		if self.hunger > 50:
			self.hunger -= 15
			self.energy += 15
			self.strength += 10
			print("Yummy!")
		else:
			print(self.name + "isn't hungry")

	def stats(self):
		print("Name: " + self.name)
		print("Energy: " + str(self.energy))
		print("Hunger: " + str(self.hunger))

mycat = Dog("Tigger", 5, "Tiger", "Orange")
mycat.stats()
mycat.eat(5)
mycat.eat(7)
mycat.eat(35)
mycat.eat(100)
mycat.stats()
mycat.