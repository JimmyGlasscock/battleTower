#rename me
class Po:
	# the constructor will generate the stats
	# takes in moves as an array
	# types will be an array as well
	def __init__(self, num, name, attack, defense, specAttack, specDefense, speed, HP, MaxHP, types, moves):
		#generate stats here

		# HP = (((2 * baseHP + IV + (EV/4)) * level)/100) + level + 10
		# Other Stat = ((((2 * baseStat + IV + (EV/4)) * level)/100) + 5) * nature

		self.num =num
		self.name = name
		self.attack = attack
		self.defense = defense
		self.specAttack = specAttack
		self.specDefense = specDefense
		self.speed = speed
		self.HP = HP
		self.MaxHP = MaxHP

		self.types = types
		self.moves = moves

class Move: 
	# takes in physical as a boolean to determine physical/special
	def __init__(self, name, typeOfMove, baseDamage, physical):
		self.name = name
		self.typeOfMove = typeOfMove
		self.baseDamage = baseDamage
		self.physical = physical