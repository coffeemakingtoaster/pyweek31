import pygame
from . import pygame_additions
import pytmx 

window_dimensions = (800,800)

def hallo_welt():
    print("hallo")


def launch_game():
    pygame.init()
    screen = pygame.display.set_mode(window_dimensions)
    gameMap = pytmx.load_pygame("data/maps/gameart2d-desert.tmx")
    running = True
    button = pygame_additions.button(40,40,100,100)
    button.set_action(hallo_welt)
    #button.draw(screen)
    pygame.display.flip()
    while running:
        #button.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                button.handle_input(event.pos)
        for layer in gameMap.visible_layers:
            for x, y, gid, in layer:
                tile = gameMap.get_tile_image_by_gid(gid)
                if(tile != None):
                    screen.blit(tile, (x * gameMap.tilewidth, y * gameMap.tileheight))        
        pygame.display.flip()
