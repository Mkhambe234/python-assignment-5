# Base class
class Animal:
    def move(self):
        print("This animal moves in some way")

# Subclasses with their own move() behavior
class Dog(Animal):
    def move(self):
        print("Running ")

class Bird(Animal):
    def move(self):
        print("Flying ")

class Fish(Animal):
    def move(self):
        print("Swimming ")

class Snake(Animal):
    def move(self):
        print("Slithering ")

# Polymorphism in action
animals = [Dog(), Bird(), Fish(), Snake()]

print("Animals moving in different ways:\n")
for animal in animals:
    animal.move()
