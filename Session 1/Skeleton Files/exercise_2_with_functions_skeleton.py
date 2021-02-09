"""Exercise 2 skeleton: Create a square that bounces when it reaches any boundary of the canvas

Remember to fill out all the TODO's, you can quickly scan for them by pressing CTRL/CMD + F
"""

import sys
import os
import pygame

"""
SETUP section - preparing everything before the main loop runs
"""
pygame.init()

screen_width, screen_height = 1000, 800
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()
FRAME_RATE = 40

BLACK = (0, 0, 0)

# Setup our variables. 
RED = (255, 0, 0) # A constant with the color red as a tuple
rect = pygame.Rect(200, 100, 75, 75) # A rectangle object we can manipulate later
speed_x = 5 # The speed we are traveling in the x direction on each frame
speed_y = 5 # The speed we are traveling in the y direction on each frame

def check_collisions(): # TODO: add parameters
    # TODO: Create function that checks for colisions (there's more than 1 way to do this)
    ... # TODO: remove this when you fill in the function body

    return # TODO: Add return arguments

while True:
    """
    EVENTS section - how the code reacts when users do things
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        


    """
    UPDATE section - manipulate everything on the screen
    """
    # TODO: Update rectangle x and y coordinates if you hit the sides/top/bottom
    speed_x, speed_y = check_collisions() # TODO: add arguments


    """
    DRAW section - make everything show up on screen
    """
    screen.fill(BLACK)  # Fill the screen with one colour

    pygame.draw.rect(screen, RED, rect) # Draw the rectangle

    #### DRAW THINGS BEFORE THIS ####
    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
    clock.tick(FRAME_RATE)  # Pause the clock to maintain 40 frames per second