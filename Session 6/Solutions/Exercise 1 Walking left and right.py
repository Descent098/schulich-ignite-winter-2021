"""Exercise 1: Walking to my own beat

Steps:
    1. Added Enemy.walk (Lines 62-69)
"""

# Created by Schulich Ignite Flare and students of Schulich Ignite

import os
import sys
import math
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

 
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
 
        image_location = os.path.join("assets", "enemy.png")
        self.walking_right_image = pygame.image.load(image_location).convert_alpha()
        self.walking_left_image = pygame.transform.flip(self.walking_right_image, True, False)
        self.image = self.walking_right_image
 
        self.rect = self.image.get_rect()
 
        self.rect.x = x
        self.rect.y = y
 
        self.x_speed = 3
        self.y_speed = 0
 
        self.walk_speed = 2
        self.walk_time = 2000
 
    def update(self):
        self.move(self.x_speed, self.y_speed)
        self.walk()
 
    def move(self, x_change, y_change):
        self.rect.x += x_change
        self.rect.y += y_change
 
    def walk(self):
        time = pygame.time.get_ticks()
        if time % self.walk_time < self.walk_time / 2:
            self.x_speed = self.walk_speed
            self.image = self.walking_right_image
        else:
            self.x_speed = -self.walk_speed
            self.image = self.walking_left_image

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
 
        image_location = os.path.join("assets", "player.png")
        self.image = pygame.image.load(image_location).convert_alpha()
        self.rect = self.image.get_rect()
 
        self.rect.x = x
        self.rect.y = y
 
        self.move_speed = 5
        self.x_speed = 0
        self.y_speed = 0
        self.gravity = 0.6
        
        self.can_jump = True
 
    def update(self):
        # Move the player based on whatever the x_speed and y_speed are
        self.move(self.x_speed, self.y_speed)
        
        # Make the player fall due to gravity
        self.fall()
 
    def move(self, x_change, y_change):
        self.rect.x += x_change
        self.rect.y += y_change 
        
    def teleport(self, x, y):
        self.rect.x = x
        self.rect.y = y
 
    def fall(self):
        self.y_speed += self.gravity
 
    def jump(self):
        if not self.can_jump:
            return
        self.y_speed = -15
 
    def on_platform_collide(self, platform):
        # Need to set self.rect.y explicitly to avoid having the player clip through the floor
        # Note a new bug surfaces - players jumping from the underside will teleport to the top. This is left for students to solve if interested
        self.rect.y = platform.rect.y - self.rect.height
        
        self.y_speed = 0
        self.can_jump = True

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        """
        Create a platform sprite. Note that these platforms are designed to be very wide and not very tall.
        
        It is required that the width is greater than or equal to the height. It is recommended to make height 50 or less. 
        Best visual effects are when the width is a multiple of the height.
 
        Args:
            x: The x coordinate of the platform
            y: The y coordinate of the platform
            width: The width of the platform. Must be greater than or equal to the height
            height: The height of the platform. Recommended to be 50 or less.
        """
        super().__init__()
        self.image = self.create_image(os.path.join("assets", "platform.png"), width, height)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def create_image(self, image_location, width, height):
        """
        Create the image for this sprite by using one base image and tiling it horizontally. Note that vertical tiling has not been implemented.
 
        Args:
            image_location: A string representing the file location for the image
            width: The width of the output image in pixels
            height: The height of the output image in pixels
        
        Returns:
            A surface representing the output image.
        """
        tile_image = pygame.image.load(image_location).convert_alpha()
        # The tile is a square and the height is expected to be smaller than the width
        tile_width = height
        tile_height = height
        tile_image = pygame.transform.scale(tile_image, (tile_width, tile_height))
 
        # The self.image attribute expects a Surface, so we can manually create one and "blit" the tile image onto the surface (i.e. paint an image onto a surface).
        # We use list comprehension to quickly make the blits_data list of tuples (each tuple has the tile image, and the X and Y coordinates)
        # Don't know what list comprehension is? Go look it up on the Internet. That's what all professional software engineers do ;)
        image = pygame.Surface((width, height))
        blits_data = [(tile_image, (tile_width * i, 0)) for i in range(math.ceil(width / tile_width))]
        image.blits(blits_data)
 
        return image



# Platforms sprite group
platforms = pygame.sprite.Group()
 
platforms.add(Platform(300, 600, 350, 50))
platforms.add(Platform(100, 500, 200, 50))
platforms.add(Platform(650, 450, 250, 50))
platforms.add(Platform(700, 650, 200, 25))
 
enemies = pygame.sprite.Group()
enemies.add(Enemy(750, 410))
 
# Create the player sprite and add it to the players sprite group
player = Player(400, 500)
players = pygame.sprite.Group()
players.add(player)
 
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
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
        player.jump()
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        player.move(-player.move_speed, 0)
    if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
        player.move(player.move_speed, 0)
    if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
        pass  # Now that we have platforms, there's no reason to make the player move down.
 
    # Mouse events
    mouse_pos = pygame.mouse.get_pos()  # Get position of mouse as a tuple representing the
    # (x, y) coordinate
 
    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:  # If left mouse pressed
        player.teleport(mouse_pos[0], mouse_pos[1])
    if mouse_buttons[2]:  # If right mouse pressed
        pass  # Replace this line
 
    """
    UPDATE section - manipulate everything on the screen
    """
    
    players.update()
    enemies.update()
 
    hit_platforms = pygame.sprite.spritecollide(player, platforms, False)
    for platform in hit_platforms:
        player.on_platform_collide(platform)
 
    if len(hit_platforms) == 0:
        player.can_jump = False
 
    """
    DRAW section - make everything show up on screen
    """
    screen.fill(BLACK)  # Fill the screen with one colour
    
    platforms.draw(screen)
    players.draw(screen)
    enemies.draw(screen)
 
    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
    clock.tick(FRAME_RATE)  # Pause the clock to always maintain FRAME_RATE frames per second
