"""Exercise 1: Pixel Forest, use the tree class to draw some trees

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
BROWN = (143, 90, 4)
GREEN = (13, 168, 55)

# Copied from https://raw.githubusercontent.com/Schulich-Ignite/flare/main/session2/tree.py
class Tree:
    """A class to easily draw a tree with some leaves"""
    def __init__(self):
        self.trunk_x = 0
        self.trunk_y = 0
        self.trunk_width = 25
        self.trunk_height = 190
        self.leaves_x = 0
        self.leaves_y = 0
        self.leaves_size = 175
        self.leaves_color = GREEN  # Note American spelling of "colour". You can edit this to "self.leaves_colour" if you prefer Canadian style

    def draw(self):
        """A function that draws the tree

        Example
        -------
        ```python
        ... # Other pygame code
        t = Tree()

        t.draw() # Put this in the DRAW step

        ... # Other pygame code
        ```
        """
        trunk = pygame.Rect(self.trunk_x, self.trunk_y, self.trunk_width, self.trunk_height)
        pygame.draw.rect(screen, BROWN, trunk)

        # Setup leaf position relative to trunk
        self.leaves_x = self.trunk_x - self.trunk_width
        self.leaves_y = self.trunk_y

        leaves = pygame.Rect(self.leaves_x, self.leaves_y, self.leaves_size//2, self.leaves_size//2)
        pygame.draw.rect(screen, self.leaves_color, leaves)

# TODO: Setup the tree HINT need the trunk x and trunk y

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

    """
    DRAW section - make everything show up on screen
    """
    screen.fill(BLACK)  # Fill the screen with one colour

    # TODO: Draw the tree

    #### DRAW THINGS BEFORE THIS ####
    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
    clock.tick(FRAME_RATE)  # Pause the clock to maintain 40 frames per second