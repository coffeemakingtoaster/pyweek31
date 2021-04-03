import random
import pygame
from .. import Render

class Keycards():

    keycard_spawns = [{"x_spawn":1568, "y_spawn":2275}, {"x_spawn":949, "y_spawn":1194}, {"x_spawn":1881, "y_spawn":652}, {"x_spawn":1880, "y_spawn":1530}, {"x_spawn":573, "y_spawn":630}]
    keycard_colors = ["blue", "red", "green"]
    

    def __init__(self):
        self.x = 40
        self.y = 40
        self.is_picked_up = False
        self.container = []
        self.create_keycards()
        self.all_collected = False
        self.collect_counter = 0
    
    
    def create_keycards(self):
        for i in range(3):
            keycard_pos = random.choice(self.keycard_spawns)
            #keycard_posx = keycard_pos["x_spawn"]
            #keycard_posy = keycard_pos["y_spawn"]
            keycard_posx = 1000
            keycard_posy = 1000
            keycard_rect = pygame.Rect((0,0),(30,30))
            #keycard_rect.center = (keycard_posx,keycard_posy)
            keycard_rect.center = (1000,1000)
            self.container.append({"x_cord":keycard_posx, "y_cord":keycard_posy, "collectable":True, "rect":keycard_rect, "color":self.keycard_colors[i]})
        
    
    def keycard_player_collision(self, player_rect):
        if self.collect_counter <= 2:
            # print(self.collect_counter)
            for keycard in self.container:
                # print("schleife")
                if keycard["rect"].colliderect(player_rect):
                    if keycard["collectable"] == True:
                        # print("collided")
                        keycard["collectable"] = False
                        self.collect_counter += 1
                        # print(self.collect_counter)
        elif self.collect_counter >= 3:
           self.all_collected = True
           

