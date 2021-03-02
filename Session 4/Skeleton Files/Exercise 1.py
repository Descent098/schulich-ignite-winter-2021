"""Exercise 1: Meower Power

Remember to fill out all the TODO's, you can quickly scan for them by pressing CTRL/CMD + F
"""

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(self.sound)

class Cat(Animal):
    #TODO: finish class
    ...

    def meow():
        # TODO: Finish meow function
        ...

cat = Cat("Fluffy")
cat.make_sound()
