# Polymorphism Example

class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

class Dog:
    def move(self):
        print("Running 🐕")

class Fish:
    def move(self):
        print("Swimming 🐟")

# List of objects
objects = [Car(), Plane(), Dog(), Fish()]

# Polymorphism in action
for obj in objects:
    obj.move()
