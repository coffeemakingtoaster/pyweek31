import random
import pygame
from . import Render

class Keycards():

    keycard_spawns = [{"x_spawn":1568, "y_spawn":2275}, {"x_spawn":949, "y_spawn":1194}, {"x_spawn":1881, "y_spawn":652}, {"x_spawn":1880, "y_spawn":1530}, {"x_spawn":573, "y_spawn":630}]
    collect_counter = 0

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
        for i in range(3):
            #keycard_posx = random.randrange(1000)
            #keycard_posy = random.randrange(1000)
            keycard_pos = random.choice(self.keycard_spawns)
            keycard_posx = keycard_pos["x_spawn"]
            keycard_posy = keycard_pos["y_spawn"]
            keycard_rect = assets['textures']['keycard'].get_rect()
            keycard_rect.center = (keycard_posx,keycard_posy)
            self.container.append({"x_cord":keycard_posx, "y_cord":keycard_posy, "collectable":True, "rect":keycard_rect})
        return self.container
    
    def keycard_player_collision(self, keycard_rect, player_rect):
        if self.collect_counter <= 2:
            #print(self.collect_counter)
            for keycard in self.container:
                if keycard["rect"].colliderect(player_rect):
                    if keycard["collectable"] == True:
                        #print("collided")
                        keycard["collectable"] = False
                        self.collect_counter += 1
                        print(self.collect_counter)
        elif self.collect_counter >= 3:
                self.winning()

    def winning(self):
        pass
