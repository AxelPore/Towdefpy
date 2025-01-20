import pygame
import pytmx
import random
import character
import turret_and_building

def load_tmx_map(filename):
    return pytmx.load_pygame(filename, pixelalpha=True)

def draw_map(tmx_data, surface, offset_x, offset_y):
    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile = tmx_data.get_tile_image_by_gid(gid)
                if tile:
                    surface.blit(tile, (x * tmx_data.tilewidth + offset_x, y * tmx_data.tileheight + offset_y))

def check_collision(nexus, enemies):
    nexus_rect = nexus.get_rect()
    for enemy in enemies:
        if nexus_rect.colliderect(enemy.get_rect()):
            enemy.do_dmg(nexus)
            if nexus.health <= 0:
                return nexus
    return None

def main():
    pygame.init()
    screen_width, screen_height = 1550, 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('TMX Map Display with Pygame')

    # Load the TMX map
    tmx_data = load_tmx_map('Image_and_map/Maps/grassMap.tmx')

    # Calculate the center of the map
    map_center_x = (tmx_data.width * tmx_data.tilewidth) // 2
    map_center_y = (tmx_data.height * tmx_data.tileheight) // 2

    # Initialize the player character at the center of the map
    player = character.PlayerEngineer(map_center_x, map_center_y)
    nexus = turret_and_building.Nexus(map_center_x, map_center_y)
    
    gold = 100
    minerals = 100
    magic_cristals = 100
    # List to hold enemies, turrets, and projectiles
    enemies = []
    turrets = []
    projectiles = []
    mines = []

    # Timing variables for spawning and deleting enemies
    spawn_interval = 1000  # 1 seconds
    ennemiesSpawned = 0
    last_spawn_time = 0

    production_interval = 10000  # 10 seconds
    last_production_time = 0

    # Timing variables for appending turrets and mines
    turret_cooldown = 0.5  # 0.5 seconds cooldown
    last_turret_time = 0

    mine_cooldown = 0.5  # 0.5 seconds cooldown
    last_mine_time = 0

    wave_start_time = 0
    wave_active = False
    wave_duration = 60 * 1000  # 1 minute in milliseconds
    wave_interval = 60 * 1000  # 3 minutes in milliseconds
    initial_delay = 30 * 1000

    numberOfWaves = 0
    running = True
    clock = pygame.time.Clock()
    while running:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-5, 0, tmx_data.width * tmx_data.tilewidth, tmx_data.height * tmx_data.tileheight)
        if keys[pygame.K_RIGHT]:
            player.move(5, 0, tmx_data.width * tmx_data.tilewidth, tmx_data.height * tmx_data.tileheight)
        if keys[pygame.K_UP]:
            player.move(0, -5, tmx_data.width * tmx_data.tilewidth, tmx_data.height * tmx_data.tileheight)
        if keys[pygame.K_DOWN]:
            player.move(0, 5, tmx_data.width * tmx_data.tilewidth, tmx_data.height * tmx_data.tileheight)
        
        def is_position_valid(x, y, existing_objects, min_distance=50):
            for obj in existing_objects:
                if abs(obj.x - x) < min_distance and abs(obj.y - y) < min_distance:
                    return False
            return True

        # Check for building turret and mine
        if keys[pygame.K_TAB]:
            if current_time - last_turret_time > turret_cooldown * 1000:
                if is_position_valid(player.x, player.y, mines + turrets):  # Convert to milliseconds
                    if gold >= 10 and minerals >= 10 and magic_cristals >= 10:
                        turrets.append(turret_and_building.Magic_Tower(player.x, player.y))
                        gold -= 10
                        minerals -= 10
                        magic_cristals -= 10
                        last_turret_time = current_time  # Update last turret time

        if keys[pygame.K_1]:
            if current_time - last_turret_time > turret_cooldown * 1000:  # Convert to milliseconds
                if is_position_valid(player.x, player.y, mines + turrets):
                    if gold >= 10 and minerals >= 10 and magic_cristals >= 10:
                        turrets.append(turret_and_building.Physical_Tower(player.x, player.y))
                        gold -= 10
                        minerals -= 10
                        magic_cristals -= 10
                        last_turret_time = current_time  # Update last turret time

        if keys[pygame.K_SPACE]:
            if current_time - last_mine_time > mine_cooldown * 1000:  # Convert to milliseconds
                if is_position_valid(player.x, player.y, mines + turrets):
                    if gold >= 10 and minerals >= 10 and magic_cristals >= 10:
                        mines.append(turret_and_building.Gold_Mine(player.x, player.y))
                        gold -= 10
                        minerals -= 10
                        magic_cristals -= 10
                        last_mine_time = current_time  # Update last mine time

        if keys[pygame.K_0]:
            if current_time - last_mine_time > mine_cooldown * 1000:  # Convert to milliseconds
                if is_position_valid(player.x, player.y, mines + turrets):
                    if gold >= 10 and minerals >= 10 and magic_cristals >= 10:
                        
                        mines.append(turret_and_building.Minerals_Mine(player.x, player.y))
                        gold -= 10
                        minerals -= 10
                        magic_cristals -= 10
                        last_mine_time = current_time  # Update last mine time

        # Check if it's time to start a new wave
        if not wave_active and current_time - wave_start_time > wave_interval:
            wave_active = True
            wave_start_time = current_time

        # If a wave is active, spawn enemies every second
        if wave_active:
            if current_time - last_spawn_time > 500:  # 1 second in milliseconds
                while True:
                    enemy_x = random.randint(0, tmx_data.width * tmx_data.tilewidth - 50)
                    enemy_y = random.randint(0, tmx_data.height * tmx_data.tileheight - 50)
                    if enemy_x < 720 or enemy_y < 720 or enemy_x > tmx_data.width * tmx_data.tilewidth - 720 or enemy_y > tmx_data.width * tmx_data.tilewidth - 720:
                        break
                if numberOfWaves < 2:
                    enemies.append(character.BaseEnnemi(enemy_x, enemy_y))
                elif numberOfWaves < 5 :
                    if ennemiesSpawned < 100:
                        enemies.append(character.BaseEnnemi(enemy_x, enemy_y))
                    else:
                        enemies.append(character.MediumEnnemi(enemy_x, enemy_y))
                elif numberOfWaves < 8 :
                    if ennemiesSpawned < 80:
                        enemies.append(character.BaseEnnemi(enemy_x, enemy_y))
                    elif ennemiesSpawned < 100 :
                        enemies.append(character.MediumEnnemi(enemy_x, enemy_y))
                    else:
                        enemies.append(character.AdvancedEnnemi(enemy_x, enemy_y))
                elif numberOfWaves < 10 :
                    if ennemiesSpawned < 90:
                        enemies.append(character.BaseEnnemi(enemy_x, enemy_y))
                    elif ennemiesSpawned < 100 :
                        enemies.append(character.MediumEnnemi(enemy_x, enemy_y))
                    elif ennemiesSpawned < 110:
                        enemies.append(character.AdvancedEnnemi(enemy_x, enemy_y))
                    else:
                        enemies.append(character.EliteEnnemi(enemy_x, enemy_y))
                else:
                    if ennemiesSpawned < 85:
                        enemies.append(character.BaseEnnemi(enemy_x, enemy_y))
                    elif ennemiesSpawned < 100 :
                        enemies.append(character.MediumEnnemi(enemy_x, enemy_y))
                    elif ennemiesSpawned < 110:
                        enemies.append(character.AdvancedEnnemi(enemy_x, enemy_y))
                    elif ennemiesSpawned < 119:
                        enemies.append(character.EliteEnnemi(enemy_x, enemy_y))
                    else:
                        enemies.append(character.BossEnnemi(enemy_x, enemy_y))
                last_spawn_time = current_time
                ennemiesSpawned+=1

            # Check if the wave duration has ended
            if current_time - wave_start_time > wave_duration:
                wave_active = False
                wave_start_time = current_time + wave_interval  # Set the next wave start time  
                numberOfWaves+=1 
                ennemiesSpawned = 0                     
        
        # Resource production logic
        if current_time - last_production_time > production_interval:
            magic_cristals = nexus.product(magic_cristals)
            for mine in mines:
                gold, minerals = mine.product(gold, minerals)
            last_production_time = current_time
        # Enemy chasing logic
        for enemy in enemies:
            enemy.chase(nexus)

        # Turret attack logic
        for turret in turrets:
            turret.attack(enemies, projectiles)
            
        nexus.attack(enemies, projectiles)

        # Projectile movement and collision logic
        for projectile in list(projectiles):
            projectile.move()
            if projectile.check_collision():
                projectiles.remove(projectile)

        # Collision detection and handling
        nexus_down = check_collision(nexus, enemies)
        if nexus_down:
            pygame.quit()

        # Remove enemies with 0 or less health
        enemies = [enemy for enemy in enemies if enemy.health > 0]

        # Calculate the camera offset to center the player
        offset_x = screen_width // 2 - player.x - 25  # 25 is half the player width
        offset_y = screen_height // 2 - player.y - 25  # 25 is half the player height

        screen.fill((0, 0, 0))  # Clear the screen with black
        draw_map(tmx_data, screen, offset_x, offset_y)  # Draw the map surface with offsets
        player.draw(screen, offset_x, offset_y)  # Draw the player character with offsets
        nexus.draw(screen, offset_x, offset_y)
        for enemy in enemies:
            enemy.draw(screen, offset_x, offset_y)  # Draw each enemy with offsets
        for turret in turrets:
            turret.draw(screen, offset_x, offset_y)  # Draw each turret with offsets
        for projectile in projectiles:
            projectile.draw(screen, offset_x, offset_y)  # Draw each projectile with offsets
        for mine in mines:
            mine.draw(screen, offset_x, offset_y)  # Draw each mine with offsets

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
