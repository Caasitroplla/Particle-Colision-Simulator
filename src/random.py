import random

from src.particle import Particle

# Create a particle with completely random values
def randomParticle() -> Particle:
    # Randomize position
    x = random.randint(0, 512)
    y = random.randint(0, 512)

    # Randomize velocity
    x_velos = random.randint(-10, 10)
    y_velos = random.randint(-10, 10)

    # Randomize mass
    mass = random.randint(1, 10)

    # Randomize color
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    return Particle(x, y, x_velos, y_velos, mass, color)