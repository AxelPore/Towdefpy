import pygame
import game
import pytmx

def load_tmx_map(filename):
    return pytmx.load_pygame(filename, pixelalpha=True)

def draw_map(tmx_data, surface):
    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile = tmx_data.get_tile_image_by_gid(gid)
                if tile:
                    surface.blit(tile, (x * tmx_data.tilewidth, y * tmx_data.tileheight))

def main():
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('TMX Map Display with Pygame')

    # Load the TMX map
    tmx_data = load_tmx_map('Image_and_map/Maps/mapTest.tmx')

    # Create a surface to draw the map on
    map_surface = pygame.Surface((tmx_data.width * tmx_data.tilewidth, tmx_data.height * tmx_data.tileheight))

    # Draw the map onto the surface
    draw_map(tmx_data, map_surface)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Clear the screen with black
        screen.blit(map_surface, (0, 0))  # Draw the map surface onto the screen
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()



#if __name__ == "__main__":
#    pygame.init()
#    game.main()
    