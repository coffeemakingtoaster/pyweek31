#library imports
import pygame
import pytmx 
import os
import time

#local imports
from . import pygame_additions
from . import Logic
from . import Render
from .game_objects import Keycard

from .helper import SoundHelper
from .helper import asset_loader

from .ui.Ui import *

from . import config

def hallo_welt():
    print("hallo")

def launch_game():
    pygame.mixer.pre_init(frequency=44100,size=-16,channels=2, buffer=2048)
    pygame.init()

    clock = pygame.time.Clock()

    if FULLSCREEN:
        screen = pygame.display.set_mode(config.WINDOW_DIMENSIONS, pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(config.WINDOW_DIMENSIONS)
    gameMap = pytmx.load_pygame("data/maps/test-map.tmx")
    running = True
    button = pygame_additions.button(40,40,100,100)
    button.set_action(hallo_welt)
    #button.draw(screen)
    pygame.display.flip()

    #Load assets
    assets = asset_loader.Assetloader().assets
    #Load sound
    soundHelper = SoundHelper.SoundHelper()

    #Play background music
    soundHelper.play_music(assets['sounds']['background'], -1)


    #Load User Interface
    ui = Ui({
        'assets': assets,
        'soundHelper': soundHelper
    })

    #Create logic
    logic = Logic.Logic(gameMap)


    render = Render.Render(logic, assets, gameMap, ui)
    ui.say('Game Main loaded!')
    
    last_second_frames = 0
    
    start_time = time.time()
    
    while running:
        if time.time() - start_time > 1 :
            start_time = time.time()
            last_second_frames = render.get_drawn_frames()
        logic.update()
        next_frame = render.generate_new_frame()
        #ui.say("Frames per second: "+str(last_second_frames))

        #if last_second_frames < 60:
        #    last_second_frames = 60
        ui.uiHelper.createText("FPS "+ str(last_second_frames), {
            'font': ui.uiHelper.fonts['text']['font'],
            'render': render,
            'x': WINDOW_WIDHT - 200,
            'y': 100,
            'color': (255, 255, 255)
        })
        screen.blit(next_frame, (0, 0)) 
        #button.draw(screen)

        #Sound test
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            soundHelper.play_sfx(assets['sounds']['bark'], 0)

        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                button.handle_input(event.pos)               
        pygame.display.flip()
