"""Exercise 1: Country Roads

Steps:
    1. Fill out Cat.__init__() (line 17)
    2. Fill out Cat.meow() (line 21)
"""

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(self.sound)

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")
    
    def meow(self):
        self.make_sound()

cat = Cat("Fluffy")
cat.make_sound()
