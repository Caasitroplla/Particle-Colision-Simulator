from src.particle import Particle
from math import sqrt

def quadratic_solve(a: float, b: float, c: float) -> tuple:
	# Calculate the discriminant
	discriminant = b**2 + 4 * a * c
	# Find two solutions
	solution_1 = (- b + sqrt(discriminant))/(2 * a)
	solution_2 = (- b - sqrt(discriminant))/(2 * a)
	return (solution_1, solution_2)

def collide(particle_a: Particle, particle_b: Particle):
	# Finding the particle with the largest combined vector
	print(particle_a.color)
	if particle_a.velocity_vector > particle_b.velocity_vector:
		# This means that particle a is moving faster
		# Setting relative velocity values
		x_offset = particle_b.velocity_vector.x
		y_offset = particle_b.velocity_vector.y
		x_velos = particle_a.velocity_vector.x - x_offset
		y_velos = particle_a.velocity_vector.y - y_offset
		# Setting the appropriate masses
		mass_a = particle_b.mass
		mass_b = particle_a.mass

	else:
		# This means that particle b is moving faster
		# Setting relative velocity values
		x_offset = particle_a.velocity_vector.x 
		y_offset = particle_a.velocity_vector.y
		x_velos = particle_b.velocity_vector.x - x_offset
		y_velos = particle_b.velocity_vector.y - y_offset
		# Setting the appropriate masses
		mass_a = particle_a.mass
		mass_b = particle_b.mass
		
	# Final velocity b 
	final_b_x_velos_tuple = quadratic_solve(
		((mass_b ** 2)/(2 * mass_a) + (mass_b)/(2)),
		((- mass_b**2 * x_velos)/(mass_a)),
		((-0.5 * mass_b * x_velos**2) + ((mass_b**2 * x_velos**2)/(2 * mass_a)))
	)
	
	final_b_y_velos_tuple = quadratic_solve(
		((mass_b ** 2)/(2 * mass_a) + (mass_b)/(2)),
		((- mass_b**2 * y_velos)/(mass_a)),
		((-0.5 * mass_b * y_velos**2) + ((mass_b**2 * y_velos**2)/(2 * mass_a)))
	)
	
	# Picking the correct velocity out of the pair
	if final_b_x_velos_tuple[0] == x_velos:
		final_b_x_velos = final_b_x_velos_tuple[1]
	else:
		final_b_x_velos = final_b_x_velos_tuple[0]
		
	if final_b_y_velos_tuple[0] == y_velos:
		final_b_y_velos = final_b_y_velos_tuple[1]
	else:
		final_b_y_velos = final_b_y_velos_tuple[0]
	
	# Final velocity a
	final_a_x_velos_tuple = quadratic_solve(
		(((mass_a / 2) + ((mass_a ** 2)/(2 * mass_b)))),
		(-1 * x_velos * mass_a),
		(0)
	)
	
	final_a_y_velos_tuple = quadratic_solve(
		(((mass_a / 2) + ((mass_a ** 2)/(2 * mass_b)))),
		(-1 * y_velos * mass_a),
		(0)
	)
	
	# Picking the correct velocity out of the pair
	if final_a_x_velos_tuple[0] == 0:
		final_a_x_velos = final_a_x_velos_tuple[1]
	else:
		final_a_x_velos = final_a_x_velos_tuple[0]
		
	if final_a_y_velos_tuple[0] == 0:
		final_a_y_velos = final_b_y_velos_tuple[1]
	else:
		final_a_y_velos = final_b_y_velos_tuple[0]
	
	# Undoing offsets
	final_a_x_velos += x_offset
	final_b_x_velos += x_offset
	final_a_y_velos += y_offset
	final_b_y_velos += y_offset
	
	print(final_a_x_velos)
	print(final_b_x_velos)
	print(final_a_y_velos)
	print(final_b_y_velos)
	
	# Changing the x and y velocities
	# Gets the dominant particle as decided at the start
	particle_a.velocity_vector.x = final_a_x_velos
	particle_a.velocity_vector.y = final_a_y_velos
	particle_b.velocity_vector.x = final_b_x_velos
	particle_b.velocity_vector.y = final_b_y_velos
	