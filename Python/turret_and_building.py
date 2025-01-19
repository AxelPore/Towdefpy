import pygame
import math

class Turret_and_building:
    def __init__(self, x, y, width=50, height=50):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = 100  # Default health value
        self.last_attack_time = 0  # Track the last attack time
    def take_dmg(self):
        print("dmg taken")
    def do_dmg(self):
        print("dmg dealt")
    def upgrade(self):
        print("upgrade")
    def repair(self):
        print("repaired")
    def loot(self):
        print("looted")
    def __del__(self):
        print(f"{self} has been deleted")
        
class Nexus(Turret_and_building):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.range = 300
        self.last_attack_time = 0
        self.health = 1000
        self.armor = 100
        self.magic_resist = 100
        self.strength = 100
        self.magic_power = 100
        self.critical_rate = 0.25
        self.critical_damage = 1.5
        self.production = 10

    def draw(self, surface, offset_x, offset_y):
        pygame.draw.circle(surface, (0, 255, 255), (self.x + offset_x, self.y + offset_y), self.range, 1)
        pygame.draw.rect(surface, (255, 0, 0), (self.x + offset_x, self.y + offset_y, self.width, self.height))

    def attack(self, enemies, projectiles):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time >= 1000:  # Attack cooldown
            for enemy in enemies:
                if math.hypot(enemy.x - self.x, enemy.y - self.y) <= self.range:
                    projectiles.append(Projectile(self.x, self.y, enemy))
                    self.last_attack_time = current_time
                    break
        
class Magic_Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.range = 300
        self.last_attack_time = 0

    def draw(self, surface, offset_x, offset_y):
        pygame.draw.circle(surface, (0, 255, 255), (self.x + offset_x, self.y + offset_y), self.range, 1)
        pygame.draw.rect(surface, (255, 255, 0), (self.x + offset_x - 15, self.y + offset_y - 15, 30, 30))

    def attack(self, enemies, projectiles):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time >= 1000:  # Attack cooldown
            for enemy in enemies:
                if math.hypot(enemy.x - self.x, enemy.y - self.y) <= self.range:
                    projectiles.append(Projectile(self.x, self.y, enemy))
                    self.last_attack_time = current_time
                    break

class Projectile:
    def __init__(self, x, y, target):
        self.x = x
        self.y = y
        self.target = target
        self.speed = 5
        self.damage_done = False

    def move(self):
        if not self.damage_done:
            direction = math.atan2(self.target.y - self.y, self.target.x - self.x)
            self.x += self.speed * math.cos(direction)
            self.y += self.speed * math.sin(direction)

    def draw(self, surface, offset_x, offset_y):
        pygame.draw.circle(surface, (255, 0, 0), (int(self.x + offset_x), int(self.y + offset_y)), 5)

    def check_collision(self):
        if not self.damage_done and math.hypot(self.target.x - self.x, self.target.y - self.y) < 5:
            self.target.take_dmg(10)
            self.damage_done = True
            return True
        return False
        
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