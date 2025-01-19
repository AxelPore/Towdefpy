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

    def product(self, magical_cristals):
        return magical_cristals + self.production

    def draw(self, surface, offset_x, offset_y):
        pygame.draw.circle(surface, (0, 255, 255), (self.x + offset_x, self.y + offset_y), self.range, 1)
        pygame.draw.rect(surface, (255, 0, 0), (self.x + offset_x, self.y + offset_y, self.width, self.height))

    def attack(self, enemies, projectiles):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time >= 3000:  # Attack cooldown
            for enemy in enemies:
                if math.hypot(enemy.x - self.x, enemy.y - self.y) <= self.range:
                    projectiles.append(Missile(self.x, self.y, enemy))
                    self.last_attack_time = current_time
                    break

class Missile:
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
            self.target.take_dmg(100)
            self.damage_done = True
            return True
        return False

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
                    projectiles.append(Magic_Projectile(self.x, self.y, enemy))
                    self.last_attack_time = current_time
                    break

class Magic_Projectile:
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
        pygame.draw.circle(surface, (255, 255, 120), (int(self.x + offset_x), int(self.y + offset_y)), 10)

    def check_collision(self):
        if not self.damage_done and math.hypot(self.target.x - self.x, self.target.y - self.y) < 10:
            self.target.take_dmg(25)
            self.damage_done = True
            return True
        return False
        
class Physical_Tower(Turret_and_building):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.range = 150
        self.last_attack_time = 0

    def draw(self, surface, offset_x, offset_y):
        pygame.draw.circle(surface, (0, 255, 255), (self.x + offset_x, self.y + offset_y), self.range, 1)
        pygame.draw.rect(surface, (0, 255, 100), (self.x + offset_x - 15, self.y + offset_y - 15, 30, 30))

    def attack(self, enemies, projectiles):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time >= 300:  # Attack cooldown
            for enemy in enemies:
                if math.hypot(enemy.x - self.x, enemy.y - self.y) <= self.range:
                    projectiles.append(Physical_Projectile(self.x, self.y, enemy))
                    self.last_attack_time = current_time
                    break

class Physical_Projectile:
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
        pygame.draw.circle(surface, (155, 90, 30), (int(self.x + offset_x), int(self.y + offset_y)), 5)

    def check_collision(self):
        if not self.damage_done and math.hypot(self.target.x - self.x, self.target.y - self.y) < 5:
            self.target.take_dmg(10)
            self.damage_done = True
            return True
        return False
        
class Gold_Mine(Turret_and_building):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.health = 250
        self.armor = 50
        self.magic_resist = 50
        self.production = 5
        self.image = pygame.image.load('C:\Users\axelp\Desktop\School\Python\Towdefpy\Image_and_map\buildings\goldMine.png')
        self.width, self.height = self.image.get_size()

    def product(self, gold, minerals):
        return gold + self.production, minerals

    def draw(self, surface, offset_x, offset_y):
        surface.blit(self.image, (self.x + offset_x, self.y + offset_y))
        
class Minerals_Mine(Turret_and_building):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.health = 250
        self.armor = 50
        self.magic_resist = 50
        self.production = 5
    def product(self, gold, minerals):
        return gold, minerals + self.production
    def draw(self, surface, offset_x, offset_y):
        pygame.draw.rect(surface, (255, 255, 255), (self.x + offset_x, self.y + offset_y, self.width, self.height))
    def __del__(self):
        print(f"{self} has been deleted")