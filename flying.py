class Flight:

	def __init__(self):
		self.air_speed = 0
		self.max_load = 0
		self.max_altitude = 0

	def fly(self):
		print("I am Flying at {} mps".format(self.air_speed))
