# Created By Jimmy Glasscock - 8/16/19

# TO DO:
# when user clicks on a pokemon it will grab the base stats and generate from there
# do a battle intro animation, call it on scene before main loop
# define checkWhiteout method

#this uses Pillow and not PIL
import random
import pygame
from pygame.locals import *
from PIL import Image
import datetime as dt

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
		odds = 4096
		num = random.randint(1,odds)

		if(num == odds):
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
	def __init__(self, playerTeam, oppoTeam):
		self.battleIntro()
		self.battleLoop(playerTeam, oppoTeam)

	def battleIntro(self):
		print("finish battle intro")

	def checkFainted(self, fighter):
		if(fighter.HP < 0 or fighter.HP == 0):
			fighter.HP = 0
			fighter.status = "FNT"

	def checkWhiteout(self, team):
		result = False

		for pokemon in team:
			if(pokemon.status == "FNT"):
				result = False

		return result

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

				#switchPokemonMethod
				self.scene.updatePkmn(None, True)
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

		self.currentPlayer = playerTeam[0]
		self.currentOpponent = oppoTeam[0]

		self.scene = Scene(BG, self)

		#call this from inside scene using battleObj.currentPKMN
		self.scene.updatePkmn(self.currentPlayer, True)
		self.scene.updatePkmn(self.currentOpponent, False)

		while(opponentWhiteout != True and playerWhiteout != True):

			self.scene.drawSceneBattle()

			#weather conditions

			#compare speed, call player/opponent attack based on which
			pkmnFainted = self.compareSpeed(currentPlayer, currentOpponent)

			if(pkmnFainted):
				playerWhiteout = self.checkWhiteout(playerTeam)
				opponentWhiteout = self.checkWhiteout(oppoTeam)

			#apply status if status

			#turn number is increased last
			turnNumber += 1

		#finish out battle based on who won

#This class is going to handle everything graphics related
#everything on the screen
class Scene:
	#init sets the background as well as the drawing bool to true
	def __init__(self, bg, battleObj):
		self.drawing = True
		self.bg = bg
		self.battleObj = battleObj

	def drawSceneBattle(self):
		#should I call this here?
		pygame.init()

		self.font = pygame.font.Font("font/font.ttf", 16)

		#screen is what is drawn to
		self.screen = pygame.display.set_mode((600,430))
		#pygame.display contains various settings
		pygame.display.set_caption("Battle Tower")

		textbox = pygame.image.load("img/ui/Textbox.png")
		textbox = pygame.transform.scale(textbox, (600, 105))

		HPBar = pygame.image.load("img/ui/HPBar.png")
		OppoHPBar = pygame.image.load("img/ui/OpponentHPBar.png")

		self.lastPKMN = self.battleObj.currentPlayer
		self.lastOpponent = self.battleObj.currentOpponent

		#this is the rendering loop
		while self.drawing:
			self.screen.blit(self.bg, (0,0))
			self.screen.blit(self.playerPokemonSprite, (60,self.playerY))
			self.screen.blit(self.opponentPokemonSprite, (375,self.oppoY))

			self.screen.blit(HPBar, (356, 225))
			self.screen.blit(OppoHPBar, (0, 60))

			self.screen.blit(textbox, (0,325))

			#draws player & opponent hp
			self.drawHP(self.screen, False)
			self.drawHP(self.screen, True)

			self.drawName(self.screen, False)
			self.drawName(self.screen, True)

			self.drawLevel(self.screen, False)
			self.drawLevel(self.screen, True)

			#updates PKMN if it changed
			if(self.lastPKMN != self.battleObj.currentPlayer):
				self.updatePkmn(self.battleObj.currentPlayer, True)
				self.lastPKMN = self.battleObj.currentPlayer
			if(self.lastOpponent != self.battleObj.currentOpponent):
				self.updatePkmn(self.battleObj.currentOpponent, False)
				self.lastOpponent = self.battleObj.currentOpponent

			#this should be last thing done with display
			pygame.display.flip()

			#do this last
			for event in pygame.event.get():
				if(event.type == pygame.QUIT):
					pygame.display.quit()
					pygame.quit()

	# this method switches the pokemon

	#isPlayerPokemon is a bool that determines whether the
	#player or opponent is switched out
	def updatePkmn(self, playerPKMN, isPlayerPokemon):
		shinyPath = ""

		if(playerPKMN.shiny):
			shinyPath = "shiny/"

		if(isPlayerPokemon):
			self.playerPKMN = playerPKMN

			filepath = "img/sprites/back/" + shinyPath + str(playerPKMN.num) +".png"	
			player = pygame.image.load(filepath)
			self.playerPokemonSprite = pygame.transform.scale(player, (160,160))

			#default
			self.playerY = 165
			self.playerY += self.getYCoordinates(filepath)


		else:
			self.oppoPKMN = playerPKMN

			filepath = "img/sprites/" + shinyPath + str(playerPKMN.num) +".png"
			oppo = pygame.image.load(filepath)
			self.opponentPokemonSprite = pygame.transform.scale(oppo, (160, 160))

			#default
			self.oppoY = 45
			self.oppoY += self.getYCoordinates(filepath)

	def updatePlayerHPBar(self, HPnum, isPlayerPokemon):
		print("updated")

	#isPlayerPokemon is a bool that determines whether the
	#player or opponent uses the move
	def moveAnimation(self, move, isPlayerPokemon):
		print("___ used move")

	def updateMessageboxText(self, newText, duration):
		#add scrolling text
		#self.screen.blit(newText, (20, 500))
		print(newText)

	#some Moves update the background, this is for that
	def updateBG(self, move, duration):
		print("updated")

	def getYCoordinates(self, filepath):
		image = Image.open(filepath).convert('RGBA')
		pixeldata = list(image.getdata())

		width, height = image.size

		lastpixel = height

		frontSprite = True

		if("back" in filepath):
			frontSprite = False

		if(frontSprite):
			#check if pokemon floats, if yes return 0
			with open("floatingPKMN.txt") as f:
				for line in f:
					line = line.rstrip()
					if(str(line)+".png" in filepath):
						return 0

		for y in range(height):
			for x in range(width):
				r, g, b, a = image.getpixel((x,y))

				if(a != 0):
					lastpixel = y + 1					

		#have to scale by 2
		return (height - lastpixel)*2

	#player is a bool
	def drawHP(self, screen, player):
		green = (0, 255, 0, 255)
		yellow = (255, 250, 0, 255)
		red = (255, 0, 0, 255)

		currentColor = green

		MaxHP = 97
		HP = MaxHP

		x = 72
		y = 106
		size = 6

		if(player):
			HP *= int(self.playerPKMN.HP/self.playerPKMN.MaxHP)

			x = 498
			y = 273
		else:
			HP *= int(self.oppoPKMN.HP/self.oppoPKMN.MaxHP)

		if(HP < 20):
			currentColor = red
		elif(HP < 49):
			currentColor = yellow

		pygame.draw.rect((screen), currentColor,(x,y,HP,size))

	#player is a bool determines if this is playerName or OppoName
	def drawName(self, screen, player):
		name = ""
		x = 0
		y = 0
		if(player):
			name = self.playerPKMN.name
			x = 420
			y = 240
		else:
			name = self.oppoPKMN.name
			x = 8
			y = 73

		text = self.font.render(name, False, (0,0,0))
		screen.blit(text, (x,y))

	def drawLevel(self, screen, player):
		lv = 0
		x = 0
		y = 0
		if(player):
			lv = self.playerPKMN.level
			x = 570
			y = 240
		else:
			lv = self.oppoPKMN.level
			x = 143
			y = 73
		text = self.font.render(str(lv), False, (0,0,0))
		screen.blit(text, (x,y))

BG = None

#sets time of day bg
if((dt.datetime.now().hour) > 6 and (dt.datetime.now().hour) < 17):
	BG = pygame.image.load("img/bg/BGMorning.png")
elif((dt.datetime.now().hour) < 19):
	BG = pygame.image.load("img/bg/BGDusk.png")
else:
	BG = pygame.image.load("img/bg/BGNight.png")

Bulba = Pokemon(1, "Bulbasaur", 50, 45, 45, 65, 65, 60, 60, 0, 0)
Charm = Pokemon(4, "Charmander", 50, 50, 50, 45, 45, 60, 60, 0, 0)

playerTeam = [Bulba, Charm]
oppoTeam = [Charm, Bulba]

battle = Battle(playerTeam, oppoTeam)