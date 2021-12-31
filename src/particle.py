from vector import Vector
import pygame
from random import randint


def random_color() -> tuple:
	red = randint(0, 255)
	green = randint(0, 255)
	blue = randint(0, 255)
	return (red, green, blue)


class Particle:
	def __init__(
		self, 
		x_pos, 
		y_pos, 
		x_vel, 
		y_vel, 
		mass, 
		color = random_color()
	):
	
		# Creating position and velocity vector
		self.position_vector = Vector(x_pos, y_pos)
		self.velocity_vector = Vector(x_vel, y_vel)
		# Setting the particles mass
		self.mass = mass
		# Settings a radius
		self.radius = mass
		self.color = color
		
	def move(self):
		# Incrementing the position vector by the velocity for x and y
		self.position_vector.x += (self.velocity_vector.x / 10)
		self.position_vector.y += (self.velocity_vector.y / 10)
		
	def side_check(self, screen_size: tuple) -> bool:
		return (screen_size[0] >= self.position_vector.x 
			and 0 <= self.position_vector.x
			and screen_size[1] >= self.position_vector.y
			and 0 <= self.position_vector.y)
		
	def draw(self, scene):
		#circle(Surface, color, center, radius, width)
		pygame.draw.circle(scene, self.color, (self.position_vector.x, self.position_vector.y), self.radius, self.radius)
		
	def __del__(self):
		# This deletes the particle removing it from screen and memory
		pass
		
	def __eq__(self, other):
		return ((self.position_vector == other.position_vector) 
			and (self.velocity_vector == other.velocity_vector) 
			and (self.mass == other.mass))
			