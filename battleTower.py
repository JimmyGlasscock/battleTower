#rename me
class Po:
	# the constructor will generate the stats
	# takes in moves as an array
	# types will be an array as well
	def __init__(self, num, name, level, attack, defense, specAttack, specDefense, speed, HP, types, moves):
		#generate stats here

		#until EV, IV and nature support is added, they will be these values:
		IV = 0
		EV = 0
		nature = 1

		self.num =num
		self.name = name
		self.level = level
		self.attack = generateStat(attack, IV, EV, level, nature)
		self.defense = generateStat(defense, IV, EV, level, nature)
		self.specAttack = generateStat(specAttack, IV, EV, level, nature)
		self.specDefense = generateStat(specDefense, IV, EV, level, nature)
		self.speed = generateStat(speed, IV, EV, level, nature)
		self.MaxHP = generateHP(HP, IV, EV, level)
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

class Move: 
	# takes in physical as a boolean to determine physical/special
	def __init__(self, name, typeOfMove, baseDamage, physical):
		self.name = name
		self.typeOfMove = typeOfMove
		self.baseDamage = baseDamage
		self.physical = physical