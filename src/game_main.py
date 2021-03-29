import pygame
from . import pygame_additions
import pytmx 
from . import Logic
from . import Render
import os

from . import config

def hallo_welt():
    print("hallo")


def launch_game():
    pygame.init()
    screen = pygame.display.set_mode(config.WINDOW_DIMENSIONS)
    gameMap = pytmx.load_pygame("data/maps/gameart2d-desert.tmx")
    running = True
    button = pygame_additions.button(40,40,100,100)
    button.set_action(hallo_welt)
    #button.draw(screen)
    pygame.display.flip()
    print(os.path.join('..', 'data', 'assets', 'testing', 'max.png'))
    #Load assets
    assets = {
        'textures': {
            "max" : pygame.image.load(os.path.join(os.path.dirname( __file__ ), '..', 'data', 'assets', 'testing', 'max.png'))
        }
    }

    #Create logic
    logic = Logic.Logic()

    render = Render.Render(logic, assets)

    while running:
        logic.update()
        next_frame = render.generate_new_frame()
        screen.blit(next_frame, (0, 0))
        
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
