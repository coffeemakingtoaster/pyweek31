#library imports
import pygame
import pytmx 
import os

#local imports
from . import pygame_additions
from . import Logic
from . import Render

from .helper import SoundHelper

from .ui.Ui import *

from . import config

def hallo_welt():
    print("hallo")

def launch_game():
    pygame.mixer.pre_init(frequency=44100,size=-16,channels=2, buffer=2048)
    pygame.init()
    screen = pygame.display.set_mode(config.WINDOW_DIMENSIONS)
    gameMap = pytmx.load_pygame("data/maps/test-map.tmx")
    running = True
    button = pygame_additions.button(40,40,100,100)
    button.set_action(hallo_welt)
    #button.draw(screen)
    pygame.display.flip()
    print(os.path.join('..', 'data', 'assets', 'testing', 'max.png'))
    #Load assets
    assets = {
        'textures': {
            "max" : pygame.image.load(os.path.join(os.path.dirname( __file__ ), '..', 'data', 'assets', 'testing', 'max.png')),
            "enemy" : pygame.image.load(os.path.join(os.path.dirname( __file__ ), '..', 'data', 'assets', 'testing', 'enemy.png')),
            "chest": pygame.image.load(os.path.join(os.path.dirname( __file__ ), '..', 'data', 'assets', 'testing', 'chest.png'))
        },
        'sounds': {
            "background" : pygame.mixer.Sound(os.path.join(os.path.dirname( __file__ ), '..', 'data', 'assets', 'testing', 'background_music.mp3'))
        }
    }

    #Load sound
    soundHelper = SoundHelper.SoundHelper()

    #play background music
    soundHelper.play_music(assets['sounds']['background'], 0)

    #Load User Interface
    ui = Ui()

    #Create logic
    logic = Logic.Logic(gameMap)

    render = Render.Render(logic, assets, gameMap, ui)
    ui.say('Game Main loaded!')
    
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
        pygame.display.flip()
