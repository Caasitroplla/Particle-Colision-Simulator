import math 
from functools import total_ordering


@total_ordering
class Vector:
	def __init__(self, x: float, y: float):
		self.x = x
		self.y = y
		
	def resolve(self) -> float:
		return math.sqrt(self.x ** 2 + self.y ** 2)
	
	def __eq__(self, other):
		return (self.x == other.x) and (self.y == other.y)
		
	def __le__(self, other):
		return (self.x <= other.x) or (self.y <= other.y)
