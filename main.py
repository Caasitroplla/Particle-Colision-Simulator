from json import load
import sys

from src.particle import Particle
from src.vector import Vector
from src.scene import Scene
from src.collision import collide

def main():
	# load json
	with open("particles.json", "r") as file:
		data = load(file)

	# make particles from json
	particles = []
	for item in data["particles"]:
		newParticle = Particle(item["x"], item["y"], item["x_velos"], item["y_velos"], item["mass"], color=item['color'])
		particles.append(newParticle)

	# load scene
	scene = Scene(particles)

if __name__ == '__main__':
	main()
