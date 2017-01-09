from superhero import *
from flying import *
from running import *
from swimming import *
from sidekick import *
from bulletproof import *

class Superman(Superhero, Flight, Running, Swimming, Bulletproof):

	def __init__(self):
		Superhero.__init__(self, 'Super Man')
		Bulletproof.__init__(self)
		self.sidekicks.add(Sidekick("Jimmy Olsen"))
		self.air_speed = 1000000
		self.swim_speed = 2000
