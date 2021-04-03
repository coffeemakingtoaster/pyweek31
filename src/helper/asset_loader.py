import pygame
import os

class Assetloader():
    def __init__(self):
        self.assets = {'sounds':{},'textures':{}}
        self.load_sounds()
        self.load_textures()
    
    def load_sounds(self):
        self.assets['sounds'] = {
            "background" : pygame.mixer.Sound(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'assets', 'audio', 'sfx', 'world', 'GefängnisAtmo.wav')),
            "bark" : [
                pygame.mixer.Sound(os.path.join(os.path.dirname( __file__ ), '..','..', 'data', 'assets', 'testing', 'pew_sfx.mp3')),
                pygame.mixer.Sound(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'assets', 'testing', 'bark.mp3')),
                pygame.mixer.Sound(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'assets', 'testing', 'bark_2.mp3'))
            ],
            "actor" : {
                "footsteps": {
                    "concrete": [
                        pygame.mixer.Sound(os.path.join(os.path.dirname( __file__ ), '..','..', 'data', 'assets', 'audio', 'sfx', 'actor', 'footsteps', 'concrete', 'running_01.wav')),
                        pygame.mixer.Sound(os.path.join(os.path.dirname( __file__ ), '..','..', 'data', 'assets', 'audio', 'sfx', 'actor', 'footsteps', 'concrete', 'running_02.wav')),
                        pygame.mixer.Sound(os.path.join(os.path.dirname( __file__ ), '..','..', 'data', 'assets', 'audio', 'sfx', 'actor', 'footsteps', 'concrete', 'running_03.wav')),
                        pygame.mixer.Sound(os.path.join(os.path.dirname( __file__ ), '..','..', 'data', 'assets', 'audio', 'sfx', 'actor', 'footsteps', 'concrete', 'running_04.wav')),
                        pygame.mixer.Sound(os.path.join(os.path.dirname( __file__ ), '..','..', 'data', 'assets', 'audio', 'sfx', 'actor', 'footsteps', 'concrete', 'running_05.wav')),
                        pygame.mixer.Sound(os.path.join(os.path.dirname( __file__ ), '..','..', 'data', 'assets', 'audio', 'sfx', 'actor', 'footsteps', 'concrete', 'running_06.wav'))
                        
                    ]
                }
            },
            "door" :[ pygame.mixer.Sound(os.path.join(os.path.dirname( __file__ ), '..','..', 'data', 'assets', 'audio', 'sfx', 'world', 'door_2.wav'))],
            "coffee": [pygame.mixer.Sound(os.path.join(os.path.dirname( __file__ ), '..','..', 'data', 'assets', 'audio', 'sfx', 'world', 'Schlürf.wav'))],
            "atmo":  [pygame.mixer.Sound(os.path.join(os.path.dirname( __file__ ), '..','..', 'data', 'assets', 'audio', 'sfx', 'world', 'GefängnisAtmo.wav')),
                      pygame.mixer.Sound(os.path.join(os.path.dirname( __file__ ), '..','..', 'data', 'assets', 'audio', 'sfx', 'world', 'GefängnisAtmo_2.wav'))],
            "jammer":[pygame.mixer.Sound(os.path.join(os.path.dirname( __file__ ), '..','..', 'data', 'assets', 'audio', 'sfx', 'world', 'PoliceCall.wav'))]     
        }
    
    def load_textures(self):
         self.assets['textures'] = {
                "max" : pygame.image.load(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'assets', 'player', 'player_1.png')),
                "enemies" : [pygame.image.load(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'assets', 'guard', 'guard1.png')),
                         pygame.image.load(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'assets', 'guard', 'guard2.png'))],
                "keycards": {"blue": pygame.image.load(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'assets', 'keycards', 'blue.png')),
                             "green": pygame.image.load(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'assets', 'keycards', 'green.png')),
                             "red": pygame.image.load(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'assets', 'keycards', 'red.png'))},
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
                "doors" : {"door": [pygame.image.load(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'assets', 'mapsprite', 'door.png')),
                                    pygame.image.load(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'assets', 'mapsprite', 'door1.png'))], 
                           "door_rot": [pygame.image.load(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'assets', 'mapsprite', 'door_rotate.png')),
                                        pygame.image.load(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'assets', 'mapsprite', 'door1_rotate.png'))]},
                "mice":[pygame.image.load(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'assets', 'mapsprite', 'mouse1.png')),
                        pygame.image.load(os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'assets', 'mapsprite', 'mouse2.png'))]
            } 