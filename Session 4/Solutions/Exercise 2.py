"""Exercise 2: The Sprite is Right

Steps:
    1. Made Player inherit from sprite (line 33)
    2. Added super.__init__() call and image attributes (lines 35-38)
    3. Updated move() and teleport (lines 42-43 and 47-48)
    4. Added and drew player group (lines 50-52 and 97)
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
        image_location = os.path.join("assets", "player.png") # Get image path
        self.image = pygame.image.load(image_location).convert_alpha() # Load image
        self.rect = self.image.get_rect()

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

    player_group.draw(screen)



    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
    clock.tick(FRAME_RATE)  # Pause the clock to always maintain FRAME_RATE frames per second
