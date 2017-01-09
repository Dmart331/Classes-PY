import unittest
from superhero import *

class TestSuperHero(unittest.TestCase):

	def test_superheroMustHaveNameProperty(self):

		random_superhero = Superhero("Bilbo")
		self.assertEqual(random_superhero.name , "Bilbo")

	def test_superheroAddPowerMustIncludePower(self):

		random_superhero = Superhero("Clark")
		random_superhero.add_power('Invisibility')
		self.assertIn("Invisibility", random_superhero.powers)

	def test_superheroRemovePowerMustRemovePower(self):

		random_superhero = Superhero("Drew")
		random_superhero.add_power("Super Punch")
		random_superhero.remove("Super Punch")
		self.assertNotIn("Super Punch", random_superhero.powers)
if __name__ == '__main__':
	unittest.main()