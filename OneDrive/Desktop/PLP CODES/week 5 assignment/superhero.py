# Base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"I am {self.name}, protector of {self.city}! 🏙️")

    def use_power(self):
        print(f"{self.name} uses {self.power}! ⚡")

# Child class (Inheritance + Polymorphism)
class FlyingHero(Superhero):
    def use_power(self):
        print(f"{self.name} takes off into the sky using {self.power}! 🦸‍♂️✈️")

class StrongHero(Superhero):
    def use_power(self):
        print(f"{self.name} smashes the ground with {self.power}! 💪💥")

# Creating objects
hero1 = FlyingHero("SkyGuard", "Flight", "Metropolis")
hero2 = StrongHero("Titan", "Super Strength", "Gotham")

# Testing methods
hero1.introduce()
hero1.use_power()

hero2.introduce()
hero2.use_power()
