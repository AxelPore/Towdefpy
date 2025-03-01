import pygame
import turret_and_building

class Character:
    def __init__(self, x, y, width=50, height=50):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = 100  
        self.last_attack_time = 0  

    def take_dmg(self, amount):
        self.health -= amount
        
            

    def do_dmg(self, target):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time >= 1000:  # 1 second cooldown
            target.take_dmg(10)
            self.last_attack_time = current_time

    def move(self, dx, dy, map_width, map_height):
        # Update position
        self.x += dx
        self.y += dy

        # Restrict movement to the map boundaries
        self.x = max(730, min(self.x, map_width - self.width - 730))
        self.y = max(730, min(self.y, map_height - self.height - 730))

    def draw(self, surface, offset_x, offset_y):
        pygame.draw.rect(surface, (255, 0, 0), (self.x + offset_x, self.y + offset_y, self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


class PlayerEngineer(Character):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.health = 100
        self.armor = 30
        self.magic_resist = 30
        self.speed = 60
        self.strength = 10
        self.magic_power = 10
        self.critical_rate = 0.25
        self.critical_damage = 0.5
        self.image = pygame.image.load(r'Image_and_map\characters\BigTankLeft.png')


    def draw(self, surface, offset_x, offset_y):
        surface.blit(self.image, (self.x + offset_x, self.y + offset_y))

class BaseEnnemi(Character):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.health = 30
        self.armor = 10
        self.magic_resist = 10
        self.speed = 50
        self.strength = 10
        self.magic_power = 10
        self.critical_rate = 0
        self.critical_damage = 0
        self.image = pygame.image.load(r'Image_and_map\characters\MagicGhostLeft.png')

    def chase(self, target):
        if self.x < target.x:
            self.x += 1
        elif self.x > target.x:
            self.x -= 1

        if self.y < target.y:
            self.y += 1
        elif self.y > target.y:
            self.y -= 1

    def draw(self, surface, offset_x, offset_y):
        surface.blit(self.image, (self.x + offset_x, self.y + offset_y))
        
class MediumEnnemi(Character):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.health = 70
        self.armor = 10
        self.magic_resist = 10
        self.speed = 35
        self.strength = 10
        self.magic_power = 10
        self.critical_rate = 0
        self.critical_damage = 0
        self.image = pygame.image.load(r'Image_and_map\characters\MagicMidGhostLeft.png')

    def chase(self, target):
        if self.x < target.x:
            self.x += 1
        elif self.x > target.x:
            self.x -= 1

        if self.y < target.y:
            self.y += 1
        elif self.y > target.y:
            self.y -= 1

    def draw(self, surface, offset_x, offset_y):
        self.image = pygame.transform.scale(self.image, (int(self.width * 2), int(self.height * 2)))
        surface.blit(self.image, (self.x + offset_x, self.y + offset_y))
        
    def do_dmg(self, target):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time >= 1000:  # 1 second cooldown
            target.take_dmg(20)
            self.last_attack_time = current_time
        
class AdvancedEnnemi(Character):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.health = 150
        self.armor = 10
        self.magic_resist = 10
        self.speed = 20
        self.strength = 10
        self.magic_power = 10
        self.critical_rate = 0
        self.critical_damage = 0
        self.image = pygame.image.load(r'Image_and_map\characters\MagicAdvGhostLeft.png')

    def chase(self, target):
        if self.x < target.x:
            self.x += 1
        elif self.x > target.x:
            self.x -= 1

        if self.y < target.y:
            self.y += 1
        elif self.y > target.y:
            self.y -= 1

    def draw(self, surface, offset_x, offset_y):
        self.image = pygame.transform.scale(self.image, (int(self.width * 3), int(self.height * 3)))
        surface.blit(self.image, (self.x + offset_x, self.y + offset_y))
        
    def do_dmg(self, target):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time >= 1000:  # 1 second cooldown
            target.take_dmg(40)
            self.last_attack_time = current_time
        
class EliteEnnemi(Character):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.health = 300
        self.armor = 10
        self.magic_resist = 10
        self.speed = 13
        self.strength = 10
        self.magic_power = 10
        self.critical_rate = 0
        self.critical_damage = 0
        self.image = pygame.image.load(r'Image_and_map\characters\MagicEliteGhostLeft.png')

    def chase(self, target):
        if self.x < target.x:
            self.x += 1
        elif self.x > target.x:
            self.x -= 1

        if self.y < target.y:
            self.y += 1
        elif self.y > target.y:
            self.y -= 1

    def draw(self, surface, offset_x, offset_y):
        self.image = pygame.transform.scale(self.image, (int(self.width * 4), int(self.height * 4)))
        surface.blit(self.image, (self.x + offset_x, self.y + offset_y))
        
    def do_dmg(self, target):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time >= 1000:  # 1 second cooldown
            target.take_dmg(150)
            self.last_attack_time = current_time
        
class BossEnnemi(Character):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.health = 1000
        self.armor = 10
        self.magic_resist = 10
        self.speed = 6
        self.strength = 10
        self.magic_power = 10
        self.critical_rate = 0
        self.critical_damage = 0
        self.image = pygame.image.load(r'Image_and_map\characters\LavenderGhostLeft.png')

    def chase(self, target):
        if self.x < target.x:
            self.x += 1
        elif self.x > target.x:
            self.x -= 1

        if self.y < target.y:
            self.y += 1
        elif self.y > target.y:
            self.y -= 1

    def draw(self, surface, offset_x, offset_y):
        self.image = pygame.transform.scale(self.image, (int(self.width * 5), int(self.height * 5)))
        surface.blit(self.image, (self.x + offset_x, self.y + offset_y))
        
    def do_dmg(self, target):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time >= 1000:  # 1 second cooldown
            target.take_dmg(1000)
            self.last_attack_time = current_time