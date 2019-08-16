# TO DO:
# create and run base stat & move scraper
# when user clicks on a po it will grab the base stats and generate from there
# 

import random

#rename me
class Po:
	# the constructor will generate the stats
	# takes in moves as an array
	# types will be an array as well
	def __init__(self, num, name, level, attack, defense, specAttack, specDefense, speed, HP, types, moves):
		#generate stats here

		#until IV and nature support is added, they will be these values:
		IV = 0
		nature = 1

		self.num =num
		self.name = name
		self.level = level
		self.attack = generateStat(attack, IV, random.randint(1,31), level, nature)
		self.defense = generateStat(defense, IV, random.randint(1,31), level, nature)
		self.specAttack = generateStat(specAttack, IV, random.randint(1,31), level, nature)
		self.specDefense = generateStat(specDefense, IV, random.randint(1,31), level, nature)
		self.speed = generateStat(speed, IV, random.randint(1,31), level, nature)
		self.MaxHP = generateHP(HP, IV, random.randint(1,31), level)
		self.HP = self.MaxHP
		self.types = types
		self.moves = moves

	# until support for this is added, ev & iv values will be 0, nature will be 1
	def generateStat(stat, IV, EV, level, nature):
		newStat = ((((2 * stat + IV + (EV/4)) * level)/100) + 5) * nature;
		return newStat;

	def generateHP(HP, IV, EV, level):
		newHP = (((2 * HP + IV + (EV/4)) * level)/100) + level + 10;
		return newHP;

	# this method is for testing purposes
	def printStats():
		print(self.name)
		print("Level: " + self.level)
		print("")
		print("HP: " + self.HP + "/" + self.MaxHP)
		print("")
		print("Attack: " + self.attack)
		print("Defense: " + self.defense)
		print("Special Attack: " + self.specAttack)
		print("Special Defense: " + self.specDefense)
		print("Speed: " + self.speed)

class Move: 
	# takes in physical as a boolean to determine physical/special
	def __init__(self, name, typeOfMove, baseDamage, physical):
		self.name = name
		self.typeOfMove = typeOfMove
		self.baseDamage = baseDamage
		self.physical = physical