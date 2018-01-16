from random import randiant
class StudentFighter(object):
	def __init__(self, strngth, health, name):
		self.strngth = strngth
		self.name = name
		self.health = health
	def attack(self, opponent):
		multiplier = randint(1, 4)
		damage = multiplier * self.strength
		opponent.health -= damage
		message = "{} has {} health points remaining".format(opponent.name, opponent.health)print(message)
kalu = StudentFighter(strngth=3, health=100, name="Kalu")
david = StudentFighter(strngth=5, health=100, name="David")
kalu.attack(david)
