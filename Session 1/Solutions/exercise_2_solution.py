"""Exercise 2 solution: Create a square that bounces when it reaches any boundary of the canvas

Steps:
    1. Define our Red color for the rectangle, then the initial values for the object, and initial x and y speeds (Lines 23-27)
    2. Update our x variable if it goes past the end or start of the screen (taking into account it's width), do the same for y (lines 48-62)
    3. Draw the rectangle (line 69)
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

# Setup our variables
RED = (255, 0, 0) # A constant with the color red as a tuple
rect = pygame.Rect(200, 100, 75, 75) # A rectangle object we can manipulate later
speed_x = 5 # The speed we are traveling in the x direction on each frame
speed_y = 5 # The speed we are traveling in the y direction on each frame

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
    # Update rect.x
    if rect.x <= 0: # Left side
        speed_x *= -1
    elif rect.x > screen_width - rect.width: # right side
        speed_x *= -1

    rect.x += speed_x # Update current x with x speed

    # Update rect.y
    if rect.y <= 0: # Top
        speed_y *= -1
    elif rect.y > screen_height - rect.height: # Bottom
        speed_y *= -1

    rect.y += speed_y # Update current y with y speed

    """
    DRAW section - make everything show up on screen
    """
    screen.fill(BLACK)  # Fill the screen with one colour

    pygame.draw.rect(screen, RED, rect) # Draw the rectangle

    #### DRAW THINGS BEFORE THIS ####
    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
    clock.tick(FRAME_RATE)  # Pause the clock to maintain 40 frames per second
