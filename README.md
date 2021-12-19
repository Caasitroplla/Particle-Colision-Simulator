# Particle Collision Simulator

To run a collision simply run the shell script:

```bash
#!/bin/sh
python3 main.py
```

To add or delete particles edit the `particles.json` this is done by creating a new row in particles like this:

```json
{
	"x" :511,
	"y" : 511,
	"x_velos" : -1,
	"y_velos" : -1,
	"mass" : 2
},
```

Where x is the x coordinate start, y is the y coordinate start and then the x and y velocity. The mass is the mass of the particle and is also proportional to the radius of the sphere.