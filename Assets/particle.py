import pygame
from random import randint

def randomColor() -> tuple():
	red: int = randint(0, 255)
	green: int = randint(0, 255) 
	blue: int = randint(0, 255)
	return (red, green, blue)
	

# Import and initialise the pygame library
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:
	
	# Did the user click the window close button?
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			
	# Fill the background with white
	screen.fill(randomColor())
	
	# Draw a solid blue circle in the centre
	pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
	
	# Flip the display
	pygame.display.flip()
	
pygame.quit()