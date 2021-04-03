#library imports
import pygame
import pytmx 
import os
import time
import sys

#local imports
from . import pygame_additions
from . import Logic
from . import Render
from .game_objects import Keycard

from .helper import SoundHelper
from .helper import asset_loader
from .helper import GameStateManager

from .ui.Ui import *

from . import config

def hallo_welt():
    print("Hello World! This is a test print! We should remove this!")


def launch_game():
    pygame.mixer.pre_init(frequency=44100,size=-16,channels=2, buffer=2048)
    pygame.init()

    game_state = GameStateManager.GameStateManager()

    clock = pygame.time.Clock()

    if FULLSCREEN:
        screen = pygame.display.set_mode(config.WINDOW_DIMENSIONS, pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(config.WINDOW_DIMENSIONS)
    gameMap = pytmx.load_pygame("data/maps/map_test_128_64.tmx")
    running = True
    #button = pygame_additions.button(40,40,100,100)
    #button.set_action(hallo_welt)
    #button.draw(screen)
    pygame.display.flip()

    #Load assets
    assets = asset_loader.Assetloader().assets
    #Load sound
    soundHelper = SoundHelper.SoundHelper()

    #Play background music
    soundHelper.play_music(assets['sounds']['background'], -1)

    time_since_last_atmo = 0
    
    #Load User Interface
    ui = Ui({
        'assets': assets,
        'soundHelper': soundHelper
    })

    #Create logic
    logic = Logic.Logic(gameMap, soundHelper, assets, game_state, ui)

    render = Render.Render(logic, assets, gameMap, ui, game_state, soundHelper)
    
    last_second_frames = 0
    
    start_time = time.time()

    ticks_while_game_state_is_play_after_tick_start = 0 #longest variable in game heheh
    ticks_of_last_frame = 0
    start_ticks = True # Set this to true and the ticker will start heheheheh (can be set later e.g.: when the player does his first move)

    game_state.set_game_state('cutscene')

    # cut_scene.createCutScene([<message>, {'time': <time>, 'color': <color>}])
    # <message>: text to display
    #
    # optional:
    # <time>: time to wait till you can press space
    # <color>: color of your text
    # WARNING: props must be at least an empty object (if someone knows how to fix that: DO it! )

    if(not SKIP_INTRO or not SKIP_DIALOGS):
        # ui.cut_scene.createCutScene([
            # ['Ahh where I am?', { 'color': (255, 0, 0)}],
            # ['Where is my thomy mayonnaise?', {'color': (255, 255, 0)}],
            # ['Maybe the one dog ate it...', {'color': (255, 0, 255)}],
            # ['hehehehehe', {}],
        # ])
        ui.cut_scene.createCutScene([
            ['Ahhhh… my head hurts.', {}],
            ['Bitchass bastards took away my beloved badge. ', {}],
            ['Suckers didn’t stop at my special sunglasses...', {}],
            ['The ones from Sander’s Supermarket Sunday Sale.', {}],
            ['But they missed the car keys in my butt crack hehehehe.', {}],
            ['But first I need to get out of here!', {}]
        ])
    
    while running:
        #print(game_state.game_state)
        
        if game_state.is_reset():
            logic = Logic.Logic(gameMap, soundHelper, assets,game_state)
            render = Render.Render(logic, assets, gameMap, ui, game_state, soundHelper)
            ticks_while_game_state_is_play_after_tick_start = 0 #longest variable in game heheh
            ticks_of_last_frame = 0
            start_ticks = True # Set this to true and the ticker will start heheheheh (can be set later e.g.: when the player does his first move)
            game_state.set_game_state('cutscene')
        
        if time.time() - time_since_last_atmo > 40:
            soundHelper.play_atmo_sound(assets["sounds"]["atmo"])
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state.set_game_state('quit')
                running = False
                pygame.display.quit()
                sys.exit()
            #if event.type == pygame.MOUSEBUTTONDOWN:
            #    button.handle_input(event.pos)               

        if time.time() - start_time > 1 :
            start_time = time.time()
            last_second_frames = render.get_drawn_frames()

        if game_state.is_play():
            logic.update()
        next_frame = render.generate_new_frame()
        
        if game_state.is_play() and start_ticks:
            ticks_while_game_state_is_play_after_tick_start += pygame.time.get_ticks() - ticks_of_last_frame
        ticks_of_last_frame = pygame.time.get_ticks()

        ui.uiHelper.createText(str(ui.uiHelper.formatTime(ticks_while_game_state_is_play_after_tick_start)[0]) + ":" + str(ui.uiHelper.formatTime(ticks_while_game_state_is_play_after_tick_start)[1]), {
            'font': ui.uiHelper.fonts['text']['font'],
            'render': render,
            'x': WINDOW_WIDHT - 200,
            'y': 50,
            'color': (255, 255, 255)
        })

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

        clock.tick(60)

        pygame.display.flip()
        
        if ui.menu.open:
            game_state.set_game_state('pause')
        elif ui.cut_scene.is_active:
            game_state.set_game_state('cut_scene')
        elif not game_state.is_over():
            game_state.set_game_state('play')

            
        if pygame.key.get_pressed()[config.PLAYER_RESET] == True:
            game_state.set_game_state('reset')