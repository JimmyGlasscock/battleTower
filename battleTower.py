# Created By Jimmy Glasscock - 8/16/19

# TO DO:
# create and run base stat & move scraper
# when user clicks on a pokemon it will grab the base stats and generate from theres
# use gen 5 GIFs for sprites (togglable?)

import random

class Pokemon:

	# until support for this is added, iv values will be 0, nature will be 1
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
	# takes in classification as a string to determine physical/special/none
	def __init__(self, name, typeOfMove, baseDamage, classification):
		self.name = name
		self.typeOfMove = typeOfMove
		self.baseDamage = baseDamage
		self.classification = classification

class Battle:
	#type chart is a 2D array and each type is a number (a row or column)
	#Type order is as follows:
	#Normal, Fighting, Flying, Poison, Ground, Rock, Bug, Ghost, Steel, Fire, Water, Grass, Electric, Psychic, Ice, Dragon, Dark, Fairy
	#	0		1		  2		  3		  4		 5	  6		7	   8	 9	   10	   11		12		 13		14	  15	 16		17

	#Attacking type is row, Defending type is column
	typeEffectivenessChart = [
		(2,2,2,2,2,1,2,0,1,2,2,2,2,2,2,2,2,2),#normal
		(4,2,1,1,2,4,1,0,4,2,2,2,2,1,4,2,4,1),#fighting
		(2,4,2,2,2,1,4,2,1,2,2,4,1,2,2,2,2,2),#flying
		(2,2,2,1,1,1,2,1,0,2,2,4,2,2,2,2,2,4),#poison
		(2,2,0,4,2,4,1,2,4,4,2,1,4,2,2,2,2,2),#ground
		(2,1,4,2,1,2,4,2,1,4,2,2,2,2,4,2,2,2),#rock
		(2,1,1,1,2,2,2,1,1,1,2,4,2,4,2,2,4,1),#bug
		(0,2,2,2,2,2,2,4,2,2,2,2,2,4,2,2,1,2),#ghost
		(2,2,2,2,2,4,2,2,1,1,1,2,1,2,4,2,2,4),#steel
		(2,2,2,2,2,1,4,2,4,1,1,4,2,2,4,1,2,2),#fire
		(2,2,2,2,4,4,2,2,2,4,1,1,2,2,2,1,2,2),#water
		(2,2,1,1,4,4,1,2,1,1,4,1,2,2,2,1,2,2),#grass
		(2,2,4,2,0,2,2,2,2,2,4,1,1,2,2,1,2,2),#electric
		(2,4,2,4,2,2,2,2,1,2,2,2,2,1,2,2,0,2),#psychic
		(2,2,4,2,4,2,2,2,1,1,1,4,2,2,1,4,2,2),#ice
		(2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,4,2,0),#dragon
		(2,1,2,2,2,2,2,4,2,2,2,2,2,4,2,2,1,1),#dark
		(2,4,2,1,2,2,2,2,1,1,2,2,2,2,2,4,4,2)#fairy
	]

	# both teams are stored as arrays
	def __init__(playerTeam, oppoTeam):
		self.battleIntro()
		self.battleLoop(playerTeam, oppoTeam)

	def checkFainted(self, fighter):
		if(fighter.HP < 0 or fighter.HP == 0):
			fighter.HP = 0
			fighter.status = "FNT"

	def playerTurn(self, player, opponent):
		#prompt the user to fight, switch, or use item
		
		#this should be last
		self.checkFainted(player)
		self.checkFainted(opponent)

	def opponentTurn(self, player, opponent):
		#uses the game's formula to decide which opponent attack to use
		
		#this should be last
		self.checkFainted(player)
		self.checkFainted(opponent)

	def calculateDamage(attacker, defender, move):
		damageDealt = 0
		modifier = 1

		attackStat = 0
		defenseStat = 0

		if(move.classification == "physical"):
			attackStat = attacker.attack
			defenseStat = defender.defense
		elif(move.classification == "special"):
			attackStat = attacker.specAttack
			defenseStat = defender.specDefense

		damageDealt = ((((((2 * attacker.level)/5)+2) * move.baseDamage * (attackStat/defenseStat))/50) + 2)

		#change me if you want critical hit support
		critical = 1
		rand = random.randint(0.85, 1.00)
		#stands for same type attack bonus
		stab = 1

		if(attacker.types[0] == move.typeOfMove or attacker.types[1] == move.typeOfMove):
			stab = 1.5

		typeEffectiveness = self.calculateTypeEffectiveness(defender.types, move.type)

		burn = 1
		if(attacker.status == "burned"):
			burn = 0.5

		modifier = (critical * rand * stab * typeEffectiveness * burn);

		return int(damageDealt * modifier)

	#opponentTypes is an array
	def calculateTypeEffectiveness(opponentTypes, moveType):
		effectiveness = typeEffectivenessChart[moveType][opponentTypes[0]]
		effectiveness *= 0.5

		if(opponentTypes[1] != -1):
			effectiveness2 = typeEffectivenessChart[moveType][opponentTypes[1]]
			effectiveness2 *= 0.5
			effectiveness = effectiveness * effectiveness2


		return effectiveness

	def compareSpeed(self, player, opponent):
		pokemonFainted = False

		if(opponent.speed > player.speed):
			self.opponentTurn(player, opponent)
			if(player.status != "FNT"):
				self.playerTurn(player, opponent)
				pokemonFainted = True
		else:
			self.playerTurn(player, opponent)
			if(opponent.status != "FNT"):
				self.opponentTurn(player, opponent)
				pokemonFainted = True

		return pokemonFainted

	def battleLoop(self, playerTeam, oppoTeam):
		turnNumber = 0
		# this is true if the players entire team is fainted
		playerWhiteout = False
		# this is true if the opponent's entire team is fainted
		opponentWhiteout = False

		currentPlayer = playerTeam[0]
		currentOpponent = oppoTeam[0]

		while(opponentWhiteout != True and playerWhiteout != True):
			#weather conditions

			#compare speed, call player/opponent attack based on which
			pkmnFainted = self.compareSpeed(currentPlayer, currentOpponent)

			if(pkmnFainted):
				playerWhiteout = checkWhiteout(playerTeam)
				opponentWhiteout = checkWhiteout(oppoTeam)

			#apply status if status

			#turn number is increased last
			turnNumber += 1

		#finish out battle based on who won
