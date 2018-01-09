class StudentFighter(object):
	 def __init__(self, strength, health, name):
	 	self.strength = strength
	 	self.name = name
	 	self.health = health

kalu = StudentFighter(strength=3, health=100, name="Kalu")
david = StudentFighter(strength=5, health=100, name="David")

print(kalu.name, kalu.strength, kalu.health)
print(david.name, david.strength, david.health)