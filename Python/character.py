import pygame


class Character:
    def __init__(self):
        self.health
        self.armor
        self.magic_resist
        self.speed
        self.strength
        self.magic_power
        self.critical_rate
        self.critical_damage
    def __del__(self):
        print(f"{self} has been deleted")
        
class Player_engineer(Character):
    def __init__(self):
        self.health = 100
        self.armor = 30
        self.magic_resist = 30
        self.speed = 60
        self.strength = 10
        self.magic_power = 10
        self.critical_rate = 0.25
        self.critical_damage = 0.5
        
class base_ennemi(Character):
    def __init__(self):
        self.health = 30
        self.armor = 10
        self.magic_resist = 10
        self.speed = 50
        self.strength = 10
        self.magic_power = 10
        self.critical_rate = 0
        self.critical_damage = 0
        
class medium_ennemi(Character):
    def __init__(self):
        self.health = 70
        self.armor = 25
        self.magic_resist = 25
        self.speed = 35
        self.strength = 25
        self.magic_power = 25
        self.critical_rate = 0
        self.critical_damage = 0