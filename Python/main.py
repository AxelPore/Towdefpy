import pygame
import pytmx
import random
import character


def load_tmx_map(filename):
    return pytmx.load_pygame(filename, pixelalpha=True)

def draw_map(tmx_data, surface, offset_x, offset_y):
    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile = tmx_data.get_tile_image_by_gid(gid)
                if tile:
                    surface.blit(tile, (x * tmx_data.tilewidth + offset_x, y * tmx_data.tileheight + offset_y))

def check_collision(player, enemies):
    player_rect = player.get_rect()
    for enemy in enemies:
        if player_rect.colliderect(enemy.get_rect()):
            player.do_dmg(enemy)
            enemy.do_dmg(player)
            if player.health <= 0 or enemy.health <= 0:
                return enemy
    return None

def main():
    pygame.init()
    screen_width, screen_height = 1550, 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('TMX Map Display with Pygame')

    # Load the TMX map
    tmx_data = load_tmx_map('Image_and_map/Maps/grassMap.tmx')

    # Create a surface to draw the map on
    map_surface = pygame.Surface((tmx_data.width * tmx_data.tilewidth, tmx_data.height * tmx_data.tileheight))

    # Draw the map onto the surface
    draw_map(tmx_data, map_surface, 0, 0)

    # Initialize the player character
    player = character.PlayerEngineer(100, 100)

    # List to hold enemies
    enemies = []

    # Timing variables for spawning and deleting enemies
    spawn_interval = 15000  # 15 seconds
    last_spawn_time = 0

    running = True
    clock = pygame.time.Clock()
    while running:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-5, 0)
        if keys[pygame.K_RIGHT]:
            player.move(5, 0)
        if keys[pygame.K_UP]:
            player.move(0, -5)
        if keys[pygame.K_DOWN]:
            player.move(0, 5)

        # Enemy spawning logic
        if current_time - last_spawn_time > spawn_interval:
            enemy_x = random.randint(0, tmx_data.width * tmx_data.tilewidth - 50)
            enemy_y = random.randint(0, tmx_data.height * tmx_data.tileheight - 50)
            enemies.append(character.BaseEnnemi(enemy_x, enemy_y))
            last_spawn_time = current_time


        # Enemy chasing logic
        for enemy in enemies:
            enemy.chase(player)

        # Collision detection and handling
        enemy_to_delete = check_collision(player, enemies)
        if enemy_to_delete:
            enemies.remove(enemy_to_delete)

        # Calculate the camera offset to center the player
        offset_x = screen_width // 2 - player.x - 25  # 25 is half the player width
        offset_y = screen_height // 2 - player.y - 25  # 25 is half the player height

        screen.fill((0, 0, 0))  # Clear the screen with black
        draw_map(tmx_data, screen, offset_x, offset_y)  # Draw the map surface with offsets
        player.draw(screen, offset_x, offset_y)  # Draw the player character with offsets
        for enemy in enemies:
            enemy.draw(screen, offset_x, offset_y)  # Draw each enemy with offsets
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()