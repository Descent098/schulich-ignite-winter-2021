"""Exercise 1: Adding Platforms; Create a set of moving platforms. This time using classes. I would do the version without classes first and then go from there.

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

class Game:
    """This class holds peices of information about our game"""
    def __init__(self):
        self.platforms = [] # TODO: find a way to create the platforms

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

    #TODO: Update the platforms so that they move
    for platform in game_state.platforms:
        ...


    """
    DRAW section - make everything show up on screen
    """
    screen.fill(BLACK)  # Fill the screen with one colour

    #TODO: Draw the platforms
    for platform in game_state.platforms:
        ...

    #### DRAW THINGS BEFORE THIS ####
    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
    clock.tick(FRAME_RATE)  # Pause the clock to maintain 40 frames per second