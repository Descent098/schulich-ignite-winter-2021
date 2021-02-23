"""Exercise 1: Country Roads

Remember to fill out all the TODO's, you can quickly scan for them by pressing CTRL/CMD + F
"""

class Car:
    """A class representing a car with details about how far it can travel"""
    def __init__(self, gas_tank_size, fuel, litres_per_kilometre):
        self.gas_tank_size = gas_tank_size
        self.fuel = fuel
        self.litres_per_kilometre = litres_per_kilometre

    def fill_up(self):
        """Fills up the car's Fuel"""
        ... # TODO: finish function
    
    def drive(self, kilometres_driven):
        """Remove the amount of fuel, based on distance driven"""
        ... # TODO: finish function
    
    def kilometres_available(self):
        """Return the number of kilometers that the car could drive with the current amount of fuel"""
        ... # TODO: Finish Function


# Code to test
c = Car(10,9,2)
print(c.kilometres_available())
c.drive(4)
print(c.kilometres_available())
c.fill_up()
print(c.kilometres_available)
