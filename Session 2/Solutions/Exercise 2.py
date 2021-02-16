"""Exercise 1: Adding Platforms; Create a set of moving platforms. This time using classes. 
I would do the version without classes first and then go from there.

NOTE: There are a few examples of different ways to solve this

Steps:
    1. Define default platforms (lines 34-42)
    2. Update platforms (lines 60-61)
    3. Draw platforms (lines 69-70)
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
RED = (255, 0, 0) # Tuple representing red color (R, G, B)


class Game:
    """This class holds peices of information about our game"""
    def __init__(self):
        # Create 5 platforms to put into self.platforms
        p1 = pygame.Rect(300, 25, 175, 40)
        p2 = pygame.Rect(500, 150, 150, 40)
        p3 = pygame.Rect(650, 250, 300, 40)
        p4 = pygame.Rect(450, 400, 250, 40)
        p5 = pygame.Rect(800, 700, 200, 40)

        # Add the 5 platforms to self.platforms
        self.platforms = [p1, p2, p3, p4, p5]

game_state = Game() # Creating a Game object that will house our platforms

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
    for platform in game_state.platforms:
        platform.x -= 5 # move platform left 5 pixels


    """
    DRAW section - make everything show up on screen
    """
    screen.fill(BLACK)  # Fill the screen with one colour

    for platform in game_state.platforms:
        pygame.draw.rect(screen, RED, platform) # Draw rectangle

    #### DRAW THINGS BEFORE THIS ####
    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
    clock.tick(FRAME_RATE)  # Pause the clock to maintain 40 frames per second