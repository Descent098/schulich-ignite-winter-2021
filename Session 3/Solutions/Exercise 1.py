"""Exercise 1: Country Roads

Steps:
    1. Fill out fill_up() so that it fills the fuel level to the gas tank size (line 18)
    2. Fill out drive() so that it removes the amount of fuel it should for how far you drove(line 22)
    3. Fill out kilometres_available so that it returns the amount of kilometers left based on the fuel economy(line 26)
"""

class Car:
    """A class representing a car with details about how far it can travel"""
    def __init__(self, gas_tank_size, fuel, litres_per_kilometre):
        self.gas_tank_size = gas_tank_size
        self.fuel = fuel
        self.litres_per_kilometre = litres_per_kilometre

    def fill_up(self):
        """Fills up the car's Fuel"""
        self.fuel = self.gas_tank_size
    
    def drive(self, kilometres_driven):
        """Remove the amount of fuel, based on distance driven"""
        self.fuel -= (self.litres_per_kilometre * kilometres_driven)
    
    def kilometres_available(self):
        """Return the number of kilometers that the car could drive with the current amount of fuel"""
        return self.fuel * self.litres_per_kilometre


# Code to test
c = Car(10,9,2)
print(c.kilometres_available())
c.drive(4)
print(c.kilometres_available())
c.fill_up()
print(c.kilometres_available)
