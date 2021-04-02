import pygame
import os

class Assetloader():
    def __init__(self):
        self.assets = {'sounds':{},'textures':{}}
        self.load_sounds()
        self.load_textures()
    
    def load_sounds(self):
        self.assets['sounds'] = {
            "background" : pygame.mixer.Sound(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'assets', 'testing', 'background_music.mp3')),
            "bark" : [
                pygame.mixer.Sound(os.path.join(os.path.dirname( __file__ ), '..','..', 'data', 'assets', 'testing', 'pew_sfx.mp3')),
                pygame.mixer.Sound(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'assets', 'testing', 'bark.mp3')),
                pygame.mixer.Sound(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'assets', 'testing', 'bark_2.mp3'))
            ]
        }
    
    def load_textures(self):
         self.assets['textures'] = {
                "max" : pygame.image.load(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'assets', 'player', 'player_1.png')),
                "enemies" : [pygame.image.load(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'assets', 'guard', 'guard1.png')),
                         pygame.image.load(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'assets', 'guard', 'guard2.png'))],
                "keycard": pygame.image.load(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'assets', 'testing', '0.png')),
                "chest" : pygame.image.load(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'assets', 'mapsprite', 'filled_bin.png')),
                "hud" : [
                    pygame.image.load(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'assets', 'testing', 'hud_1.png')),
                    pygame.image.load(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'assets', 'testing', 'hud_2.png')),
                    pygame.image.load(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'assets', 'testing', 'hud_3.png'))
                ],
                "player" : [
                    pygame.image.load(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'assets', 'player', 'player_1.png')),
                    pygame.image.load(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'assets', 'player', 'player_2.png'))
                ],
                "ui": {
                    "menu_background": pygame.image.load(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'assets', 'wall', 'wall_full_back_high_res.png'))
                },
                "door" :  pygame.image.load(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'assets', 'testing', 'door.png')),
                "mice":[pygame.image.load(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'assets', 'mapsprite', 'mouse1.png')),
                        pygame.image.load(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'assets', 'mapsprite', 'mouse2.png'))]
            } 