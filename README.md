# Particle Collision Simulator

To run a collision simply run the shell script:

```bash
#!/bin/sh
python3 main.py
```

This program calcualtes collisions as they happen **not** premptively meaning that once `100+` particles are being rendered a powerful computer is required.

To add or delete particles edit the `particles.json` this is done by creating a new row in particles like this:

```json
{
	"x" :511,
	"y" : 511,
	"x_velos" : -1,
	"y_velos" : -1,
	"mass" : 2,
	"color" : (0, 0, 0)
},
```

Where x is the x coordinate start, y is the y coordinate start and then the x and y velocity. The mass is the mass of the particle and is also proportional to the radius of the sphere.

Alternatively you can run the shell script:

```bash
#!/bin/sh
python3 particle_setup.py
```

Now you are able to use a user interface to add particles or reset the json file. The user interface only allows for the addition of particles or clearing the build folder (removes all particles) so a new simulation can be set up.

The tests module cannont be run in its state it simply stores test used in the development of the code in order for them to run move them into the same directory as the code they're testing.
