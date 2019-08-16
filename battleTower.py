# Created By Jimmy Glasscock - 8/16/19

# TO DO:
# create and run base stat & move scraper
# when user clicks on a po it will grab the base stats and generate from there
# rename Po class

import random

#rename me
class Po:

	# until support for this is added, ev & iv values will be 0, nature will be 1
	def generateStat(self, stat, IV, EV, level, nature):
		newStat = ((((2 * stat + IV + (EV/4)) * level)/100) + 5) * nature;
		newStat = int(newStat)
		return newStat;

	def generateHP(self, HP, IV, EV, level):
		newHP = (((2 * HP + IV + (EV/4)) * level)/100) + level + 10;
		newHP = int(newHP)
		return newHP;

	#returns boolean, 1/4096 odds it will be true
	def shinyRoll(self):
		num = random.randint(1,4096)

		if(num == 4096):
			return True
		return False

	# the constructor will generate the stats
	# takes in moves as an array
	# types will be an array as well
	def __init__(self, num, name, level, HP, attack, defense, specAttack, specDefense, speed, types, moves):
		#generate stats here

		#until IV and nature support is added, they will be these values:
		IV = 0
		nature = 1

		self.num =num
		self.name = name
		self.level = level

		self.shiny = self.shinyRoll()

		# EV values are generated and stored
		self.attackEV = random.randint(1,31)
		self.defenseEV = random.randint(1,31)
		self.specAttackEV = random.randint(1,31)
		self.specDefenseEV = random.randint(1,31)
		self.speedEV = random.randint(1,31)
		self.HPEV = random.randint(1,31)

		self.attack = self.generateStat(attack, IV, self.attackEV, level, nature)
		self.defense = self.generateStat(defense, IV, self.defenseEV, level, nature)
		self.specAttack = self.generateStat(specAttack, IV, self.specAttackEV, level, nature)
		self.specDefense = self.generateStat(specDefense, IV, self.specDefenseEV, level, nature)
		self.speed = self.generateStat(speed, IV, self.speedEV, level, nature)
		self.MaxHP = self.generateHP(HP, IV, self.HPEV, level)
		self.HP = self.MaxHP
		self.types = types
		self.moves = moves

		self.status = ""

	# this method is for testing purposes
	def printStats(self):
		print(self.name)
		print("Level: " + str(self.level))
		print("")
		print("HP: " + str(self.HP) + "/" + str(self.MaxHP))
		print("")
		print("Attack: " + str(self.attack))
		print("Defense: " + str(self.defense))
		print("Special Attack: " + str(self.specAttack))
		print("Special Defense: " + str(self.specDefense))
		print("Speed: " + str(self.speed))
		print("Shiny: " + str(self.shiny))

class Move: 
	# takes in physical as a boolean to determine physical/special
	def __init__(self, name, typeOfMove, baseDamage, physical):
		self.name = name
		self.typeOfMove = typeOfMove
		self.baseDamage = baseDamage
		self.physical = physical

class Battle:
	# both teams are stored as arrays
	def __init__(playerTeam, oppoTeam):
		print("this will start the loop and do the various checks")

	def playerTurn():
		print("player turn")

	def opponentTurn():
		print("opponent turn")

	def battleLoop():
		turnNumber = 0
		playerWhiteout = False
		opponentWhiteout = False

		while(opponentWhiteout != True && playerWhiteout != True):
			print("this will increase turnNumber and all that good stuff")
