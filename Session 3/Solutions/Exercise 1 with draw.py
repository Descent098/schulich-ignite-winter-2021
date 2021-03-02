"""Exercise 1: Country Roads

Steps:
    1. Fill out fill_up() so that it fills the fuel level to the gas tank size (line 18)
    2. Fill out drive() so that it removes the amount of fuel it should for how far you drove(line 22)
    3. Fill out kilometres_available so that it returns the amount of kilometers left based on the fuel economy(line 26)

Bonus:
    1. Add draw function (lines 55-57)
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

class Car:
    """A class representing a car with details about how far it can travel"""
    def __init__(self, gas_tank_size, fuel, litres_per_kilometre):
        self.gas_tank_size = gas_tank_size
        self.fuel = fuel
        self.litres_per_kilometre = litres_per_kilometre

    def fill_up(self):
        """Fills up the car's Fuel"""
        self.fuel = self.gas_tank_size
    
    def drive(self, kilometres_driven:float):
        """Remove the amount of fuel, based on distance driven"""
        self.fuel -= (self.litres_per_kilometre * kilometres_driven)
    
    def kilometres_available(self) -> float:
        """Return the number of kilometers that the car could drive with the current amount of fuel"""
        return self.fuel / self.litres_per_kilometre

    def draw(self) -> pygame.Rect:
        """Return a rect object representing the fuel size"""
        return pygame.Rect(0, 0, (self.fuel / self.gas_tank_size)* 1000, 800)

# Code to test
c = Car(10,9,2)


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
        pass  # Replace this line
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
    c.drive(1)
    if c.fuel < 1:
        c.fill_up()


    """
    DRAW section - make everything show up on screen
    """
    screen.fill((122,122,122))  # Fill the screen with one colour

    fuel_level = c.draw()
    pygame.draw.rect(screen, BLACK, fuel_level)

    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
    clock.tick(FRAME_RATE)  # Pause the clock to always maintain FRAME_RATE frames per second




