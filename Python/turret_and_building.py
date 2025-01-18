import pygame

class Turret_and_building:
    def __init__(self):
        self.health
        self.armor
        self.magic_resist
        self.strength
        self.magic_power
        self.critical_rate
        self.critical_damage
        self.production
    def __del__(self):
        print(f"{self} has been deleted")
        
class Nexus(Turret_and_building):
    def __init__(self):
        self.health = 1000
        self.armor = 100
        self.magic_resist = 100
        self.strength = 100
        self.magic_power = 100
        self.critical_rate = 0.25
        self.critical_damage = 1.5
        self.production = 10
    def __del__(self):
        print(f"{self} has been deleted")
        
class Magic_Tower(Turret_and_building):
    def __init__(self):
        self.health = 250
        self.armor = 50
        self.magic_resist = 50
        self.strength = 0
        self.magic_power = 100
        self.critical_rate = 0.1
        self.critical_damage = 1
    def __del__(self):
        print(f"{self} has been deleted")
        
class Physical_Tower(Turret_and_building):
    def __init__(self):
        self.health = 250
        self.armor = 50
        self.magic_resist = 50
        self.strength = 100
        self.magic_power = 0
        self.critical_rate = 0.1
        self.critical_damage = 1
    def __del__(self):
        print(f"{self} has been deleted")
        
class Gold_Mine(Turret_and_building):
    def __init__(self):
        self.health = 250
        self.armor = 50
        self.magic_resist = 50
        self.production = 5
    def __del__(self):
        print(f"{self} has been deleted")
        
class Minerals_Mine(Turret_and_building):
    def __init__(self):
        self.health = 250
        self.armor = 50
        self.magic_resist = 50
        self.production = 5
    def __del__(self):
        print(f"{self} has been deleted")