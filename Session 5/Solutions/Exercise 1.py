"""Exercise 1: Ignitey Bird

Steps:
    1. Added additional attributes to Bird (lines 40-42)
    2. Added Bird.jump() and Bird.update() (lines 45-46, 53)
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

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        image_location = os.path.join("assets", "bird.png")
        self.image = pygame.image.load(image_location).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed_x = 1
        self.speed_y = 0
        self.gravity = 0.6

    def update(self):
        self.move(self.speed_x, self.speed_y)
        self.speed_y += self.gravity

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def jump(self):
        self.speed_y = -10


bird = Bird(100, 200)
birds = pygame.sprite.Group(bird)

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
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_SPACE]:
        bird.jump()
    if keys_pressed[pygame.K_LEFT]:
        pass  # Replace this line
    if keys_pressed[pygame.K_RIGHT]:
        pass  # Replace this line
    if keys_pressed[pygame.K_DOWN]:
        pass  # Replace this line

    # Mouse events
    mouse_pos = pygame.mouse.get_pos()  # Get position of mouse as a tuple representing the
    # (x, y) coordinate

    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:  # If left mouse pressed
        pass  # Replace this line
    if mouse_buttons[2]:  # If right mouse pressed
        pass  # Replace this line


    """
    UPDATE section - manipulate everything on the screen
    """
    
    birds.update()

    """
    DRAW section - make everything show up on screen
    """
    screen.fill(BLACK)  # Fill the screen with one colour

    birds.draw(screen)

    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
    clock.tick(FRAME_RATE)  # Pause the clock to always maintain FRAME_RATE frames per second
