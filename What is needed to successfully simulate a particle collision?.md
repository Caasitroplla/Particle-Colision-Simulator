# Abstract
The aim of this report is to find out how to simulate a particle collision in two dimensions. This focuses in on the equations needed and then data to support those equations, next it moves onto the order of execution, then how to display the collision. It contains a section on how to write good and maintainable code. The report documents the development of the project in detail. The report concludes that in order to simulate a particle collision you need a velocity vector for each particle involved and its weight. Along with the two variables you’d need in order to use the equation that can be found reported below (see equation group (7)). 

If you wish to view code or run the project yourself, clone the repository: `https://github.com/Caasitroplla/Particle-Colision-Simulator`. The repository includes a guide on how to add particles. There are two branches of the project one for this report and then an expanded branch with further functionality.

+++

# Contents Page
 
{{TOC}}

# Acknowledgements

I would like to express my very great appreciation to Andy Kay, a senior software developer for his valuable work and constructive suggestions during the development of this research work.

I would also extend my thanks to E. Jones and A L Tudor of the Maths and Computer Science departments for their valuable technical support on this project.

And lastly I would like to thank Mr J Sanderson for his guidance and support whilst supervising this research.

# List of Figures

- Figure 1. Particle UML Digram.
- Figure 2. Scene UML Digram.

# List of Tables

- Table 1. Table of Terms.
- Table 2. Table of Units.
- Table 3. Extended Table of Units.

# What is needed to successfully simulate a particle collision?

# Introduction
A physics engine is a computer program that emulates real world scenarios of how collisions would realistically occur. This means you are able to use a physics engine to predict how to particles or bodies would react if they collided in the real word.

The aim of this project was to develop a two dimensional physics engine, it should have a user interface allowing for the masses and trajectories of particles to be set. At the core of the system are two main algorithms: collision detection and then resolving a collision. To store attributes and ways of viewing the different aspects of the program there are two main classes the scene and the particle. Many particles are created one for each particle the user requests, but just one scene object is used to show and simulate the environment.

This report presents what equations that enable the resolving of particle collisions. These equations have been put into a program format along with the attributes they take. Another part of the report is the displaying of the collision this has been done using Pygame.[^1] Since this project involves making a physics engine there is a section on writing maintainable code and then conceptualising the problem so it can be programmed.

# Methodology

The research carried out for this project was completed by first deconstructing the  question into multiple sub-questions. This allows each subsection of the problem to be individually researched and analysed. The sub-questions where:

1. What equations are needed to predict a collision?
2. What values or attributes have to be stored to enable the equations?
3. How do you detect a collision?
4. What is the operation order required?
5. How can you display this?
6. How do you write the code?

Having established these questions I then researched each one individually to aid in the production of the physics engine.

# Research

## What equations are needed to predict a collision?

> To help conceptualise this problem of two object / particles colliding they are referred to as particle a or object a within this chapter.

Table 1. Table of Terms.

| Term | Name |
|:---|:---:|
| $m_a$ | Object a mass. |
| $m_b$ | Object b mass. |
| $v_{ia}$ | Object a initial velocity. |
| $v_{va}$ | Object a final velocity. |
| $v_{ib}$ | Object b initial velocity. |
| $v_{vb}$ | Object b final velocity. |

> These values are only applicable for this topic: *What equations are needed to predict a collision?*

To find the equations needed firstly I researched collision physics. With the website guide, on Toppr named *Work, Energy and Power/Collisions*[Ln 3][#Toppr:Collisions], it is explained that any given particle collision is an inelastic collision meaning the total kinetic energy is conserved. Since kinetic energy = $\frac{1}{2}mv^2$ you can gain the equation.

$$\frac{1}{2}m_{a}v_{ia}{}^2 + \frac{1}{2}m_{b}v_{ib}{}^2 = \frac{1}{2}m_{a}v_{va}{}^2 + \frac{1}{2}m_{b}v_{vb}{}^2$$ 
(1)

This will allow the calculation of the final velocity after the collision has occurred. However this equations has two unknowns, both of the final velocities. In order to use this equation one velocity must be calculated. Another issue is that the particle collision simulator is planned to be in two dimension so to use this equation the vertical and horizontal components will have to be separated out. Meaning the x and y velocity will be two separate values.

One way of simplifying this equation is using relative physics. To do this it is necessary to class one particle as stationary then compare it to the other particle. This means that you have the speed of one particle relative to another.
This means which ever particle chosen as the primary one has a velocity of $0$. Meaning one of the kinetic energy formulas in the first half of equation (1) can be discarded, leaving the equation:

$$\frac{1}{2}m_{b}v_{ib}{}^2 = \frac{1}{2}m_{a}v_{va}{}^2 + \frac{1}{2}m_{b}v_{vb}{}^2$$
(2)

To obtain theses relative velocities first find the particle with the largest vertical and horizontal velocities. Once the fastest particle has been found take the slower particle's velocities away from it. The resulting velocity vector shows you the relative speed of the faster moving particle to the slower moving particle. This means the relative velocity of the slower moving particle is equal to zero.

The other equation needed to give a mathematical relationship for the final velocities come from the conservation of momentum. Since momentum can’t be created or destroyed[p. 1][#Nasa:Conservation_of_Momentum], an equation can be made using $p = mv$. Momentum is the product of mass and velocity. 

$$m_a \times v_{ia} + m_b \times v_{ib} = m_a \times v_{va} + m_b \times v_{vb}$$
(3)

As before, if relative velocities are used you can remove one half of the left hand statement since on velocity will become zero leaving:

$$m_b \times v_{ib} = m_a \times v_{va} + m_b \times v_{vb}$$
(4)

This gives two equations that both give the final velocities of both particles. Rearranging equation (4) to get one of the final velocities, it can then be substituted back into equation (2) leaving with a single equation. This equation can then be used to work out a final velocity. There will be two versions of this function to calculate horizontal and vertical velocities. Here are the two rearrange versions:

$$v_{va} = \frac{m_b \times v_{ib} - m_b \times v_{vb}}{m_a} = \frac{m_b \times (v_{ib} - v_{vb})}{m_a} \\ v_{vb} = \frac{m_b \times v_{ib} - m_a \times v_{va}}{m_b} = v_{ib} - \frac{m_a \times v_{va}}{m_b}$$
(5)

Now substitute those two equations above into equation (2):

$$\frac{1}{2}m_{b}v_{ib}{}^2 = \frac{1}{2}m_{a}(\frac{m_b \times (v_{ib} - v_{vb})}{m_a}){}^2 + \frac{1}{2}m_{b}v_{vb}{}^2 \\ \frac{1}{2}m_{b}v_{ib}{}^2 = \frac{1}{2}m_{a}v_{va}{}^2 + \frac{1}{2}m_{b}(v_{ib} - \frac{m_a \times v_{va}}{m_b}){}^2$$
(6)

For a computer to be able to calculate the $v_{va}$ and $v_{vb}$ it needs to be a single term not multiple as seen in equation (6). Here is the rearranged equation (6) it can be re-arranged into two quadratics:

$$(\frac{m_b}{2m_a} + \frac{m_b}{2}) v_{vb}{}^2 + (-\frac{m_b{}^2 \times V_{ib}}{m_a})v_{vb} + (-\frac{1}{2}m_b v_{ib}{}^2 + \frac{m_b{}^2 v_{ib}{}^2}{2m_a}) = 0 \\ (\frac{m_a}{2} + \frac{m_a{}^2}{2m_b}) v_{va}{}^2 + (-v_{ib}m_a)v_{va} = 0$$
(7)

This pair of equations are what is primarily needed to simulate a particle collision. The reason that they are quadratic is that one pair of answers will give the velocity before the collision and the other pair will give the velocity after the collision. The final velocity’s just need to be identified out of the pair.

To support this primary equation there must be a function to calculate relative velocity and another equation to then work out absolute velocity when the equation has been carried out. Another function will also have to be made for equation group (7) to be useful since it is a quadratic equation so a function must be made that is able to solve quadratics.

One shortcut that can be taken with the second equation of equation set (7). Since $v_{ia}$ is zero, one of the solutions for $v_{va}$ will also equal zero. This will allow the division of the equation by  $v_{va}$ leaving the equation:

$$(\frac{m_a}{2} + \frac{m_a{}^2}{2m_b}) v_{va}{}+ (-v_{ib}m_a) = 0$$
(8)

This means it is no longer a quadratic making it much easier to solve rearranging it leaves:

$$v_{va} = \frac{2v_{ib}m_a + 2m_a m_b v_{ib} }{m_a + m_a{}^2} = \frac{2v_{ib} + 2m_b v_{ib}}{m_a{}^2}$$
(9)

## What values or attributes have to be stored to enable the equations?

As can be seen in the table at the top of Ch. 1 *table of terms* the equation set (7) needs the following attributes about a particle:

- Initial velocity, $v_i$
- Mass, $m$

This means for every particle class there must be two attributes of initial velocity and mass. To keep them in standard format I read an article by NIST on SI Units[p. 1][#NIST:SI_Units] which outlines the units to be used for every measure. The applicable section is:

Table 2. Table of Units.

| Unit Name | Base SI Unit | Full Name |
|:---|:---|:---|
| Velocity | $ms^{-2}$ | Meters per second squared. |
| Mass | $kg$ |  Kilogram. |

This shows that when entering values for mass and velocity they must be in these units or they need to be converted. When storing velocities there must be one for horizontal velocity (x) and vertical velocity (y) as stated in chapter (1).

## How do you detect a collision?

To detect a collision of two circles in two dimensions this developer article[Ch. 2][#MDN_Web_Docs:2D_collision_detection] shows how you can use the distance between centre coordinates, and the combined radiuses of the two circle to detect collisions. If the shortest distance between the two centres is less than or equal to the combined radiuses than a collision has occurred. To find the shortest distance between two points the Pythagorean theorem ($a^2 + b^2 = c^2$) has to be used. This gives the equation:

$$distance = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2} \\ distance > (r_1 + r_2)$$
(10)

Where $(x_1, y_1)$ are the coordinates of the first object and $(x_2, y_2)$ are the coordinates of the second object. $r_1$ is the radius of the first object and $r_2$ is the radius of the second object.

This also means that each particle class must contain the object's position and radius. Using the research from chapter (2) I can add the new attributes to the table of units:

Table 3. Extension 1 to Table of Units

| Unit Name | Base SI Unit | Full Name |
|:---|:---|:---|
| Position | $m$ | Meters (from origin). |
| Radius | $m$ |  Meters. |

When storing the position it must have two components vertical (y) and horizontal (x).

To optimise the finding of collisions this chat forum comment[Cmnt. 1][#StackExchange:Collision_Detection] states that you should split up the scene. If you divide the screen up into multiple sub sections then it lessens the complexity. This improvement in efficiency can be quantified, as if you didn’t divide up the scene you would check every object against every other object this gives a complexity of $o(n^2)$. If you split the view in half you only compare objects in each half of screen, giving the complexity $o(n \log n)$ which is a lesser complexity. The more you then divide the scene up the lower the complexity up until a certain point. This point is where you have that many section split up that it takes more time to process the dividing up than to checking collisions. In the comment[Cmnt. 1][#StackExchange:Collision_Detection] it is suggested that you divide a scene up into quarters. Dividing the scene into quarters means that scene dimensions should be divisible by four. To ensure this and any further divides are doable I planned on using base two values for the scene dimensions for example $2^{9} = 512$ Pixels.

## How must the logic flow?

The execution order of all the equations and functions in previous chapter is important since each equation is either triggered from another or passes data forward. To calculate the execution order I consulted a professional programmer, Andy Kay. After looking through my research are notes we concurred the order in which things must be executed is:

1. Detect a collision
2. Calculate relative velocities
3. Calculate resultant velocities
	- Solve quadratic equation
	- Find final velocities
4. Calculate absolute velocities
5. Set new absolute velocities

Following this execution order means that in every step every input value is calculated and is happening when it is supposed to.

## How can you display this?

This project is going to be made using Python[#Python] it is necessary to use a Python compatible UI package. A popular UI package I’ve found is Pygame[#Pygame] which is a ‘set of python modules designed for writing video games’. The plan is to repurpose some of these modules which allow the rendering of differently coloured spheres within a scene.

From the Python Pygame Introduction [Tutorials: Introduction to Pygame][#Pygame] you can see that the Modules that will be necessary in this project are:

- display
- draw
- event
- key

The display module will give control of the display window and scene. The draw module provides the ability to draw shapes onto the scene including circles. The event module will provide a queue data structure to handle the processing of collisions. The key module allows input from the keyboard useful for an escape button to stop the simulation. To get these modules in the python script it says to use the line of code:

```
from pygame import display, draw, event, key
```

Each of these imported modules is in the form of a class so their methods can be accessed in the standard way. To see a list of these methods view the Pygame documentation [Docs][#Pygame].

## How do you write the code?

To keep the code consistent throughout any project it is standard practice to use  style guide. A commonly used style guide in Python is PEP8[#PEP8], using a style guide within this project will mean it can be easily maintained and understood by other developers. The main ideas about how to format your code whilst using PEP8 are:

- All variables must be lower case
- When variables are multi-word, use underscores to separate words
- Object names must be one word and start with a capital
- All lines must be shorter than 79 character
- When writing mathematical equations over multiple lines the operator comes before the variable name in the line
- 2 blank lines before every class and single blank line before every function

Earlier, within the equation set (7) raised a challenge of having to solve a quadratic equation. To solve a quadratic equation within a computer program this article[P. 1][#GeeksForGeeks:QuadraticEquation] by geeks for geeks shows how to solve quadratic equations. To solve quadratic equations it uses another equation:

$$\frac{-b {}^+_- \sqrt{b^2 - 4ac}}{2 a}$$
(11)

The ${}^+_-$ means that this equation will be performed twice, once with the $+$ and once with the $-$. This will give the two results to the equation. Putting this formula in code format means it can be simplified since the $b^2 - 4ac$ component is used twice in both calculations, it can be pre-calculated. Pre-calculating this component decreases the execution time of the program since less calculations are carried out. Leaving the code as seen below:

```python
from math import sqrt 

def quadratic_equation(a, b, c):
	discriminant = b**2 + 4 * a * c
	solution_1 = (-b + sqrt(discriminant))/(2 * a)
	solution_2 = (-b + sqrt(discriminant))/(2 * a)
	return (solution_1, solution_2)
```

This function will take the three inputs the ‘a’, ‘b’ and ‘c’, the coefficients of a quadratic equation, that is in the form $ax^2 + bx + c = 0$ and then return a tuple containing the two solutions.

Another part of the project is the modelling of a particle in computer code. To model particle within the program we will make a class to represent it. To show the design of this class here is a industry standard UML diagram:

![Figure 1. Particle UML Digram](Images/Particle_Class_EPQ.png)

In the top section of the particle class you can see the attributes as discussed earlier. The method listed named ‘move’ is to be ran every refresh of the engine, this will change the position of the particle by the velocity vector. Using a class to model this particle means as many particles as necessary can be made from this template.

The other main part of the project is the modelling of the scene or atmosphere in which the collision occurs. To model the scene another class will be used named 'Scene', it will mainly contain attributes for the imported Scene model from Pygame. To show the design of this Scene class here is another UML diagram:

![Figure 2. Scene UML Diagram](Images/Scene_Class_EQP.png)

The method named loop defined in the scene class is the function that once ran will carry out the collision, a while loop will operate until the user quits where particles are moved then redrawn as well as collisions being detected and dealt with.

One more part of the project is the collision algorithm, this will take the form of a procedure, it will take in two particles that are confirmed to have of collided. Using the execution structure defined in Ch. 4 *How must the logic flow?* this collision algorithm procedure must follow these five main steps:

1. Find fastest particle
2. Find the relative velocity of the faster particle to the slower particle
3. Run equation set (7) using the masses and relative velocities of the two particles
4. Find which result out of the two given from the quadratic equation is valid
5. Set absolute particle velocities

The procedure should execute all these steps than edit the particle attributes of velocity in x and y direction. The procedure doesn’t need to return any values which is what makes it a procedure. Since this is an integral part of the program, to be sure that it works a method of testing called unit testing will be employed. The official Python unit testing framework[P. 1][#Python:Unit_Testing] explains how to make unit tests, in Appendix (11. Collision Procedure Unit Testing) you can see the tests designed using the unit test frame work.

# Project Development

## Part 1 Creating the Particle

To begin the development of the particle collision simulator, we first need to create the Particle class. Using Figure 1. Particle UML Digram, it is clear that firstly the vector object must be created. This vector object is going to be situated inside the `src` code folder of the project in its own separate file. It will have two variables when instantiated of an x and y then will have a resolve vector method that returns the distance between the two points or combined velocity depending on implementation using Pythagoras theorem as seen in Ch. 3. The code can be seen in appendix(12. Vector Class)

After having made this vector class it is now possible to create the particle class following Figure 1. Particle UML Digram. This Particle object will also be stored in a separate file with the `src` folder. The code can be seen in appendix (13. Particle Class).

The move procedure of the particle operates by incrementing the x and y position by the x and y velocities moving by a number of pixels. The `side_check` function takes in a parameter of the screen size, this allows it to see if it within the boundaries of the screen, if it is within the scene then it returns true otherwise it returns false. This will then be used by the Scene object to determine whether it needs to be deleted or not. The `draw` function draws a circle using Pygame using the particle attributes of position, radius  and colour. The `__eq__`  (standing for equate) can see if the particle is the same as another particle returning a boolean for if it is the same or not.

## Part 2 Creating the Collision procedure

The collision procedure has to follow the steps described in chapter (6) in order to calculate the resultant velocities. To accommodate the `collide` procedure it is necessary that there is a the quadratic equation solver. This can bee seen here:

```python
from math import sqrt

def quadratic_solve(a: float, b: float, c: float) -> tuple:
	# Calculate the discriminant
	discriminant = b**2 + 4*a*c
	# Find two solutions
	solution_1 = (-b + sqrt(discriminant))/(2 * a)
	solution_2 = (-b - sqrt(discriminant))/(2 * a)
	return (solution_1, solution_2)
```

With this function programmed it is now possible to create the `collide` procedure as can be seen in appendix (14. Collide Procedure). To enable this function extensions had to be made for existing classes, these modifications are: 

The vector class has the `@total_ordering` statement before it then two extra methods (the final version of the particle can be seen in appendix(12. Vector Class)):

```python
	def __eq__(self, other):
		return (self.x == other.x) and (self.y == other.y)
		
	def __le__(self, other):
		return (self.x <= other.x) or (self.y <= other.y)
``` 

This will allow the vectors to be compared with operators such as `<` or `<=` which allows the `collide` function to determine the faster moving particle. With these modifications, the tests that were designed in chapter (6) seen in appendix (11. Collision Procedure Unit Testing) ran successfully and the collision algorithm now works.

## Part 3 Creating the scene

The scene object is going to take one input of the particles it is going to display, which is stored in the `self.particles` array. Following Figure 2. Scene UML Digram the Scene can be seen in appendix (15. Scene Class). 

The `__init__` function instantiates the scene creating it then it calls the `loop` function which runs the simulation. The loop function first checks to see if the user has requested to stop the simulation. Next, the function checks for any collisions, once a particle has been in a collision it can no longer collide in that refresh so its appended to a black list called `collided_particles`. Finally it goes through each particle first allowing it to move then drawing it.

## Part 4 Making everything interface

To allow particles to be entered a json (java script object notation) file will be used to store the attributes about a particle, which are then loaded into the program. To load this data then call the Scene class is the job of the main function which is the top level of the program. It can be seen in appendix (16. Main function). It first loads the data from json file using the load function imported from json package then creates particles from the file, then creates the scene passing it the created particles.

# Conclusion

> In order to successfully simulate a particle collision the following is needed:

Firstly, the equation set (7) is needed this allows the resultant velocities in the x and y direction to be calculated when a collision occurs. These equations only work with relative velocities, so one object (object a for these equations) must have a velocity of (0, 0). The equation can be seen here:

$$(\frac{m_b}{2m_a} + \frac{m_b}{2}) v_{vb}{}^2 + (-\frac{m_b{}^2 \times V_{ib}}{m_a})v_{vb} + (-\frac{1}{2}m_b v_{ib}{}^2 + \frac{m_b{}^2 v_{ib}{}^2}{2m_a}) = 0 \\ (\frac{m_a}{2} + \frac{m_a{}^2}{2m_b}) v_{va}{}^2 + (-v_{ib}m_a)v_{va} = 0$$
(7)

These two equations must be run for each particle in both x and y directions then choose the outcome of the quadratic that not the original value.

To enable this equation each particle must have the following attributes:

- mass
- velocity x and y

This allows the equation to run since it takes a mass and velocity for each particle and the finds the final velocity.

Secondly, to simulate the collision there are two parts: detecting the collision and displaying the collision.

To simulate the collision the particle need to have a position, radius and colour allowing it to be drawn. The particles also need to be able to move so each refresh the particles must be moved by their velocity vector.

To detect the collision the shortest distance between to centre's of spheres must be found then compared to the total of the two radii. If the shortest distance between centre's if less then the combined radii then a collision has occurred.

Thus, we are able to conclude that in order to simulate a particle collision you need a set of equations and then 6 variables stored about each particle being simulated.

# Appendix
## Collision Procedure Unit Testing

Here are two example instances of the particles that the equation will take:

```
Particle 1, x_velocity = 1, y_velocity = 1, mass = 2
Particle 2, x_velocity = 3, y_velocity = 2, mass = 1
```

Here are what the calculated relative velocity after the collision should be:

```
Particle 1, x_velocity = 2, y_velocity = 1, mass = 2
Particle 2, x_velocity = -0.666, y_velocity = -0.333, mass = 1
```

Here are what the calculated absolute velocities after the collision should be:

```
Particle 1, x_velocity = 3, y_velocity = 2, mass =2
Particle 2, x_velocity = 0.333, y_velocity = 0.666, mass = 1
```

Therefore, the unit test object should look like this:

```python
import unittest
from particle import Particle
from collision import collide


class Test_Particle_Collision_Procedure(unitest.TestCase):
	def test_particle_collision_procedure(self):
		actual_a = Particle(x: 1, y: 1, mass: 2)
		actual_b = Particle(x: 3, y: 2, mass: 1)
		
		collide(actual_a, actual_b)
		
		expected_a = Particle(x: 3, y: 2, mass: 2)
		expected_b = Particle(x: 0.333, y: 0.666, mass: 1)
		
		self.assertEqual(actual_a, expected_a)
		self.assertEqual(actual_b, expected_b)
```

## Vector Class

```python
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
```

## Particle Class 

```python
from src.vector import Vector
import pygame
from random import randint

# So particles can be coloured : just makes a random color
def random_color() -> tuple:
	red = randint(0, 255)
	green = randint(0, 255)
	blue = randint(0, 255)
	return (red, green, blue)


class Particle:
	def __init__(self, x_pos, y_pos, x_vel, y_vel, mass):
		# Creating position and velocity vector
		self.position_vector = Vector(x_pos, y_pos)
		self.velocity_vector = Vector(x_vel, y_vel)
		# Setting the particles mass
		self.mass = mass
		# Settings a radius
		self.radius = mass
		self.color = random_color()
		
	def move(self):
		# Incrementing the position vector by the velocity for x and y
		self.position_vector.x += self.velocity_vector.x
		self.position_vector.y += self.velocity_vector.y
		
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
```

## Collide Procedure

```python
from src.particle import Particle

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
	particle_b.velocity_vector.y = final_b_y_velos```
```

## Scene Class

```python
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
		collided_particles = []
		while self.running :
			for event in pygame.event.get():
				if event.type == QUIT:
					running = False
					
			# Collision detection
			for primary_particle in self.particles:
				if not collided_particles.__contains__(primary_particle):
					for particle in self.particles:
						distance = resolve((primary_particle.position_vector.x - particle.position_vector.x), (primary_particle.position_vector.y - particle.position_vector.y))
						if distance <= (primary_particle.radius + particle.radius) and distance != 0:
							collide(primary_particle, particle)
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
```

## Main function

```python
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
```

## particles.json

Default data for `particles.json` :

```json
{
	"particles" : [
		{
			"x" : 1,
			"y" : 1,
			"x_velos" : 1,
			"y_velos" : 1,
			"mass" : 2
		},
		{
			"x" :511,
			"y" : 511,
			"x_velos" : -1,
			"y_velos" : -1,
			"mass" : 2
		},
		{
			"x" : 215,
			"y" : 215,
			"x_velos" : 0,
			"y_velos" : 0,
			"mass" : 2
		}
	]
}
```

# Glossary
<!-- This is an example of how the glossary should look: 
The glossary should be in alphabetical order and look like this:
**term.** Definition of term. -->

**attribute.** A data item or variable that is a belonging to a class.

**class.** A template defining the attributes and methods that can be used to create a type of data known as an object.

**constant.** A data item that, once declared, retains the same value for the entire duration of the program run.

**dunder method.** A function or procedure that that is inbuilt in python that is being overwritten. It is normally defined by a double underscore before and after the name.

**encapsulation.** A method of maintaining data integrity by only allowing class methods to access data in an object’s attributes.

**functions.** A subroutine that can be called to perform a task or operation and always returns a value. They can be called in an expression or be assigned to a variable.

**inheritance.** The concept of subclassing inheriting the methods and attributes of its parent class (a.k.a. its super class)

**instantiation.** The creation of an object from a class.

**object oriented programming.** A programming paradigm where the system is viewed as a set of objects, each with their own data (attributes) and procedures (methods), that can interact with each other. All processing is done by the objects.

**objects.** An instance of a class. The behavior of this data item depends on how its attributes were defined.

**package.** A collection of pre-programmed code that can be used to perform tasks.

**procedures.** A subroutine that can be called by simply writing its name in the code. Procedures do not have to return values in a program.

**tuple.** A data item that is used to store multiple items in a single variable.

**variable.** A data item that, once declared, can be used as a short term memory container for a temporary value that may change over the duration of the program run.

# Bibliography

[^1]: A package for Python that enables on screen graphics.

[#Toppr:Collisions]: Toppr. *https://www.toppr.com/guides/physics/work-energy-and-power/collisions/*. 2021.

[#Nasa:Conservation_of_Momentum]: NASA. *https://www.grc.nasa.gov/www/k-12/airplane/conmo.html*. 2021.

[#NIST:SI_Units]: NIST. U.S. Department of Commerce. *https://www.nist.gov/pml/weights-and-measures/metric-si/si-units*. 2021.

[#StackExchange:Collision_Detection]: Stack exchange. Basweasel. Comment 2. *https://gamedev.stackexchange.com/questions/76185/how-to-optimize-collision-detection/76201*. Jun 6 ‘14 at 0:08.

[#MDN_Web_Docs:2D_collision_detection]: MDN Web Docs. Mozilla. *‌https://developer.mozilla.org/en-US/docs/Games/Techniques/2D_collision_detection*. 2021.

[#Python]: Python. Python software foundation. *https://www.python.org*. 2021.

[#Pygame]: Pygame. *‌pygame.org*. 2021.

[#PEP8]: PEP8. Kenneth Reitz. *‌pep8.org*. 2021

[#GeeksForGeeks:QuadraticEquation]: GeeksForGeeks. Simran Bhandari. *https://www.geeksforgeeks.org/python-program-to-solve-quadratic-equation/*. 2021.

[#Python:Unit_Testing]: Python Unit testing framework. Python software foundation. *https://docs.python.org/3/library/unittest.html*. 2021.


