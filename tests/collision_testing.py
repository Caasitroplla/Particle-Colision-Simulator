import unittest
from particle import Particle
from collision import collide
import src 


class Test_Particle_Collision_Procedure(unittest.TestCase):
	def test_particle_collision_procedure(self):
		actual_a = Particle(0, 0, 1, 1, 2)
		actual_b = Particle(0, 0, 3, 2, 1)
		
		collide(actual_a, actual_b)
		
		expected_a = Particle(0, 0, 3, 2, 2)
		expected_b = Particle(0, 0, (1/3), (2/3), 1)
		
		self.assertEqual(actual_a, expected_a)
		self.assertEqual(actual_b, expected_b)
