"""Exercise 2: The Sprite is Right

Remember to fill out all the TODO's, you can quickly scan for them by pressing CTRL/CMD + F
"""

import sys
import os
import pygame

"""
SETUP section - preparing everything before the main loop runs
"""
pygame.init()

# Global constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
FRAME_RATE = 60

# Useful colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Creating the screen and the clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.set_alpha(0)  # Make alpha bits transparent
clock = pygame.time.Clock()

class Player: # TODO: Make inherit from pygame.sprite.Sprite
    def __init__(self, x, y):
        #TODO: Make necessary changes to __init__
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.colour = (255, 0, 0 ) # Red

    def move(self, x_change, y_change):
        """Moves the player by the amount provided"""
        #TODO: make necessary changes
        self.x += x_change
        self.y += y_change
    
    def teleport(self, x, y):
        """Teleports the player to the location specified (optional)"""
        #TODO: make necessary changes
        self.x = x
        self.y = y

player_1 = Player() # Setup a player instance
#TODO: setup a sprite group


while True:
    """
    EVENTS section - how the code reacts when users do things
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # When user clicks the 'x' on the window, close our game
            pygame.quit()
            sys.exit()

    # Keyboard events
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP]:
        player_1.move(0, -5)
    if keys_pressed[pygame.K_LEFT]:
        player_1.move(-5, 0)
    if keys_pressed[pygame.K_RIGHT]:
        player_1.move(5, 0)
    if keys_pressed[pygame.K_DOWN]:
        player_1.move(0, 5)

    # Mouse events
    mouse_pos = pygame.mouse.get_pos()  # Get position of mouse as a tuple representing the
    # (x, y) coordinate

    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:  # If left mouse pressed
        player_1.teleport(mouse_pos[0], mouse_pos[1])
    if mouse_buttons[2]:  # If right mouse pressed
        player_1.teleport(mouse_pos[0], mouse_pos[1])



    """
    UPDATE section - manipulate everything on the screen
    """
    


    """
    DRAW section - make everything show up on screen
    """
    screen.fill(BLACK)  # Fill the screen with one colour

    #TODO: make necessary changes
    player_1_rect = pygame.Rect(player_1.x, player_1.y, player_1.width, player_1.height)
    pygame.draw.rect(screen, player_1.colour, player_1_rect)



    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
    clock.tick(FRAME_RATE)  # Pause the clock to always maintain FRAME_RATE frames per second
