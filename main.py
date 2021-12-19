from src.particle import Particle
from src.vector import Vector
from src.scene import Scene
from src.collision import collide
from json import load

def main():
	# load json
	with open("particles.json", "r") as file:
		data = load(file)
		print(data)
	
	# make particles from json
	particles = []
	for item in data["particles"]:
		newParticle = Particle(item["x"], item["y"], item["x_velos"], item["y_velos"], item["mass"])
		particles.append(newParticle)
	
	# load scene
	scene = Scene(particles)	

if __name__ == '__main__':
	main()