"""Exercise 2: The Sprite is Right

Steps:
    1. All the steps in the 'Exercise 2.py file'
    2. Modified init to load one of 4 images (lines 36-39)
    3. Wrote update() so that the image moves on to the next image and handles mouse/keyboard (Lines 41-71)
    4. Called player_group.update() (line 101)
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

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() # Initialize class as a pygame sprite class
        self.image_number = 0 # The current image to load
        image_location = os.path.join("assets", "player" + str(self.image_number) + ".png") # Get image path
        self.image = pygame.image.load(image_location).convert_alpha() # Load image
        self.rect = self.image.get_rect()

    def update(self):
        """Animates the frames of the sprite"""
        frame = str(self.image_number//10)
        if self.image_number < 30: # Not yet on the tenth frame
            self.image_number += 1
        else: # Reset back to 0
            self.image_number = 0

        image_location = os.path.join("assets", "player" + frame + ".png") # Get image path
        self.image = pygame.image.load(image_location).convert_alpha() # Load image

        # Keyboard events
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP]:
            self.move(0, -5)
        if keys_pressed[pygame.K_LEFT]:
            self.move(-5, 0)
        if keys_pressed[pygame.K_RIGHT]:
            self.move(5, 0)
        if keys_pressed[pygame.K_DOWN]:
            self.move(0, 5)

        # Mouse events
        mouse_pos = pygame.mouse.get_pos()  # Get position of mouse as a tuple representing the
        # (x, y) coordinate

        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:  # If left mouse pressed
            self.teleport(mouse_pos[0], mouse_pos[1])
        if mouse_buttons[2]:  # If right mouse pressed
            self.teleport(mouse_pos[0], mouse_pos[1])

    def move(self, x_change, y_change):
        """Moves the player by the amount provided"""
        self.rect.x += x_change
        self.rect.y += y_change
    
    def teleport(self, x, y):
        """Teleports the player to the location specified (optional)"""
        self.rect.x = x
        self.rect.y = y

player_1 = Player() # Setup a player instance
player_group = pygame.sprite.Group()
player_group.add(player_1)


while True:
    """
    EVENTS section - how the code reacts when users do things
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # When user clicks the 'x' on the window, close our game
            pygame.quit()
            sys.exit()

    """
    UPDATE section - manipulate everything on the screen
    """

    player_group.update()

    """
    DRAW section - make everything show up on screen
    """
    screen.fill(BLACK)  # Fill the screen with one colour

    player_group.draw(screen)



    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
    clock.tick(FRAME_RATE)  # Pause the clock to always maintain FRAME_RATE frames per second
