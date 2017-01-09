import unittest
from superman import *

class TestSuperman(unittest.TestCase):

	def test_SupermanIsASuperhero(self):
		superman = Superman()

		self.assertIsInstance(superman , Superhero)

	def test_SupermanIsAFlyingSuperhero(self):
		superman = Superman()
		self.assertIsInstance(superman, Flight)

	def test_SupermanIsARunningSuperhero(self):
		superman = Superman()
		self.assertIsInstance(superman, Running)

	def test_SupermanIsASwimmingSuperhero(self):
		superman = Superman()
		self.assertIsInstance(superman, Swimming)

	def test_SupermanFlyingIsFast(self):
		superman = Superman()
		self.assertEqual(superman.air_speed, 1000000)

	def test_SupermanSwimmingIsFast(self):
		superman = Superman()
		self.assertEqual(superman.swim_speed, 2000)

	def test_SupermanMustBeBulletProof(self):
		superman = Superman()
		self.assertTrue(superman.is_bulletproof)

if __name__ == '__main__':
	unittest.main()