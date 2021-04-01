import random
import pygame
from . import Render

class Keycards():


    def __init__(self, assets):
        self.x = 40
        self.y = 40
        self.is_picked_up = False
        self.container = []
        self.assets = assets
    
    #container = []

    #asset for keycard
    
    
    def create_keycards(self):
        assets = self.assets
        for i in range(10):
            keycard_posx = random.randrange(1000)
            keycard_posy = random.randrange(1000)
            keycard_rect = assets['textures']['keycard'].get_rect()
            keycard_rect.center = (keycard_posx,keycard_posy)
            self.container.append({"x_cord":keycard_posx, "y_cord":keycard_posy, "collectable":True, "rect":keycard_rect})
        return self.container
    
    def keycard_player_collision(self, keycard_rect, player_rect):
        for keycard in self.container:
            if keycard["rect"].colliderect(player_rect):
                print("collided")
                keycard["collectable"] = False