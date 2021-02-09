"""Exercise 2 solution: Create a square that bounces when it reaches any boundary of the canvas

Keep in mind this is just one solution, there are a few ways to do this

Steps:
    1. Added rectangle, x_speed, y_speed arguments(Line 37)
    2. Added docstring; we didn't talk about these but it's just an explanation of what the function does (Line 38)
    3. Take the soltion from exercise_2_solution.py and put it in check_collisions (Lines 39-54)
    4. Added return values (line 55)

Why:
    - Creating a general function means you can now add another rectangle with as little as 4 lines vs 22 lines without a function
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

def check_collisions(rectangle, x_speed, y_speed):
    """Takes in a rectangle, and if it collides with a boundary"""
    # Update rectangle.x
    if rectangle.x <= 0: # Left side
        x_speed *= -1
    elif rectangle.x > screen_width - rectangle.width: # right side
        x_speed *= -1
    
    rectangle.x += x_speed

    # Update rectangle.y
    if rectangle.y <= 0: # Top
        y_speed *= -1
    elif rectangle.y > screen_height - rectangle.height: # Bottom
        y_speed *= -1
    
    rectangle.y += y_speed

    return x_speed, y_speed

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
    # Reset speed_x and speed_y to new values
    speed_x, speed_y = check_collisions(rect, speed_x, speed_y) 


    """
    DRAW section - make everything show up on screen
    """
    screen.fill(BLACK)  # Fill the screen with one colour

    pygame.draw.rect(screen, RED, rect) # Draw rectangle

    #### DRAW THINGS BEFORE THIS ####
    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
    clock.tick(FRAME_RATE)  # Pause the clock to maintain 40 frames per second