import pygame 
import sys
from pygame.locals import *
from src.particle import Particle
from math import sqrt
from src.collision import collide

def resolve(x, y):
	return sqrt(x**2 + y**2)


class Scene:
	def __init__(self, particles):
		pygame.init()
		self.screen = pygame.display.set_mode((512, 512))
		self.running = True
		self.background = (0, 0, 0)
		self.particles = particles
		self.loop()
		
	def loop(self):
		
		while self.running :
			for event in pygame.event.get():
				if event.type == QUIT:
					running = False
					
			# Collision detection
			collided_particles = []
			for primary_particle in self.particles:
				if not collided_particles.__contains__(primary_particle):
					for particle in self.particles:
						distance = resolve((primary_particle.position_vector.x - particle.position_vector.x), (primary_particle.position_vector.y - particle.position_vector.y))
						if distance <= (primary_particle.radius + particle.radius) and distance != 0:
							try:
								collide(primary_particle, particle)
							except MathDomainError:
								print("Math Domain Error(no collision was calculated)")
							collided_particles.append(particle)
							collided_particles.append(primary_particle)
							
			self.screen.fill(self.background)
			# move everything that is necessary then draw it
			for particle in self.particles:
				particle.move()
				particle.draw(self.screen)
				if not particle.side_check((512, 512)):
					# if out of bounds bye bye
					self.particles.remove(particle)
				
			pygame.display.update()
				
		pygame.quit() 
