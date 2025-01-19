import pygame
import turret_and_building

class Character:
    def __init__(self, x, y, width=50, height=50):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = 100  # Default health value
        self.last_attack_time = 0  # Track the last attack time

    def take_dmg(self, amount):
        self.health -= amount
        print(f"Damage taken: {amount}, Health remaining: {self.health}")
        if self.health <= 0:
            self.__del__()

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
        # Placeholder for drawing the character (a red square for now)
        pygame.draw.rect(surface, (255, 0, 0), (self.x + offset_x, self.y + offset_y, self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def __del__(self):
        print(f"{self} has been deleted")

class PlayerEngineer(Character):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.health = 10000000
        self.armor = 30
        self.magic_resist = 30
        self.speed = 60
        self.strength = 10
        self.magic_power = 10
        self.critical_rate = 0.25
        self.critical_damage = 0.5

    def build(self):
        turret = turret_and_building.Magic_Tower(self.x, self.y)

    def draw(self, surface, offset_x, offset_y):
        # Draw the player as a green square
        pygame.draw.rect(surface, (0, 255, 0), (self.x + offset_x, self.y + offset_y, self.width, self.height))

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
        # Draw the enemy as a blue square
        pygame.draw.rect(surface, (0, 0, 255), (self.x + offset_x, self.y + offset_y, self.width, self.height))
        
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
    def __del__(self):
        print(f"{self} has been deleted")